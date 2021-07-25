# Python program to display calender
"""In the program below we import the calendar module.
The builtin function month() inside the module takes in the year and the month and,
displays the calender for that month of the year."""


# importing calender module
import calendar
yy = 2021
mm = 6
# To take month and year input from the user
# yy = int((input("Enter a year: ")))
# mm = int((input("Enter a month: ")))

# Display the calendar
print(calendar.month(yy, mm))
