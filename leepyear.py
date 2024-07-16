year = input("Please input year :")
year = int(year)
if year % 100 != 0 and year % 4 == 0:
    print(year, "is a LeepYear")
elif year % 100 == 0 and year % 400 == 0:
    print(year, "is a LeepYear")
else:
    print(year, "is not a LeepYear")