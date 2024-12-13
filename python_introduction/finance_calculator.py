monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_interest_rate = 0.05
current_savings = 0
print(f"\nYour monthly savings are: ${monthly_savings:.2f}\n")
print("Projected savings over 10 years with 5% annual interest:\n")
for year in range(1, 11):
    current_savings += monthly_savings * 12
    current_savings += current_savings * annual_interest_rate
    print(f"Year {year}: ${current_savings:.2f}")