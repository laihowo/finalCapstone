'''This program is a finance calculator that can calculate the interest on 
an investment or the amount you'll have to pay on a home loan each month.'''

# Import math library to use the power function
import math

# Display the options to the user
print('investment - to calculate the amount of interest you\'ll earn on your investment')
print('bond       - to calculate the amount you\'ll have to pay on a home loan')

# Get the user's selection
user_selection = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ")
user_selection = user_selection.lower()

# If the user selects 'investment'
if user_selection == 'investment':
    # Get the necessary inputs of
    # deposit, interest rate, number of years investing and type of interest
    deposit = float(input('Enter the amount of money that you are depositing: '))
    interest_rate = float(input('Enter the interest rate (as a percentage): '))
    interest_rate = interest_rate / 100
    years_investing = float(input('Enter the number of years you plan on investing: '))
    interest = input('Do you want "simple" or "compound" interest? ')
    interest = interest.lower()

    # Initialize the amount variable
    amount = 0
    # Calculate the amount based on the type of interest
    if interest == 'simple':
        amount = deposit * (1 + interest_rate * years_investing)
    elif interest == 'compound':
        amount = deposit * math.pow((1 + interest_rate), years_investing)
    # Display the result
    print(f'You will get back ${amount:.2f} after the given period.')

# If the user selects 'bond'
elif user_selection == 'bond':
    # Get the necessary inputs of house value, interest rate and number of months to repay
    house_value = float(input('Enter the present value of the house: '))
    interest_rate = float(input('Enter the interest rate (as a percentage): '))
    interest_rate = interest_rate / 100 / 12
    months_repay = float(input('Enter the number of months you plan to take to repay the bond: '))

    # Calculate the monthly repayment
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months_repay))
    # Display the result
    print(f'You will have to repay ${repayment:.2f} each month.')
