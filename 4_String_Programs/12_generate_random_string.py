# program to generate random strings until a given string is generated

import string, random

main_str = input("Enter the string\n")

print("Entered string is '" + main_str + "'")

possibleChars = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

attempt_main = ''.join(random.choice(possibleChars)
                       for i in range(len(main_str)))

attempt_next = ''

completed = False
iteration = 0

while completed == False: 
    print(attempt_main) 
      
    attempt_next = '' 
    completed = True
    
    for i in range(len(main_str)): 
        if attempt_main[i] != main_str[i]: 
            completed = False
            attempt_next += random.choice(possibleChars) 
        else: 
            attempt_next += main_str[i] 
  
    iteration += 1
    attempt_main = attempt_next

print("Target matched after " + str(iteration) + " iterations")

