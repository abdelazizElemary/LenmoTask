from classes import investor, borrower

annual_rate = 15.0
lenmo_fee = 3.0
months = 12.0
loan_status = False
lenmo_profit = 0


# This function where the borrower request the loan and this increase the requests for the borrower with 1
# As the investor before submitting the offer will check if there is a request from the borrower or not
def loan_request(amount, period, borrower):
    amount = amount
    period = period
    borrower.requests += 1
    return True

# The pay back value for the loan will be calculated
# Then the investor will announce the offer
def submit_offer(amount, period, borrower, investor):
    global months, annual_rate, lenmo_fee
    if borrower.requests > 0:
        borrower.requests -= 1
        interest_rate = (period/months) * annual_rate
        added_amount = (interest_rate/100) * amount
        amount = amount + added_amount
        investor.offers += 1
        return amount
    else:
        return 0.0

# In this function the Investor will transfer the loan to the borrower in his balance
# the investor balance will be checked if it has sufficient values to cover lenmo fees and the loan
# Adding the lenmo fees to the company profit
def check_balance(amount, investor, borrower):
    global lenmo_profit
    if investor.balance >= amount+lenmo_fee and investor.offers > 0:
        investor.offers -= 1
        investor.balance -= 3
        investor.balance -= amount
        borrower.balance += amount
        lenmo_profit += 3
        global loan_status
        loan_status = True
        return True
    else:
        print("\nNo Investors found\n")
        return False

# This function takes the loan added to the interest and calculate each month pays
# according to the determined period
def pay_back_value(amount, period):
    value = amount / period
    return value

# This function implements the addition of the installments of the loan to the
# investor balance
def pay_back_monthly(amount, value, borrower, investor):
    if amount != 0:
        new_amount = amount - value
        investor.balance = investor.balance + value
        return new_amount

# check if the loan funded from the investor or not
def loan_status_funded():
    if loan_status == True:
        print("Loan Funded")

# check if the loan is paid back to the investor completely with the interest rate added
def loan_status_completed(amount):
    if amount <= 0:
        print("PayBack Completed")


if __name__ == '__main__':

    Abdelaziz = investor('Abdelaziz', 6000.0)
    print("Welcome to Lenmo test program\n")

    borrower1 = borrower('Rami', 0, 0)

    i=True
    while i==True:

        loan_amount = input("Enter the loan amount: ")
        period = input("Enter the period to pay the loan back: ")

        # Taking the loan amount and period from the user and increasing the requests number by 1
        loan_request(loan_amount, period, borrower1)

        # Calculating the value of the loan added to the interest rate based on the user inputs
        # And then the offer is announced by the investor
        amount_to_be_paid = submit_offer(loan_amount, period, borrower1, Abdelaziz)

        # The investor's balance is checked to pay the loan and Lenmo fees and transfer the loan to the borrower
        flag = check_balance(loan_amount, Abdelaziz, borrower1)

        if flag == True:
            print("This is the amount to be paid by the borrower => " +
                str(amount_to_be_paid))
            i = False
        else:
            i=True

    
    print("------------------------------------------------------------")
    # check if the loan funded
    loan_status_funded()
    print("------------------------------------------------------------")

    # make sure the loan is taken from the investor balance
    print("\nThis is the Investor balance rightnow => "+ str(Abdelaziz.balance)+"\n")


    # calculating the value of the loan installments that must be paid by the borrower
    shunk = pay_back_value(amount_to_be_paid, period)    

    # loop on the months count for the borrower to pay the loan installments
    for i in range(period):
        password = input("Enter 2 to pay the month payment ")
        if password == 2:
            amount_to_be_paid = pay_back_monthly(
                amount_to_be_paid, shunk, borrower1, Abdelaziz)
    
    
    print("\n------------------------------------------------------------")
    # check if the loan is completely paid back and added to the investor balance
    loan_status_completed(amount_to_be_paid)
    print("------------------------------------------------------------")


    print("\nThis is the Lenmo profit from this operation and the Investor's balance added to it the profit from the operation\n")
    print(lenmo_profit, Abdelaziz.balance)
