# 	6. Check if a year is a leap year

year = int(input("Enter the Year :"))

if((year % 4 == 0) or ((year % 100 != 0) and (year % 400 == 0))):
    print(year, " is a Leap Year")
else:
    print(year , "is Not a Leap Year")