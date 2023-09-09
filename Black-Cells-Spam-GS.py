import pygsheets
import random

# This script paints random cells in spreadsheet black

gc = pygsheets.authorize()

print("Enter URL")
URL = input()
sh = gc.open_by_url(URL)
print("Spreadsheet title ", sh._title)

# Get list of all worksheets
print(sh.worksheets())
print("Choose worksheet index")
list = int(input())
wks = sh[list]

rows_max = wks.rows
cols_max = wks.cols
print("Number of rows: ", wks.rows)
print("Number of columns: ", wks.cols)

print("Enter number of cells to paint black")
num = int(input())

print("Press any key to start")
input()

print("Spreedsheet erase started")

# Creating 50000 (maximum allowed string length) length string
longstring = ""
for i in range(5500):
    longstring = longstring + "[DELETED]"

for i in range(num):
    try:
        row = random.randint(1, rows_max)
        coll = random.randint(1, cols_max)

        cell = wks.cell([row, coll])
        cell.unlink()
        cell.value = "" # Also can write longstring to cell
        cell.note = "[ЭТО ТОЛЬКО НАЧАЛО]"
        cell.color = (0, 0, 0, 0)
        cell.update(force = True)
        
        print(100*i/num, "%")
    except Exception as Error:
        print(Error)