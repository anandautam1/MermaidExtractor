import xlsxwriter 

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1','Hello World')
worksheet.write('A2','Hello World')

workbook.close()