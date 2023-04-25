# this is a hotel bill split calculator
print("welcome to the tip calculator.")
bill=float(input("what is the total bill? "))
tip=float(input("what persentage tip would you like to give? 10,12 or 15? "))
people=float(input("how many people to split the total bill? "))
# here we will calculate the bill after adding the tip
p_bill=(bill+ (bill*tip)/100)/people
print("each person should pay: $",round(p_bill,2))