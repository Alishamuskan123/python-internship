import os
import sys
import time
from datetime import datetime

# File to store data
DATA_FILE = "app_data.txt"
QUIZ_FILE = "quiz_data.json"

# 1️ Calculator Functions
def calculator():
    print("\n" + "="*40)
    print("           CALCULATOR")
    print("="*40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        choice = int(input("\nSelect operation (1-4): "))
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"\nResult: {num1} × {num2} = {result}")
        elif choice == 4:
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} ÷ {num2} = {result}")
        else:
            print("\nInvalid operation choice!")
    except ValueError:
        print("\nInvalid input! Please enter numbers only.")
    
    input("\nPress Enter to continue...")

# 2️ Pattern Generator Functions
def pattern_generator():
    print("\n" + "="*40)
    print("       PATTERN GENERATOR")
    print("="*40)
    print("1. Star Pattern")
    print("2. Number Pattern")
    
    try:
        choice = int(input("\nSelect pattern type (1-2): "))
        rows = int(input("Enter number of rows: "))
        
        if choice == 1:
            print("\n--- Star Pattern ---")
            for i in range(1, rows + 1):
                print("*" * i)
        elif choice == 2:
            print("\n--- Number Pattern ---")
            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print(j, end=" ")
                print()
        else:
            print("\nInvalid pattern choice!")
    except ValueError:
        print("\nInvalid input! Please enter numbers only.")
    
    input("\nPress Enter to continue...")

# 3️ File Handling System
def file_handling():
    while True:
        print("\n" + "="*40)
        print("     FILE HANDLING SYSTEM")
        print("="*40)
        print("1. Add Data to File")
        print("2. View All Data")
        print("3. Back to Main Menu")
        
        try:
            choice = int(input("\nSelect option (1-3): "))
            
            if choice == 1:
                # Add data to file
                data = input("Enter data to save: ")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                try:
                    with open(DATA_FILE, "a") as file:
                        file.write(f"[{timestamp}] {data}\n")
                    print("\n✓ Data saved successfully!")
                except Exception as e:
                    print(f"\nError saving data: {e}")
                
            elif choice == 2:
                # View stored data
                try:
                    with open(DATA_FILE, "r") as file:
                        data = file.read()
                        if data.strip():
                            print("\n--- STORED DATA ---")
                            print(data)
                        else:
                            print("\nNo data found in file.")
                except FileNotFoundError:
                    print("\nNo data file found. Add some data first!")
                except Exception as e:
                    print(f"\nError reading file: {e}")
                
            elif choice == 3:
                break
            else:
                print("\nInvalid choice!")
                
        except ValueError:
            print("\nInvalid input! Please enter a number.")
        
        input("\nPress Enter to continue...")

# 4 Number Utilities
def number_utilities():
    while True:
        print("\n" + "="*40)
        print("        NUMBER UTILITIES")
        print("="*40)
        print("1. Check Even/Odd")
        print("2. Check Prime Number")
        print("3. Generate Multiplication Table")
        print("4. Back to Main Menu")
        
        try:
            choice = int(input("\nSelect option (1-4): "))
            
            if choice == 1:
                num = int(input("Enter a number: "))
                if num % 2 == 0:
                    print(f"\n{num} is EVEN")
                else:
                    print(f"\n{num} is ODD")
                    
            elif choice == 2:
                num = int(input("Enter a number: "))
                if num < 2:
                    print(f"\n{num} is NOT a prime number")
                else:
                    is_prime = True
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        print(f"\n{num} is a PRIME number")
                    else:
                        print(f"\n{num} is NOT a prime number")
                        
            elif choice == 3:
                num = int(input("Enter a number: "))
                print(f"\n--- Multiplication Table of {num} ---")
                for i in range(1, 11):
                    print(f"{num} × {i} = {num * i}")
                    
            elif choice == 4:
                break
            else:
                print("\nInvalid choice!")
                
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")
        
        input("\nPress Enter to continue...")

# 5️ Simple Quiz System
def simple_quiz():
    print("\n" + "="*40)
    print("        SIMPLE QUIZ SYSTEM")
    print("="*40)
    print("Answer the following questions:\n")
    
    # Quiz questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "answer": "C"
        },
        {
            "question": "Which programming language is known as Python?",
            "options": ["A. Snake", "B. Programming Language", "C. Operating System", "D. Database"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 3 × 2?",
            "options": ["A. 16", "B. 11", "C. 10", "D. 13"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a Python data type?",
            "options": ["A. Integer", "B. Float", "C. String", "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "What does CLI stand for?",
            "options": ["A. Command Line Interface", "B. Computer Language Input", "C. Code Line Integration", "D. Control Line Interface"],
            "answer": "A"
        }
    ]
    
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(f"   {option}")
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("   ✓ Correct!")
            score += 1
        else:
            print(f"   ✗ Wrong! Correct answer is {q['answer']}")
    
    # Show final score
    print("\n" + "="*40)
    print("         QUIZ COMPLETED!")
    print("="*40)
    print(f"Your Score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # Save score to file
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("quiz_scores.txt", "a") as file:
            file.write(f"[{timestamp}] Score: {score}/{len(questions)} ({percentage:.1f}%)\n")
        print("\n Score saved to file!")
    except Exception as e:
        print(f"\nError saving score: {e}")
    
    input("\nPress Enter to continue...")

# Bonus: Simple Login System
def login_system():
    print("\n" + "="*40)
    print("          LOGIN SYSTEM")
    print("="*40)
    
    # Simple credentials (in real app, you'd use database)
    users = {
        "admin": "admin123",
        "user": "user123"
    }
    
    try:
        username = input("Username: ")
        password = input("Password: ")
        
        if username in users and users[username] == password:
            print("\nLogin successful!")
            return True
        else:
            print("\n Invalid username or password!")
            return False
    except Exception as e:
        print(f"\nError during login: {e}")
        return False

# Main Menu Function
def main_menu():
    while True:
        # Clear screen for better visibility
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("="*50)
        print("     PYTHON CLI APPLICATION - MAIN MENU")
        print("="*50)
        
        print("\nCORE FEATURES:")
        print("  1. Calculator")
        print("  2. Pattern Generator")
        print("  3. File Handling System")
        print("  4. Number Utilities")
        print("  5. Simple Quiz System")
        print("\n BONUS FEATURES:")
        print("  6. Login System")
        print("  7. Exit")
        
        try:
            choice = int(input("\nSelect an option (1-7): "))
            
            if choice == 1:
                calculator()
            elif choice == 2:
                pattern_generator()
            elif choice == 3:
                file_handling()
            elif choice == 4:
                number_utilities()
            elif choice == 5:
                simple_quiz()
            elif choice == 6:
                if login_system():
                    input("\nPress Enter to continue...")
            elif choice == 7:
                print("\n" + "="*40)
                print("Thank you for using the application!")
                print("Goodbye! ")
                print("="*40)
                sys.exit()
            else:
                print("\nInvalid choice! Please select 1-7.")
                time.sleep(1)
                
        except ValueError:
            print("\nInvalid input! Please enter a number.")
            time.sleep(1)

# Main Program Entry Point
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye! ")
        sys.exit()