# import sys
# if len(sys.argv)==2:
#     script_name = sys.argv[0]
#     celsius = float(sys.argv[1])
# else:
#     script_name = sys.argv[0]
#     celsius = 30
# print("Invalid inpur using default values.")
# f = (celsius * 1.8) + 32

# print(f"Celsius : {celsius}")
# print(f"Fahrenheit : {f}")


import sys

# Check if argument is provided
if len(sys.argv) == 2:
    try:
        celsius = float(sys.argv[1])
    except ValueError:
        print("Error: Please enter a numeric value.")
        sys.exit(1)
else:
    print("Usage: python program.py <celsius>")
    sys.exit(1)

fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)