# Import necessary libraries
import gspread  # Library for interacting with Google Sheets
from google.oauth2.service_account import Credentials  # Handles authentication

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
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")
        
    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")
        
get_sales_data()
