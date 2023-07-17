import xlwings as xw
app = xw.App(True,True)
book = app.books.open('Answers.xlsx')
sheet = book.sheets['Sheet1']
area = sheet.range(1,1)
area.value = 'Analysis'
area = sheet.range(1,2)
area.value = 'Question'
area = sheet.range(1,3)
area.value = 'Tanswer'
area = sheet.range('D1:F1')
area.value = 'Eanswer'
for i in range(10):
    area = sheet.range(i + 2, 1)
    area.value = 'Analysis:' + str(i + 1)
for i in range(10):
    area = sheet.range(i + 2, 2)
    area.value = 'Question:' + str(i + 1)
for i in range(10):
    area = sheet.range(i + 2, 3)
    area.value = 'Tanswer:' + str(i + 1)
for i in range (3):
    for a in range(10):
        area = sheet.range(a + 2, i+4)
        area.value = 'Eanwser:' + str(a + 1)

book.save()
book.close()
app.quit()