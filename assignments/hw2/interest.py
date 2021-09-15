
"""
Name: <Madison Byrne>
<interest>.py

Problem: calculate the value of an investment after 10 years

Certification of Authenticity:
I certify that this assignment is entirely my own work, but had help with Professor Baier.
"""
def main():
    interest_rate = eval(input("Enter a value for the annual interest rate:"))
    billing_cycle = eval(input("Enter a value for the number in the billing cycle:"))
    net_balance = eval(input("Enter a value for the previous net balance:"))
    payment = eval(input("Enter a value for the payment made on the billing day:"))
    billing_day = eval(input("Enter a value for the day the payment was made:"))
    step_1 = (net_balance * billing_cycle)
    step_2 = (payment * (billing_cycle - billing_day))
    step_3 = (step_1-step_2)
    average_daily_balance = (step_3/ billing_cycle)
    monthly_interest_rate = (interest_rate/12)/100
    interest_charge = average_daily_balance * monthly_interest_rate
    print(round(interest_charge, 2))

#'rate': 15.84, 'days': 31.0, 'previous_balance': 850.0, 'payment': 400.0, 'payment_day': 20.0

if __name__ == "__main__":

    main()
