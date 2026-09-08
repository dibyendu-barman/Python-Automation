from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active
ws.title = "Summary"

ws.append(["Result", "Count"])
ws.append(["PASS", 21])
ws.append(["FAIL", 4])

chart = BarChart()
chart.title = "Test Results"
chart.y_axis.title = "Count"
chart.x_axis.title = "Result"

data = Reference(ws, min_col=2, min_row=1, max_row=3)
categories = Reference(ws, min_col=1, min_row=2, max_row=3)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
ws.add_chart(chart, "D2")

wb.save("reports/test_dashboard.xlsx")
print("Created: reports/test_dashboard.xlsx")