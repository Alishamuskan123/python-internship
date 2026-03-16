# Simple User Profile Generator

# Get user inputs
full_name = input("Enter your full name: ").capitalize()
age = input("Enter your age: ")
city = input("Enter your city: ").capitalize()
profession = input("Enter your profession/field of study: ").title()
fav_language = input("Enter your favorite programming language: ").capitalize()
bio = input("Enter a short bio (1-2 lines): ").capitalize()


# Convert age to integer (type casting)
age = int(age)

# Display the profile
print("\n==================================")
print("        USER PROFILE SUMMARY")
print("===================================")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Profession: {profession}")
print(f"Favorite Language: {fav_language}")
print(f"\nBio:\n{bio}")
print("====================================")