text = '‹span›58nbsp;1288nbsp;Pc/span>'
result = ''
for e in text:
    if e.isdigit():
        result += e

print(result)