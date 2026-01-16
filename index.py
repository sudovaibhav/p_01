import sys
if len(sys.argv)==2:
    script_name = sys.argv[0]
    celsius = sys.argv[1]
else:
    script_name = sys.argv[0]
    celsius = 30
print("Invalid inpur using default values.")
f = (float(celsius) * 1.8) + 32

print("Celsius : ", celsius)
print("Fahrenheit : ", f)