leiviska=int(input("Anna leiviskät:"))
naula=int(input("Anna naulat:"))
luoti=int(input("Anna luodit:"))

luoti_g=13.3
naula_g=32*luoti_g
leiviska_kg=20*naula_g

kokonaispaino_g = (leiviska * leiviska_kg * 1000) + (naula * naula_g) + (luoti * luoti_g)
kg = kokonaispaino_g // 1000
g = kokonaispaino_g % 1000

print(f"Kokonaispaino on: {int(kg)} kg ja {g:.1f} g")
