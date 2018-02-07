from Tkinter import *

import os
import json



file_name = 'projects.json'

file_path = os.path.abspath(os.path.join('.json', file_name))

with open(file_path) as f:
    data = json.load(f) # data of json file


#data[0]['id']
#data[0]['name']

#data[0]['deadline']['formatted']

#data[0]['actualDeliveryDate']['formatted']

#data[0]['projectManager']['name']

#print json.dumps(data,indent=4)

print len(data)


class Application(Frame):

    def __init__(self, master =  None):
        Frame.__init__(self, master)
        self.pack()
        self.create_Window()

    def create_Window(self):
        bottomFrame = Frame(root)
        self.listLb = Label(self)
        self.listLb['text'] = "List of tasks"
        self.listLb.pack(side = TOP)

        self.idLb = Label(self)
        self.idLb['text'] = "ID"
        self.idLb.pack(side = LEFT)

        self.nameLb = Label(self)
        self.nameLb['text'] = "Name"
        self.nameLb.pack(side=LEFT)

        self.deadlineLb = Label(self)
        self.deadlineLb['text'] = "Deadline"
        self.deadlineLb.pack(side=LEFT)

        self.deliverLb = Label(self)
        self.deliverLb['text'] = "Delivery"
        self.deliverLb.pack(side=LEFT)

        self.managerLb = Label(self)
        self.managerLb['text'] = "Project Manager"
        self.managerLb.pack(side=LEFT)

        self.lb = Listbox(root)


        for x in xrange(0, len(data)):
            print (x,data[x]['id'], data[x]['name'], data[x]['deadline']['formatted'], data[x]['actualDeliveryDate']['formatted'], data[x]['projectManager']['name'] )
            self.lb.insert(data[x]['id'], data[x]['name'], data[x]['deadline']['formatted'], data[x]['actualDeliveryDate']['formatted'], data[x]['projectManager']['name'] )
            self.lb['width'] = 100
        self.lb.pack()


        self.dataCols = ('ID', 'Name', 'Deadline', 'Delivery', 'ProjectManager')
        self.tree = treeview(columns = self.dataCols, show = 'headings')




root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()