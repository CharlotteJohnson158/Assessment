# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Yarn.db'

#Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate


# This is the filename of the database to be used
DB_NAME = 'Yarn.db'
# This is the SQL to connect to all the tables in the database
TABLES = (" yarn "
          "LEFT JOIN brand ON yarn.brand_id = brand.brand_id "
          "LEFT JOIN weight ON yarn.weight_id = weight.weight_id ")

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Yarn database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: Yarn with the brand of either Bernat, or Caron\n'
                        'B: Choose the brand you want to see\n'
                        'C: Choose the hook size you want to see\n'
                        'D: Yarn with the brand of either Red Heart, or Lion Brand\n'
                        'E: Yarn that has the weight of either Sport, or Super Bulky\n'
                        'F: Yarn that has the weight of either Sport, or Worsted\n'
                        'G: Yarn that has the weight of Worsted\n'
                        'H: Choose the needle size you want to see\n'
                        'I: Choose the material you want to see\n'
                        'J: Yarn that has the material of Acrylic and Wool\n'
                        'K: Yarn that has the weight of either Bulky, or Super Bulky\n'
                        'L: Yarn that is made out of polyester\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('Bernat, Caron')
    elif menu_choice == 'B':
        print('Red Heart\nLion Brand\nBernat\nCaron\nRowan\nCascade Yarns')
        brand = input('Which brand of yarn do you want to see?: ')
        print_parameter_query("name, weight, colour", "brand = ? ORDER BY name ASC",brand)
    elif menu_choice == 'C':
        hook_size = input('Which hook size do you want to see?: ')
        print_parameter_query("brand, name, weight, colour", "hook_size = ? ORDER BY brand DESC",hook_size)
    elif menu_choice == 'D':
        print_query('Red Heart, Lion Brand')
    elif menu_choice == 'E':
        print_query('Sport or Super Bulky')
    elif menu_choice == 'F':
        print_query('Sport or Worsted')
    elif menu_choice == 'G':
        print_query('Worsted Weight')
    elif menu_choice == 'H':
        needle_size = input('Which needle size do you want to see?: ')
        print_parameter_query("brand, name, weight, colour", "needle_size = ? ORDER BY weight DESC",needle_size)
    elif menu_choice == 'I':
        materials = input('Which material do you want to see?: ')
        print_parameter_query("brand, name, weight, colour, materials", "materials = ? ORDER BY weight ASC",materials)
    elif menu_choice == 'J':
        print_query('Acrylic and Wool')
    elif menu_choice == 'K':
        print_query('Bulky or Super Bulky')
    elif menu_choice == 'L':
        print_query('Polyester')