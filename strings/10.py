string = "+7(991)80-69-162"
elements = ['(', ')', '-', ' ']
for i in range(len(elements)):
    if elements[i] in string:
        string = string.replace(elements[i], '')

print(string)
