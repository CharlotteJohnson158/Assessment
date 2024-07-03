# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Yarn.db'

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
                        'B: Yarn from the brand Cascade Yarns\n'
                        'C: All yarn with the hook sizes of 4mm, 4.5mm, or 5mm\n'
                        'D: Yarn with the brand of either Red Heart, or Lion Brandn\n'
                        'E: Yarn that has the weight of either Sport, or Super Bulky\n'
                        'F: Yarn that has the weight of either Sport, or Worsted\n'
                        'G: Yarn that has the weight of Worsted\n')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('Bernat,Caron')
    elif menu_choice == 'B':
        print_query('Cascade Yarns')
    elif menu_choice == 'C':
        print_query('Hook Sizes')
    elif menu_choice == 'D':
        print_query('Red Heart, or Lion Brand')
    elif menu_choice == 'E':
        print_query('Sport or Super Bulky')
    elif menu_choice == 'F':
        print_query('Sport or Worsted')
    elif menu_choice == 'G':
        print_query('Worsted Weight')

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


brand = input('Which brand of yarn do you want to see?: ')
print_parameter_query("name, weight, colour", "brand = ? ORDER BY weight ASC",brand)
