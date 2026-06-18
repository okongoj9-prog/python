Monthly_contribution = int(input("What is your Monthly_contribution ? "))

if  Monthly_contribution < 5999:
    print("Monthly contribution is 150.00 Ksh")
elif Monthly_contribution >= 6000 and Monthly_contribution <= 7999:
    print("“Monthly contribution is 300.00 Ksh”")
elif Monthly_contribution >= 8000 and Monthly_contribution <= 11999:
    print("“Monthly contribution is 400.00 Ksh”")
elif Monthly_contribution >= 12000 and Monthly_contribution <= 14999:
    print("“Monthly contribution is 500.00 Ksh”")
elif Monthly_contribution >= 15000 and Monthly_contribution <= 19999:
    print("“Monthly contribution is 600.00 Ksh”")
elif Monthly_contribution >= 20000 and Monthly_contribution <= 24999:
    print("“Monthly contribution is 750.00 Ksh”")
elif Monthly_contribution >= 25000 and Monthly_contribution <= 29999:
    print("“Monthly contribution is 850.00 Ksh”")
elif Monthly_contribution > 30000 and Monthly_contribution <= 49999:
    print("“Monthly contribution is 1,000.00 Ksh”")
elif Monthly_contribution >= 50000 and Monthly_contribution <= 99999:
    print("“Monthly contribution is 1,500.00 Ksh”")
elif Monthly_contribution >= 100000:
    print("“Monthly contribution is 2,000.00 Ksh”")
else:
    print("“Not in the monthly contribution”")