import random

kolmenumeroinen_koodi = ""
for _ in range(3):
    kolmenumeroinen_koodi += str(random.randint(0, 9))

nelinumeroisen_koodi = ""
for _ in range(4):
    nelinumeroisen_koodi += str(random.randint(1, 6))

print(f"Kolmenumeroinen koodi: {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {nelinumeroisen_koodi}")
