width = float(input())
height = float(input())
rashod = float(input())
obem = int(input())
zapas = int(input())

S = width * height
litri = S / rashod * (zapas / 100 + 1)
banki = litri // obem + 1
lishnie = banki * obem - litri
print(round(S, 2))
print(round(litri, 2))
print(int(banki))
print(round(lishnie, 2))

