"""
    Fuzz-Buzz
    ---------
Fizz-Buzz is a game that is sometime played by childern to help them learn about division
-->if the player's number is divisible by 3then the player says fizz instead of their number
-->if the player's number is divisible by 3then the player says fizz instead of their number
-->A player must say both fizz and buzz for number that are divisible by both 3 and 5
to display the ans for the first 100 numbers in the fizz buzz game
"""
for i in range(1,16):
    if(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)
        
