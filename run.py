# Import necessary libraries
import gspread  # Library for interacting with Google Sheets
from google.oauth2.service_account import Credentials  # Handles authentication
from pprint import pprint


# Define the required scopes (permissions) for Google Sheets and Google Drive access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",  # Access Google Sheets
    "https://www.googleapis.com/auth/drive.file",  # Access specific files in Google Drive
    "https://www.googleapis.com/auth/drive"  # Full access to Google Drive
]

# Load credentials from a service account JSON file (creds.json)
# This file contains authentication details for accessing Google services securely
CREDS = Credentials.from_service_account_file('creds.json')

# Apply the defined scopes to the credentials
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Authorize gspread using the scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet named 'love-sandwiches' from the authenticated account
SHEET = GSPREAD_CLIENT.open('love-sandwiches')

# Access the 'sales' worksheet within the spreadsheet
sales = SHEET.worksheet('sales')

# Retrieve all data from the 'sales' worksheet as a list of lists
data = sales.get_all_values()

# Print the retrieved data to the console
print(data)

def get_sales_data():
    
    """
    Get sales figures input from the user.
    """
    
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")
            
        data_str = input("Enter your data here: ")
        
        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid")
            break
        
    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
        
  
    return True 


def update_sales_worksheet(data):
    '''
    Update sales worksheet, add new row with new data provided
    '''
    
    print("Updating sales worksheet...\n")  
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n") 
    
    
def update_surplus_worksheet(data):
    '''
    Update surplus worksheet, add new row with new data provided
    '''
    
    print("Updating surplus worksheet...\n")  
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully.\n")  
         
    

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    - The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    
    surplus_data =[]
    for stock, sales in zip (stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

    
    
def main():
    '''
    Run all program functions
    '''
  
data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)
new_surplus_data = calculate_surplus_data(sales_data) 
update_surplus_worksheet(new_surplus_data)

      

print("Welcome to Love Sandwiches Data Automation")
main()
