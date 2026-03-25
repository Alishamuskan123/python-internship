"""
Patterns and Sequence Builder - Simple Version
A beginner-friendly Python program that generates number and star patterns
"""

# ==================== PATTERN FUNCTIONS ====================

def star_triangle(size):
    """Prints a triangle of stars"""
    print("\n--- STAR TRIANGLE ---")
    # Loop for each row
    for i in range(1, size + 1):
        # Print stars for current row (i stars)
        for j in range(i):
            print("*", end="")
        print()  # New line after each row

def reverse_star(size):
    """Prints an inverted triangle of stars"""
    print("\n--- REVERSE STAR ---")
    # Loop from size down to 1
    for i in range(size, 0, -1):
        # Print stars for current row (i stars)
        for j in range(i):
            print("*", end="")
        print()

def number_triangle(size):
    """Prints a triangle of numbers"""
    print("\n--- NUMBER TRIANGLE ---")
    # Loop for each row
    for i in range(1, size + 1):
        # Print numbers 1 to i
        for j in range(1, i + 1):
            print(j, end="")
        print()

def number_pyramid(size):
    """Prints a centered pyramid of numbers"""
    print("\n--- NUMBER PYRAMID ---")
    # Loop for each row
    for i in range(1, size + 1):
        # Print spaces for centering
        for s in range(size - i):
            print(" ", end="")
        # Print numbers 1 to (2*i - 1)
        for j in range(1, 2*i):
            print(j, end="")
        print()

def print_all_patterns(size):
    """Prints all patterns one after another"""
    print("\n" + "=" * 40)
    print("   GENERATING ALL PATTERNS")
    print("=" * 40)
    
    # Call all pattern functions
    star_triangle(size)
    reverse_star(size)
    number_triangle(size)
    number_pyramid(size)
    
    print("\n" + "=" * 40)
    print("   ALL PATTERNS GENERATED!")
    print("=" * 40)

# ==================== MAIN PROGRAM ====================

print("=" * 40)
print("   PATTERNS AND SEQUENCE BUILDER")
print("=" * 40)

# Keep showing menu until user chooses to exit
while True:
    # Display menu
    print("\nChoose a pattern:")
    print("1. Star Triangle")
    print("2. Reverse Star Pattern")
    print("3. Number Triangle")
    print("4. Number Pyramid")
    print("5. Print ALL Patterns")
    print("6. Exit")
    
    # Get user choice
    choice = input("\nEnter your choice (1-6): ")
    
    # Exit program
    if choice == "6":
        print("\nGoodbye! Thanks for using Pattern Builder!")
        break
    
    # Validate choice is 1-5
    if choice not in ["1", "2", "3", "4", "5"]:
        print("❌ Invalid choice! Please enter 1, 2, 3, 4, 5, or 6")
        continue
    
    # Get pattern size
    try:
        size = int(input("Enter pattern size (positive number): "))
        
        # Check if size is positive
        if size <= 0:
            print("❌ Error: Size must be positive!")
            continue
            
    except ValueError:
        print("❌ Error: Please enter a valid number!")
        continue
    
    # Generate the selected pattern
    if choice == "1":
        star_triangle(size)
    elif choice == "2":
        reverse_star(size)
    elif choice == "3":
        number_triangle(size)
    elif choice == "4":
        number_pyramid(size)
    elif choice == "5":
        print_all_patterns(size)
    
    print("\n" + "-" * 30)
    
    # Ask if user wants to continue
    again = input("Generate another pattern? (y/n): ")
    if again.lower() != "y":
        print("\nGoodbye! Thanks for using Pattern Builder!")
        break