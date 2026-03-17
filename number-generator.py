def main():
    print("===SIMPLE NUMBER ANALYZER===\n")
    # List to store analyzed numbers (bonus feature)
    analyzed_numbers = []

    while True:
        try:
            # Take user input
            num = int(input('ENTER A NUMBER: (0 to quit!) '))
            
            # Check if user wants to quit
            if num == 0:
                break
                
            # Add to list (bonus feature)
            analyzed_numbers.append(num)
            
            print('\n---RESULTS---')
            
            # 1. Check Positive/Negative/Zero
            if num > 0:
                print('Number is POSITIVE')
            elif num < 0:
                print('Number is NEGATIVE')
            else:
                print('Number is ZERO')
            
            # 2. Check Even/Odd
            if num % 2 == 0:
                print('Number is EVEN')
            else:
                print('Number is ODD')
            
            # 3. Check divisibility by both 3 AND 5 (using AND)
            if num % 3 == 0 and num % 5 == 0:
                print('Number is divisible by both 3 and 5')
            
            # 4. Check range 1-100 using AND
            if num >= 1 and num <= 100:
                print('Number is within range 1-100')
            
            # 5. Check special condition using OR
            if num % 3 == 0 or num % 5 == 0:
                print("Number is divisible by 3 OR 5")
            
            # 6. Check special condition using AND and NOT
            if num > 0 and num % 2 == 0 and num >= 1 and num <= 100 and not (num % 3 == 0 and num % 5 == 0):
                print('✨ SPECIAL CONDITION MATCHED!')
            
            print('-' * 30)
            
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
    
    # SUMMARY 
    print("\n===SUMMARY===")
    if analyzed_numbers:
        print(f"TOTAL NUMBERS ANALYZED: {len(analyzed_numbers)}")
        print(f"NUMBERS: {analyzed_numbers}")
    else:
        print("No numbers were analyzed.")
    print("THANK YOU FOR USING ANALYZER")

# Run the program
if __name__ == '__main__':
    main()