import sqlparse

 # Деление строки содержащей два SQL запроса
query = 'select * from foo; select * from bar;'
statements = sqlparse.split(query)
print(statements)

# Нормализация формата первого запроса
first = statements[0]
print(sqlparse.format(first, reindent=True, keyword_case='upper'))

# Парсинг запроса на токены
parsed = sqlparse.parse('select * from foo')[0]
print(parsed.tokens)