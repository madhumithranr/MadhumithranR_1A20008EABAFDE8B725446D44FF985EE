def checleap(year):
  # checking if the  given year is leap year
  if ((year % 400 == 0) or 
(year % 100 != 0) and 
(year % 4 == 0)):
    print("given year is a leap year")
    # Else it is not a leap year
  else:
    print(" given year is not a leap year")
    # Taking an input year from user
    year = int(input("Enter the number:"))
    #printing result
    checkLeap(year)
