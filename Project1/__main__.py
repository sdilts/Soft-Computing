from tkinter import *
import urllib3
import Converter


class buildGUI(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.attributeList = []
        self.attributeDataType = []
        self.data = ""

        self.init_gui()

    def init_gui(self):
        self.master.title('Convert UCI to ARFF')
        self.pack(fill=BOTH, expand=1)

        #Create entry for source URL
        sourceLabel = Label(self, text="UCI source URL")
        sourceLabel.grid(row=0, column=0)

        self.sourceURL = Entry(self)
        self.sourceURL.grid(row=0, column=1)

        #Create entry for location to save converted file
        saveLabel = Label(self, text="Location to save ARFF File")
        saveLabel.grid(row=1, column=0)

        self.fileLoc = Entry(self)
        self.fileLoc.grid(row=1, column=1)

        #Create button to add an attribute to a list
        attributeButton = Button(self,text = "Add Attribute", command = self.saveAttribute)
        attributeButton.grid(row=3,column=0)

        #Entry for name of attribute
        self.attributeEntry = Entry(self)
        self.attributeEntry.grid(row=3,column=1)

        attributeName = Label(self,text="Attribute Name")
        attributeName.grid(row=2,column=1)

        #Entry for type of attribute
        self.attributeType = Entry(self)
        self.attributeType.grid(row=3,column=2)

        attributeLabel = Label(self,text="Attribute Data Type")
        attributeLabel.grid(row=2,column=2)

        #Entry for data set title
        self.titleEntry = Entry(self)
        self.titleEntry.grid(row=6,column=1)

        titleLabel = Label(self,text = "Data Set Title")
        titleLabel.grid(row=6,column=0)

        #Button to start the file conversion
        convertButton = Button(self, text="Convert", command=self.convertAction)
        convertButton.grid(row=7, column=1)

    def convertAction(self):
        url = self.sourceURL.get()

        http = urllib3.PoolManager()
        response = http.request('GET',url)
        data = response.data.decode("utf-8")

        dataHandler = Converter.convertData(self.titleEntry.get(), self.attributeList, self.attributeDataType, data, self.fileLoc.get())
        dataHandler.convertToARFF()

        exit()

    def saveAttribute(self):
        self.attributeList.append(self.attributeEntry.get())
        self.attributeDataType.append(self.attributeType.get())

        self.attributeEntry.delete(0,END)
        self.attributeType.delete(0,END)

        print(self.attributeList)
        print(self.attributeDataType)

if __name__ == '__main__':
    root = Tk()
    app = buildGUI(root)
    root.mainloop()