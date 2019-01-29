import os
import shutil
import re
from datetime import datetime

class PO:


    def getActivePO(self, cwd):

        listactivepo = []

        for filename in os.listdir(cwd):
            if filename.startswith("PO") and filename.endswith(".txt"):
                    listactivepo.append(filename)

        return listactivepo


    def processPO(self, cwd, amount):
        # To process existing PO's, we need to identify them, update workbook with contained info, and
        # move to processed PO folder (with name change "PO_2_19012019 to out_PO_2_19012019.txt"
        if amount == "ALL":
            for filename in os.listdir(cwd):
                if filename.startswith("PO") and filename.endswith(".txt"):
                    print("Running...")

                    old_file_loc = os.path.join(cwd, filename)
                    new_file_loc = os.path.join(cwd + "\processed_PO", filename)
                    new_file_name = os.path.join(cwd + "\processed_PO", "out_" + filename)

                    shutil.move(old_file_loc, new_file_loc)
                    os.rename(new_file_loc, new_file_name)
        else:
            for id in amount:
                for filename in os.listdir(cwd):
                    if filename.startswith("PO") and filename.endswith(".txt"):  # and filename[3] == str(id):
                        splitting = re.split(r"_", filename)
                        if splitting[1] == id:
                            print("Processing Purchase Order: " + str(id) + "...")

                            old_file_loc = os.path.join(cwd, filename)
                            new_file_loc = os.path.join(cwd + "\processed_PO", filename)
                            new_file_name = os.path.join(cwd + "\processed_PO", "out_" + filename)

                            shutil.move(old_file_loc, new_file_loc)
                            os.rename(new_file_loc, new_file_name)



    def genPO(self, cwd):

        # To generate a Purchase Order, you need to know:
        # Vendors available
        # Item Names available
        # Balance available

        prev_po_id = 0

        for filename in os.listdir(cwd):
            if filename.startswith("PO") and filename.endswith(".txt"):
                splitting = re.split(r"_", filename)
                if int(splitting[1]) > prev_po_id:
                    prev_po_id = int(splitting[1])

        for filename in os.listdir(cwd + "\processed_PO"):
            if filename.startswith("out_PO") and filename.endswith(".txt"):
                splitting = re.split(r"_", filename)
                if int(splitting[2]) > prev_po_id:
                    prev_po_id = int(splitting[2])

        new_po_id = prev_po_id + 1
        # return new_po_id

        new_po = open("PO_{}_{}.txt".format(new_po_id, datetime.today().strftime("%d%m%Y")), "w+")
        new_po.write("PO\n")
        sup_name = input("Supplier Name: ")
        new_po.write("Supplier: %s\n"% sup_name)
        while input("Enter new item and quantity: [Y/N] ") != "N":
            item_name = input("Item Name: ")
            new_po.write("Item: %s\n" % item_name)
            qty = input("Item Quantity: ")
            new_po.write("Quantity: %s\n" % qty)

        new_po.close()
        return new_po_id
