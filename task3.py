# 3. Write a program that reads an integer number and prints its previous and
# next numbers. See the examples below for the exact format your answers
# should take. There shouldn't be a space before the period.
# Remember that you can convert the numbers to strings using the function str.
# (The next number for the number 179 is 180. The previous number for the number 179 is 178.)

number = int(input("Enter your number: "))
print("The previous number for the", number, "is" , number-1 ,".","The next number for the" , number , "is" , number+1)


