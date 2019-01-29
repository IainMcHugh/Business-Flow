from SO import SO
from PO import PO
from Records import Records
import os
import time

cwd = os.getcwd()
PO_class = PO()
SO_class = SO()
allPO = "ALL"
Records_class = Records()


def spaces():
    time.sleep(1)
    print("\n")


def restart():
    print("\n")
    re = menu()
    re.mainmenu()


def records_menu():

    spaces()
    print("1. Inventory\n2. Vendors\n3. Customers\n4. Accounts\n5. Back\n")
    user_input = input("Enter number: ")

    if user_input == "1":

        Inventory_submenu()

    if user_input == "2":

        Vendors_submenu()

    if user_input == "3":

        Customers_submenu()

    if user_input == "4":

        Accounts_submenu()

    if user_input == "5":

        restart()


def Inventory_submenu():

    print("1. Display all Inventory\n2. Search Inventory\n3. Amend Inventory\n4. Back")
    user_input = input("Enter number: ")

    if user_input == "1":
        displayAllInventory_subsubmenu()

    if user_input == "2":
        SearchInventory_subsubmenu()

    if user_input == "3":
        AmendInventory_subsubmenu()

    if user_input == "4":
        records_menu()


def displayAllInventory_subsubmenu():
    retrieve = Records_class.get_inventory()
    Records_class.display_inventory(retrieve)
    Inventory_submenu()


def SearchInventory_subsubmenu():
    retrieve = Records_class.get_inventory()
    Records_class.search_inventory(retrieve)
    Inventory_submenu()


def AmendInventory_subsubmenu():
    retrieve = Records_class.get_inventory()
    Records_class.ammend_inventory(retrieve)
    Inventory_submenu()


def Vendors_submenu():
    Records_class.vendors()


def Customers_submenu():
    Records_class.customers()


def Accounts_submenu():
    Records_class.accounts()


def OutstandingPO_menu():
    spaces()
    po_list = PO_class.getActivePO(cwd)

    print("Current available Purchase orders to Process:\n")

    for count, po in enumerate(po_list, 1):
        print(str(count) + ". ", po)

    time.sleep(1)

    choice = input("Do you wish to process some or all existing Purchase Orders? [Y/N/SOME]")

    if choice == "Y":
        PO_class.processPO(cwd, allPO)
        print("Process Complete: Files moved to processed PO folder")
        restart()

    elif choice == "SOME":
        choice2 = input("Enter Purchase Order ID numbers to process. [Comma separated with no spaces]")
        choice_list = choice2.split(",")
        PO_class.processPO(cwd, choice_list)
        restart()

    else:
        print("Cancelled, back to main menu")
        restart()


def GenPO_menu():
    spaces()
    po_id = PO_class.genPO(cwd)
    print("Purchase Order ID: " + str(po_id) + " created")
    spaces()
    restart()


def OutstandingSO_menu():
    spaces()
    so_list = SO_class.getActiveSO(cwd)

    print("Current available Sales orders to Process:\n")
    for count, so in enumerate(so_list, 1):
        print(str(count) + ". ", so)


# Plan of action for tomorrow:
# Work out amend records, using 'xlwt'
# search records, what about less than/equals than/contains ?
# Further on:
# Need to work out how to link checks between POs/SOs and Records

class menu:

    print("Retailers Ltd \nMain Menu \n\nCHOOSE AN OPTION BY ENTERING LINE NUMBER\n")

    def mainmenu(self):
        print("1. Records\n2. Outstanding Purchase Orders\n3. Generate Purchase Order\n4. Outstanding Sales Orders\n5."
              " Quit")

        user_input = input("Enter: ")

        if user_input == "1":
            records_menu()

        if user_input == "2":
            OutstandingPO_menu()

        if user_input == "3":
            GenPO_menu()

        if user_input == "4":
            OutstandingSO_menu()

        if user_input == "5":
            print("Closing Application")


setup = menu()
print("This is a GitHub test")
setup.mainmenu()
