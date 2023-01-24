def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
while True:
    year = input("Geben sie eine Jahreszahl ein (oder tippen sie  'exit' zum beenden): ")
    if year == "exit":
        break
    year = int(year)
    if is_leap_year(year):
        print(year, "Das ist EIN Schaltjahr.")
    else:
        print(year, "Das ist KEIN Schaltjahr.")