from linked_list import LinkedList 
from customer import Customer 
from bank_loan_application import BankLoanApplication 
from loan_transaction import Loan_Transaction
from loan_payment_accountpy import Loan_Payment_Accountpy
from loan_account import LoanAccount
from savings_account import Savings_Account

def Main_Menu():
 print("Main Menu", end="\n\n")
 print("1. Go to Customer menu")
 print("2. Go to Loan manager menu")
 print ("0. Exit")

 choice = input(">>")

 if choice == '1':
  Customer_Menu()
 elif choice == '2':
  Loan_Manager_Menu()
 elif choice =='0':
  return 
  
 def Customer_Menu():
  print("Customer's Menu", end="\n\n")
  print("1. Make a savings account depoist")
  print("2. View savings account balance")
  print("3. Make a loan payment")
  print("4. View loan balance")
  print("0. Go to Main menu")
  
        
  def Loan_Manager_Menu():
   print("Loan Manager Menu", end="\n\n")
   print("1. Manage customer records")
   print("2. Create a loan application")
   print("0. Go to Main menu")
   
def print_menu(): 
    print("Manage Customer Records", end="\n\n") 
    print("1. Add a customer record") 
    print("2. View a customer record") 
    print("3. Update a customer record") 
    print("4. Delete a customer record") 
    print("5. List all customer records") 
    print("6. Count the number of customer records") 
    print("0. Exit the application") 
 
def create_customer_record(): 
    print("Add Customer Record", end="\n\n") 
    last_name = input("Enter last name: ") 
    first_name = input("Enter first name: ") 
    address = input("Address: ") 
    mobile_number = input("Mobile number: ") 
    customer_record = Customer(last_name, first_name, address, mobile_number) 
    return customer_record 
 
def find_customer_record(): 
    name = input("Enter the last name of the record you want to view: ") 
    customer_record = customers.search(name) 
    return customer_record 
 
def delete_customer_record(): 
    name = input("Enter the last name of the record you want to delete: ") 
    deleted = customers.delete(name) 
    return deleted 
 
def print_customer_record(customer): 
    print(f"{customer.first_name} {customer.last_name} (ID#{customer.id}) ") 
    print(f"Address: {customer.address}") 
    print(f"Mobile telephone: {customer.mobile_number}")  
 
def update_customer_record(): 
    customer_record = find_customer_record() 
    if customer_record is not None: 
        my_customer = customer_record.data 
        print_customer_record(my_customer) 
        print("Update the Record:", end="\n\n") 
        new_first_name = input("Enter new first name: ") 
        my_customer.first_name = new_first_name 
        new_last_name = input("Enter new last name: ") 
        my_customer.last_name = new_last_name 
        new_address = input("Enter new address: ") 
        my_customer.address = new_address 
        new_mobile_number = input("Enter new mobile number: ") 
        my_customer.mobile_number = new_mobile_number 
 
# create the linked list 
customers = LinkedList() 
application=BankLoanApplication()
# accept input from the menu 
while True: 
    try: 
        print_menu() 
        menu_option = input(">>") 
        match menu_option: 
            case '1': 
                my_customer = create_customer_record() 
                customers.insert(my_customer) 
            case '2': 
                my_customer = find_customer_record() 
                if my_customer is not None: 
                    print_customer_record(my_customer.data) 
            case '3': 
                update_customer_record() 
            case '4': 
                if delete_customer_record(): 
                    print("Customer record deleted!")  
            case '5': 
                print(customers) 
            case '6': 
                print(f"Number of customers = {customers.length()}") 
            case '0':  
                break 
        input("Press Enter key to continue...") 
    except: 
        print("Invalid input. Please try again.")
