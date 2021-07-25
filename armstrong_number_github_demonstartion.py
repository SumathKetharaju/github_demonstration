# Python program to check armstrong number of n digits

num = 1634
# num = int(input("Enter a three digit number: "))
# Changed the num variable to string, and calculated the length(number of digits)
order = len(str(num))
# Initialize the sum
sum = 0
# Find the sum cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
# Display the result
if sum == num:
    print("Given number", num, "is an armstrong number")
else:
    print("Given number", num, "is not an armstrong number")
