# Business-Flow

The purpose of this project is to simulate a simplfied business workflow process.

There are three main areas:

<b>Records</b>: This is where the businesses information is being stored (in an excel workbook). There are four worksheets, which include the
         Inventory, Vendors, Customers, and Accounts. With Inventory, there are multiple options available, the first action taken is to
         retreive the current Inventory. This is done by creating a dictionary where the keys are the worksheet headings and a subsequent
         list is created with each value being mapped to the appropriate key. From here there is an option to "Display all Inventory".
         This will print the entire Inventory in an ordered fashion. There is also an option to "Search Inventory". Here the user can
         search using a 'Where:is:' method, meaning any heading can be searched for any value. This search takes into account number types
         and will return every matching row. There is also an option to "Ammend Inventory". This involves inputting the ID number to ammend
         which will return the row to the user, and then the user specifies the heading and new value. This then updates the excel sheet
         with the new value, again takign into account the data type.
         
        
<b>Purchase Orders</b>: Purchase orders can be generated and processed. With generating, the user can enter the Vendor name along with item
         information for the PO. The PO is then created as a .txt file, where the PO id is an increment on the most recent PO. There
         is also an option to process all or some PO's. Processing a PO results in it's name being updated and it being added to the
         "processed_PO" folder.
         
        
<b>Sales Order</b>: Similarly to Purchase orders, SO's can be generated. When generating, the user can enter the Customer name along with
        item information for the SO. The SO is then created as a .txt file, where the SO id is an increment on the most recent SO.
        
This entire workflow is run through the terminal, with a menu system. For every menu entered, there is an option to return to the previous
menu.
