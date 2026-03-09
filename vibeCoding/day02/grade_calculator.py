# Grade Calculator Script

# Get student information
name = input("Enter student's name: ")

# Get 3 subject marks
mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

# Calculate the average
average = (mark1 + mark2 + mark3) / 3

# Determine pass or fail
result = "Pass" if average >= 40 else "Fail"

# Display results
print(f"\n--- Results for {name} ---")
print(f"Average Mark: {average:.2f}")
print(f"Status: {result}")