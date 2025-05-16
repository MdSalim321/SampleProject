from openpyxl import load_workbook


workbook =load_workbook("TestData.xlsx")
sheet =workbook.active

print(sheet["Login"].value)
