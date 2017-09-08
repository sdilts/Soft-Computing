import os.path

class convertData:
    def __init__(self, relation = "",attributes = [],attributeTypes = [],data = "",fileLoc = ""):
        self.relation = relation
        self.attributes = attributes
        self.attributeTypes = attributeTypes
        self.data = data
        self.fileLoc = fileLoc

    def convertToARFF(self):
        fname = self.relation + ".arff"
        fullName = os.path.join(self.fileLoc,fname)
        print("Filepath is: " + fullName)

        file = open(fullName,'w')
        file.write("@RELATION " + self.relation + "\n")
        file.write("\n")

        for i in range(0, len(self.attributes)):
            file.write("@ATTRIBUTE " + self.attributes[i] + " " + self.attributeTypes[i] + "\n")

        file.write("\n" + "@DATA\n" + self.data)