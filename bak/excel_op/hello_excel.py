import xlsxwriter

excel_data = list()

title = ('COL_A', 'COL_B')
excel_data.append(title)

def write_to_sheet(workbook, sheet, data_list, LOG):
    color_format = workbook.add_format()
    color_format.set_bg_color('#FFFF00')

    for row_num, columns in enumerate(data_list):
        for col_num, cell_data in enumerate(columns):
            sheet.write(row_num, col_num, cell_data, color_format)
    return

def write_excel(excel_file, LOG):
    workbook = xlsxwriter.Workbook(excel_file)
    
    sheet_name = 'Test'
    worksheet1 = workbook.add_worksheet(sheet_name)
    worksheet1.set_column('A:C', 30)
    worksheet1.set_column('D:E', 20)
    
    line_data = ('Hello', 'Hello')
    # line_data.append('Hello', 'Hello')
    excel_data.append(line_data)
    write_to_sheet(workbook, worksheet1, excel_data, LOG)
    
    workbook.close()
    return

def test():
    write_excel('Hello.xls', None)
    print('test')

if __name__ == '__main__':
   test()