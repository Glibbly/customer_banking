# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from Account import Account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    sab_client = input("Please enter your savings account balance")
    sair_client = input("Please enter your interest rate")
    months_client = input("Please enter your months")

    sab_client = float(sab_client)
    sair_client = float(sair_client)
    months_client = float(months_client)

    # Call the create_savings_account function and pass the variables from the user.
    create_savings_account(sab_client, sair_client, months_client)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Youve earned {sair_client} interest and that was accrued over {months_client}months. You current savings balance is {sab_client}")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input("Please enter your CD balance")
    cd_interest = input("Please enter your interest rate")
    cd_maturity = input("Please enter your months")

    cd_balance = float(cd_balance)
    cd_interest = float(cd_interest)
    cd_maturity = float(cd_maturity)
    # Call the create_cd_account function and pass the variables from the user.
    create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Youve earned {cd_interest} interest and that was accrued over {cd_maturity}months. \n You current savings balance is {cd_balance}")

if __name__ == "__main__":
    main()