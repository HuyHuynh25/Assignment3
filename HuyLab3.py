########################################################################
##
## CS 101 Lab
## Program #
## Name: Huynh Gia Huy
## Email: hghydv@umsystem.edu
##
## PROBLEM : the great prognosticator “Flarsheim”, will let the user
## choose a number in their head from 1 to 100.
## It will then ask the remainder of this number when divided by 3, 5 and 7.
## To find what number the user is thinking of just find the number from
## 1 to 100 that has the same remainder for 3, 5, and 7 and astound them withthe resul
## ALGORITHM :
##      Step1: Start
##      Step2: print('Welcome to the Flarsheim Guesser!')
##      Step3: print('Please think of a number between and including 1 and 100.')
##      Step4: use while loop for user_input = 'Y'
##      Step5: create user_int1 and use condition for create user_int1
##      Step6: same as user_int2 and user_int3
##      Step7: print('How amazing is that?')
##      Step8: using loop for user_input for replay the game or not
##      Step9: end
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
print('Welcome to the Flarsheim Guesser!')
print('Please think of a number between and including 1 and 100.')
user_input = 'Y'
while user_input == 'Y' or user_input == 'y':
    user_int1 = int(input('What is the remainder when your number is divided by 3 ?'))
    if user_int1 < 0:
        print('The value entered must be 0 or greater')
    elif user_int1 > 2:
        print('The value entered must be less than 3')
    while user_int1 < 0 or user_int1 > 2:
        user_int1 = int(input('What is the remainder when your number is divided by 3 ?'))
        if user_int1 < 0:
            print('The value entered must be 0 or greater')
        elif user_int1 > 2:
            print('The value entered must be less than 3')
        continue
    user_int2 = int(input('What is the remainder when your number is divided by 5 ?'))
    if user_int2 < 0:
        print('The value entered must be 0 or greater')
    elif user_int2 > 4:
        print('The value entered must be less than 5')
    while user_int2 < 0 or user_int2 > 4:
        user_int2 = int(input('What is the remainder when your number is divided by 5 ?'))
        if user_int2 < 0:
            print('The value entered must be 0 or greater')
        elif user_int2 > 4:
            print('The value entered must be less than 5')
        continue
    user_int3 = int(input('What is the remainder when your number is divided by 7 ?'))
    if user_int3 < 0:
        print('The value entered must be 0 or greater')
    elif user_int3 > 6:
        print('The value entered must be less than 7')
    while user_int3 < 0 or user_int3 > 6:
        user_int2 = int(input('What is the remainder when your number is divided by 7 ?'))
        if user_int3 < 0:
            print('The value entered must be 0 or greater')
        elif user_int3 > 6:
            print('The value entered must be less than 7')
        continue
    for i in range(1, 101):
        if user_int1 == i % 3 and user_int2 == i % 5 and user_int3 == i % 7:
            print('Your number was {}'.format(i))
    print('How amazing is that?')
    user_input = input('Do you want to play again? Y to continue, N to quit  ==>')
    continue
while user_input == 'n':
    print('Have a great day!\n')
    break




