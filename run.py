import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CILENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CILENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbets, sapreted by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here:")

    sales_data = data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings connot br converted inti int,
    or if there aren't exactly 6 values. 
    """
    try:
        [int(value) for value in values]
        if len(values) != 6 :
            raise ValueError(
                f"Exactly 6 values requaired, you provided {len(values)} "
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_sales_data()