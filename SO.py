import os


class SO:


    def getActiveSO(self, cwd):

        listactiveso = []

        for filename in os.listdir(cwd):
            if filename.startswith("SO") and filename.endswith(".txt"):
                    listactiveso.append(filename)

        return listactiveso
