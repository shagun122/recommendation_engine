# Smart ATM Simulator

balance = 1000

def show_menu():
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        deposit = int(input("Enter amount to deposit: "))
        if deposit > 0:
            balance = balance + deposit
            print("₹", deposit, "deposited successfully.")
        else:
            print("Enter a valid amount!")
            

    elif choice == "3":
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= balance and withdraw > 0:
            balance = balance - withdraw
            print("₹", withdraw, "withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount!")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
