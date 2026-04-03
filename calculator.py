#ADVANCED CALCULATOR
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError(" Cannot divide by zero!")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def modulus(self, a, b):
        if b == 0:
            raise ValueError(" Cannot calculate modulus with zero!")
        return a % b
    
    def add_to_history(self, operation, num1, num2, result):
        """Store calculation in history"""
        entry = f"{num1} {operation} {num2} = {result}"
        self.history.append(entry)
        
        # Keep only last 10 calculations
        if len(self.history) > 10:
            self.history.pop(0)
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("\n No calculations yet!")
        else:
            print("\n" + "="*35)
            print("     CALCULATION HISTORY")
            print("="*35)
            for i, entry in enumerate(self.history, 1):
                print(f"{i}. {entry}")
            print("="*35)
    
    def get_number(self, prompt):
        """Get valid number with retry mechanism"""
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print(" Invalid! Please enter a number (e.g., 5, 3.14, -2)")
    
    def display_menu(self):
        """Display enhanced menu"""
        print("\n" + "="*35)
        print("        ADVANCED CALCULATOR")
        print("="*35)
        print("1.  Addition")
        print("2.  Subtraction")
        print("3.   Multiplication")
        print("4.  Division")
        print("5.  Power (xʸ)")
        print("6.  Modulus (remainder)")
        print("7.  View History")
        print("8.   Clear History")
        print("9.  Exit")
        print("-"*35)
    
    def print_result(self, num1, num2, operation, result):
        """Helper function to print result clearly"""
        print("\n" + "="*35)
        print(" CALCULATION COMPLETE! ")
        print("="*35)
        print(f" {num1} {operation} {num2} = {result:.4f}")
        print("="*35)
        print("Result displayed successfully!\n")
    
    def run(self):
        """Main calculator loop"""
        print("\n" + "*"*18)
        print("   WELCOME TO ADVANCED CALCULATOR")
        print("   With History & Error Handling!")
        print("*"*18)
        
        while True:
            self.display_menu()
            choice = input("\n Choose option (1-9): ").strip()
            
            # Exit
            if choice == '9':
                print("\n Thanks for calculating! Goodbye!")
                break
            
            # View history
            if choice == '7':
                self.show_history()
                continue
            
            # Clear history
            if choice == '8':
                self.history.clear()
                print("\n  History cleared successfully!")
                continue
            
            # Validate operation choice
            if choice not in ['1', '2', '3', '4', '5', '6']:
                print(" Invalid choice! Please select 1-9")
                continue
            
            # Get numbers
            print("\n Enter your numbers:")
            num1 = self.get_number("   First number: ")
            num2 = self.get_number("   Second number: ")
            
            # Print confirmation that numbers were received
            print(f"\n Numbers received: {num1} and {num2}")
            print("Calculating result...")
            
            # Perform calculation
            try:
                if choice == '1':
                    result = self.add(num1, num2)
                    operation = "+"
                    print(f" Performing addition...")
                elif choice == '2':
                    result = self.subtract(num1, num2)
                    operation = "-"
                    print(f" Performing subtraction...")
                elif choice == '3':
                    result = self.multiply(num1, num2)
                    operation = "×"
                    print(f"  Performing multiplication...")
                elif choice == '4':
                    result = self.divide(num1, num2)
                    operation = "÷"
                    print(f" Performing division...")
                elif choice == '5':
                    result = self.power(num1, num2)
                    operation = "^"
                    print(f" Performing power calculation...")
                elif choice == '6':
                    result = self.modulus(num1, num2)
                    operation = "%"
                    print(f"  Performing modulus calculation...")
                
                # Display result using the helper function
                self.print_result(num1, num2, operation, result)
                
                # Save to history
                self.add_to_history(operation, num1, num2, f"{result:.4f}")
                print(f" Result saved to history! (Total: {len(self.history)} calculations)")
                
            except ValueError as e:
                print(f"\n  {e}")
                print("Calculation failed! Please try again.")
            except OverflowError:
                print("\n Result too large to compute!")
                print(" Calculation failed! Please try smaller numbers.")
            except Exception as e:
                print(f"\n Unexpected error: {e}")
                print(" Calculation failed! Please try again.")
            
            # Add a separator for clarity
            print("\n" + "─"*35)
            input("Press Enter to continue...")

# Run the program
if __name__ == "__main__":
    calc = Calculator()
    calc.run()