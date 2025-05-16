from openpyxl import Workbook

# Create and managing the xlsx file for 3 files
for f in range(1, 4):
    wb = Workbook()
    ws = wb.active
    ws.title = f"fake_data{f}.xlsx"
    for i in range(1, 20):
        ws.append([f"stu_id{i}", f"fn{i}", 60*(i%3)])
    wb.save(f"fake_data{f}.xlsx")