import pygsheets as pgs
import time

# This script slowly clears google spreadsheet row by row

# Authorization with Google API
gc = pgs.authorize()

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

print("Press any key to start")
input()

print("Spreedsheet erase started")

currentRow = 3
while(currentRow < rows_max):
    startAdr = pgs.Address((currentRow, 1))
    endAdr = pgs.Address((currentRow, cols_max))
    wks.clear(start = startAdr, end = endAdr, fields='*')
    # Unmerging cells, if cannot unmerge add next row to cells range and try to unmerge again 
    fl = 1
    rows = 0
    while(fl):
        try:
            wks.merge_cells(start = startAdr, end = endAdr, merge_type = 'NONE', grange=None)
            fl = 0
        except Exception as Error:
            rows += 1
            endAdr = pgs.Address((currentRow + rows, cols_max))
    currentRow += 1
    # Spreadsheet clearing progress
    print("Erased ", 100*currentRow/wks.rows, " %")
    time.sleep(1)