#Simple Interest Calculator

principal_amt = float(input("Enter Principal amount:"))
time_years = int(input("Enter Time Period:"))
rate_of_interest = float(input("Enter rate of interest:"))

SI = (principal_amt*time_years*rate_of_interest) / 100

print("The computed interest is:")
print(SI)