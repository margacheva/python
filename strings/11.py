number = '+79918069162'
print('<a href="tel:"' + number + '"' + ">" + number + "</a>")

inp = '<a href="tel:+79918069162">+79918069162</a>'
result = ''
for e in inp:
    if e.isdigit() == True:
        result += e
    else:
        pass
print(int(result))