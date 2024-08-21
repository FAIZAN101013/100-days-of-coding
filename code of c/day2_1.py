
def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a Leap Year"
            else:
                return f"{year} is not a Leap Year"
        else:
            return f"{year} is a Leap Year"
    else:
        return f"{year} is not a Leap Year"
    
def main():
    year = int(input("Enter the year>> "))
    is_leap = leap(year)
    print(is_leap)


main()

 