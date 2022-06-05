print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
bill2 = round(bill,2)
total_percentage = float(input("What percentage tip would you like to give 10 , 12 , 15 "))
percentage = (total_percentage/100) * bill
percentage2 = round(percentage , 2)
total_bill = percentage2 + bill2
split = int(input("How many no. of people to split the bill? "))
final_bill = total_bill / split
show_bill = round(final_bill,2)
show_bill = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${show_bill}")