import hashlib
import gspread
from google.oauth2.service_account import Credentials


def MD5(input_value):
    value = str(input_value)
    return hashlib.md5(value.encode()).hexdigest()

def update_md5_columns(sheet_id, sheet_name):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]

    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes) # Path to your service account key file
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).worksheet(sheet_name)

    # Read all values
    data = sheet.get_all_values()

    col_c = []  
    col_d = []  

    for row in data:
        
        if len(row) >= 1 and row[0].strip() != "":
            col_c.append([MD5(row[0])])
        else:
            col_c.append([""])
        if len(row) >= 2 and row[1].strip() != "":
            col_d.append([MD5(row[1])])
        else:
            col_d.append([""])

    # Write MD5 to Column C & D
    sheet.update(f"C1:C{len(col_c)}", col_c)
    sheet.update(f"D1:D{len(col_d)}", col_d)

    print("MD5 hashes written: Column A → C, Column B → D")

# ---- RUN ----
update_md5_columns(
    sheet_id="SheetID_here",
    sheet_name="Sheet1"
)


