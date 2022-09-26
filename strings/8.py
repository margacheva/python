string = "Экономический рост тесно связан с ростом общего благостояния."
iy = "ический"
ya = "ическая"
if iy in string:
      string = string.replace(iy, '.')
else:
      string = string.replace(ya, '.')

print(string)