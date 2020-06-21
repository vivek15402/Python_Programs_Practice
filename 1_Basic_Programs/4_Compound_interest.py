# program for compound interest

principal = float(input("Enter principal value\n"))
rate = float(input("Enter rate\n"))
time = float(input("Enter time\n"))

ci = principal * pow( (1 + (rate/100)) , time)

print(ci)
