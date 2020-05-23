'''
Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

sum = 0

for num in range(0, 1000):
    #if num is divisible by 3 and 5 - add num to sum, else, check that it's divisible by 5 OR 3, or else - ignore it
    if (num % 5 == 0) and (num % 3 == 0):
        sum += num
    else:
        # if num is div by 5 OR 3, add to sum
        if (num % 5 == 0) or (num % 3 == 0):
            sum += num
print(sum)


#This code ouputted solution in 0.125 seconds