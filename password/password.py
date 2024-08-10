import random

print("Welcome to password generator")


enter_number = input("Enter your number = ")

alphabet = ["a" , "b" , "c" , "d" , "e" , "f" ,  "g" ,  "h", 
            "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "w", "x", "y", "z", "A" , "B" , 
            " C" , "D" ," E" , "F" ,"G" ,"H" , "I ", "J" , "K" ,
           " L ","M" ," N" , "O" , 'P', "Q" , "R" , "S" ,"T" 
           ,"U" , "W" , "X" ,"Y" , "Z"]


numbers = ["0" , '1' , "2" , "3", "4" ,"5" ,"6","7","8","9",]

special_character  = ["@" , "$" , '% '," &" ,"*" , "#"]


n_alphabet = int(input("How many letter you want in your password =  \n"))
n_numbers = int(input("How many number you want in your password =  \n"))
n_sepcial_character = int(input("How many special character you want in your password =  \n"))

password = ""

for i in range(1 , n_alphabet +1):
    store = random.choice(alphabet)
    password += store

for i in range(1 , n_numbers + 1):
    store = random.choice(numbers)
    password += store

for i in range(1 , n_sepcial_character + 1):
    char = random.choice(special_character)
    password +=store

print(password)