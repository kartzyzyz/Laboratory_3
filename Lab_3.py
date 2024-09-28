monthly_salary = float(input("Enter your monthly salary: "))
loan_amount = float(input("Enter the amount that you are about to loan: "))
if monthly_salary >= 30000.00 and loan_amount <= 10 * monthly_salary:
    print("You are eligible for a loan!")
    months_to_pay = int(input("How many months do you want to pay the loan? "))
    interest_rate = 0.10 
    total_amount = loan_amount * (1 + interest_rate)
    print(f"Your total amount to pay is: {total_amount:.2f}")
else:
    if monthly_salary < 30000.00:
        print("You are not eligible for a loan because your monthly salary is too low.")
    else:
        print("You are not eligible for a loan because the loan amount is too high compared to your salary.")