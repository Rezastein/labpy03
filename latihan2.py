maks = 0
while True:
    a = int(input("Masukan bilangan = "))
    if maks < a:
        maks = a
    if a == 0:
        break
print("Bilangan Terbesarnya Adalah = ", maks)
