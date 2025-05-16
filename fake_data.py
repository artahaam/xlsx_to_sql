from openpyxl import Workbook
import random
for f in range(1, 4):
    wb = Workbook()
    ws = wb.active
    ws.title = f"fake_data{f}.xlsx"
    for i in range(1, 20):
        ws.append([f"stu_id{i}", f"fn{i}", random.randint(0,100)])
    wb.save(f"fake_data{f}.xlsx")