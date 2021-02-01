import PyPDF2

# Создание объекта pdf
pdfFileObj = open('lorem-ipsum.pdf', 'rb')

# Создание объекта reader
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Количество страниц в pdf файле
print(pdfReader.numPages)

# Создание объекта страницы
pageObj = pdfReader.getPage(0)

# Извлечение текста из страницы
print(pageObj.extractText())

# Закрытие объекта pdf
pdfFileObj.close()