from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import os
import json

taskNumb = 0  # should be recieved from API

file_name = 'projects.json'

file_path = os.path.abspath(os.path.join('.json', file_name))

with open(file_path) as f:
    jdata = json.load(f) # data of json file




class MCListDemo(ttk.Frame):
    # class variable to track direction of column
    # header sort
    SortDir = True  # descending

    def __init__(self, isapp=True, name='mclistdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('List of projects')
        self.isapp = isapp
        self._create_widgets()

    def _create_widgets(self):

        self._create_demo_panel()

    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)

        self._create_treeview(demoPanel)
        self._load_data()

    def _create_treeview(self, parent):
        self.numbLb = Label(self)
        self.numbLb['text'] = 'Number of tasks ' + str(taskNumb)

        f = ttk.Frame(parent)
        f.pack(side=TOP, fill=BOTH, expand=Y)

        # create the tree and scrollbars
        self.dataCols = ('ID', 'Name', 'Deadline', 'Initial Language','Translated language', 'Project Manager')
        self.tree = ttk.Treeview(columns=self.dataCols,
                                 show='headings')

        ysb = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set

        # add label, tree and scrollbars to frame
        self.numbLb.grid(in_=f, row=0, column=0, sticky = W)
        self.tree.grid(in_=f, row=1, column=0, sticky=NSEW)
        ysb.grid(in_=f, row=1, column=1, sticky=NS)
        xsb.grid(in_=f, row=2, column=0, sticky=EW)

        # set frame resize priorities
        f.rowconfigure(0, weight=1)
        f.columnconfigure(0, weight=1)

    def _load_data(self):
        self.data = []
        for x in xrange(0, len(jdata)):
            self.data.append((jdata[x]['id'], jdata[x]['name'], jdata[x]['deadline']['formatted'], jdata[x]['languageCombinations'][0],jdata[x]['languageCombinations'][1], jdata[x]['projectManager']['name'] ))


        # configure column headings
        for c in self.dataCols:
            self.tree.heading(c, text=c.title(),
                              command=lambda c=c: self._column_sort(c, MCListDemo.SortDir))
            self.tree.column(c, width=Font().measure(c.title()))

        # add data to the tree
        for item in self.data:
            self.tree.insert('', 'end', values=item)

            # and adjust column widths if necessary
            for idx, val in enumerate(item):
                iwidth = Font().measure(val)
                if self.tree.column(self.dataCols[idx], 'width') < iwidth:
                    self.tree.column(self.dataCols[idx], width=iwidth)

    def _column_sort(self, col, descending=False):

        # grab values to sort as a list of tuples (column value, column id)
        # e.g. [('Argentina', 'I001'), ('Australia', 'I002'), ('Brazil', 'I003')]
        data = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]

        # reorder data
        # tkinter looks after moving other items in
        # the same row
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.tree.move(item[1], '', indx)  # item[1] = item Identifier

        # reverse sort direction for next sort operation
        MCListDemo.SortDir = not descending


if __name__ == '__main__':
    MCListDemo().mainloop()