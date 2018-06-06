import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import *


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)

client = gspread.authorize(creds)
sheet = client.open("Alpha").sheet1

data = sheet.get_all_records()

print(data)


pp = PrettyPrinter()
pp.pprint(data)
