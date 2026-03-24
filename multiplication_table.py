print('='*40)
print('MULTIPLICATION TABLE GENERATOR')
print('='*40)

# Variable for multiple sessions (bonus feature)
continue_program=True

# Variable for multiple sessions (bonus feature)
while continue_program:
# Get user input with validation
    while True:
        try:
            number=int(input('\nENTER A NUMBER:'))
            if number<0:
                print('PLEASE ENTER A POSITIVE NUMBER:')
                continue
            break
        except ValueError:
            print('INVALID INPUT!PLEASE ENTER A NUMBER:')
    while True:
        try:
            range_limit=int(input('ENTER THE RANGE:'))
            if range_limit<0:
                print('ENTER A POSITIVE NUMBER:')
                continue
            break
        except ValueError:
            print('INVAID INPUT!PLEAS ENTER A NUMBER:')
    # FOR LOOP - Generates the multiplication table with highlights
    print(f'\nMULTIPLICATION OF TABLE OF {number}')
    print('-'*40)
    for i in range(range_limit+1):
        result=number*i
        # Check if result is multiple of 10 or 5
        if result%10==0:
            # Multiple of 10 (also multiple of 5)
            print(f'{number}*{i}={result} *SPECIAL:Multiple of 10*')
        elif result%5==0:
            # Multiple of 5 only (not 10)
            print(f"{number}*{i}={result} *SECIAL:Multiple of 5*")
        else:
            #Regular output
            print(f'{number}*{i}={result}')
    print('-'*40)
    # Ask if user wants to generate another table
    another=input('GENERATE ANOTHER TABLE(y/n):').lower()
    if another!='y':
        continue_program=False

print("\nThank you for using Multiplication Table Generator!")
