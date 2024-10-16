'''Question: FizzBuzz

Write a program that prints the numbers from 1 to 100.
But for multiples of three, print "Fizz" instead of the number,
and for the multiples of five, print "Buzz".
For numbers which are multiples of both three and five, print "FizzBuzz".'''

def fizzbuz():
    i = 0
    while i<=100:
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZBUZZ")
        elif i%5 == 0:
            print("BUZZ")
        elif i%3 == 0:
            print("FIZZ")
        else:
            print(i)
        i += 1

fizzbuz()