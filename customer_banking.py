# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Enter the savings account balance: "))
    interest_rate = float(input("Enter an interest rate: "))
    months = int(input("Enter months to determine the interest gained: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned of the CD is: {interest_earned}")
    print(f"The updated balance of the saving account is: {savings_balance + interest_earned}")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Enter the balance of the CD account: "))
    interest_rate = float(input("Enter an interest rate of the CD account: "))
    months = int(input("Enter months of the CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    cd_balance, interest_earned = create_cd_account(cd_balance, interest_rate, months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"The interest earned of the CD account is: {interest_earned}")
    print(f"The updated balance of the CD is: {cd_balance + interest_earned }")
if __name__ == "__main__":
    # Call the main function.
    main()