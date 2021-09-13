"""
Name: <Madison Byrne>
<interest>.py

Problem: calculate the value of an investment after 10 years

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""
def main():
    rate =eval(input("Enter a value for the interest rate:"))
    days = eval(input("Enter a value for the amount of days in the billing cycle:"))
    principle = eval(input("Enter a value for the previous net balance:"))
    payment = eval(input("Enter a value for the payment amount:"))
    billing_day = eval(input("Enter a value for the day the payment was made:"))
    step_1 =(principle * days)
    step_2 =(payment * 11)
    step_3 = (step_2 - step_1)
    step_4 =(step_3/ billing_day)
    print (step_4*(rate/12))


if __name__ == '__main__':
    main()
