import sys

if len(sys.argv) == 2:
    salary = float(sys.argv[1])
    print("User provided salary:")
else:
    salary = 50000
    print("No input given - using default salary:")

bonus = salary * 0.10
total = salary + bonus

print("Bonus Amount:", bonus)
print("Total Salary:", total)
