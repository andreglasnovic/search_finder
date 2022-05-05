import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont


class GridOptions(tk.Tk):
    # Controls the generation of other frames(windows)
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(False, False)
        self.title("Algorith Explorer")
        self.title_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

        # Centers the tkinter window
        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry("+%d+%d" % (x, y))

        # storing the user inputs in dictionary 
        
        self.shared_data = {
            "Grid_size": tk.StringVar(),
            "Search_Algorithm": tk.StringVar(),
            "Start_row": tk.IntVar(),
            "Start_column": tk.IntVar(),
            "Goal_Row": tk.IntVar(),
            "Goal_column": tk.IntVar(),
        }
        
        main_frame = tk.Frame(self)
        main_frame.grid(column=0, row=0)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        
        self.frames = {}
        for F in (SizePage, SGPage, ConfirmPage):
            pg_name = F.__name__
            frame = F(parent=main_frame, controller=self)
            self.frames[pg_name] = frame
            frame.grid(column=0, row=0, sticky="nsew")

        
        self.show_frame("SizePage")

    def show_frame(self, pg_name):
        
        frame = self.frames[pg_name]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

    def quit_win(self):
       
        self.destroy()

    def get_size(self):
        """Returns size stored in shared_data dic"""
        return self.shared_data["Grid_size"].get()


class SizePage(ttk.Frame):
    def __init__(self, parent, controller):
        #  Search_Algorithm and size is hold by this frame 
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        title = ttk.Label(
            self, text="Search Options", font=controller.title_font, anchor="center"
        )
        size_label = ttk.Label(self, text="Select a size for the grid: ")
        size_box = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.shared_data["Grid_size"],
            values=("Small", "Medium", "Large"),
        )
        size_box.current(0)
        alg_label = ttk.Label(self, text="Select a search Search_Algorithm: ")
        alg_box = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.shared_data["Search_Algorithm"],
            values=("BFS", "DFS", "A-Star"),
        )
        alg_box.current(0)
        size_qbtn = ttk.Button(self, text="Quit", command=lambda: controller.quit_win())
        size_nextbtn = ttk.Button(
            self, text="Next", command=lambda: controller.show_frame("SGPage")
        )
        title.grid(column=0, row=0, columnspan=2)
        size_label.grid(column=0, row=1, sticky=("nw"))
        size_box.grid(column=1, row=1, sticky=("nw"))
        alg_label.grid(column=0, row=2)
        alg_box.grid(column=1, row=2)
        size_qbtn.grid(column=0, row=3, pady=10)
        size_nextbtn.grid(column=1, row=3, pady=10)


class SGPage(ttk.Frame):
    def __init__(self, parent, controller):
        # This frame holds goal and start indices
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        startLabel = ttk.Label(self, text="Select a start location, (row, column): ")
        goalLabel = ttk.Label(self, text="Select a goal location, (row, column): ")

        # Class members so on_show_frame function can set available values after class has been instantiated
        self.start_row = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.shared_data["Start_row"],
            width="5",
        )
        self.start_col = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.shared_data["Start_column"],
            width="5",
        )
        self.goal_row = ttk.Combobox(
            self,
            state="readonly",
            textvariable=self.controller.shared_data["Goal_Row"],
            width="5",
        )
        self.goal_col = ttk.Combobox(
            self,
            state="readyonly",
            textvariable=self.controller.shared_data["Goal_column"],
            width="5",
        )

        sg_backbtn = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame("SizePage")
        )
        sg_nextbtn = ttk.Button(
            self, text="Next", command=lambda: controller.show_frame("ConfirmPage")
        )
        startLabel.grid(column=0, row=0, sticky=("nw"))
        goalLabel.grid(column=0, row=1, sticky=("nw"))
        self.start_row.grid(column=1, row=0)
        self.start_col.grid(column=2, row=0)
        self.goal_row.grid(column=1, row=1)
        self.goal_col.grid(column=2, row=1)
        sg_backbtn.grid(column=0, row=3, pady=30)
        sg_nextbtn.grid(column=1, row=3, pady=30)

    def on_show_frame(self, event):

        dimensions = []
        size_selection = self.controller.shared_data["Grid_size"].get()
        if size_selection == "Small":
            dimensions = [i for i in range(10)]
        elif size_selection == "Medium":
            dimensions = [i for i in range(25)]
        elif size_selection == "Large":
            dimensions = [i for i in range(40)]

        self.start_col["values"] = dimensions
        self.start_row["values"] = dimensions
        self.goal_col["values"] = dimensions
        self.goal_row["values"] = dimensions
        self.goal_col.current(len(dimensions) - 1)
        self.goal_row.current(len(dimensions) - 1)


class ConfirmPage(ttk.Frame):
    # this frame displays the final grid after selecting start 
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        confirmLabel = ttk.Label(
            self,
            text="""
            Confirm to start the Grid and 
            create obstricles using mouse. 
            Press spacebar to start selected Search Algorithm""",
            anchor="center",
        )
        confirm_frame_startbtn = ttk.Button(
            self, text="Start", command=lambda: controller.quit_win()
        )
        confirm_frame_backbtn = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame("SGPage")
        )
        confirmLabel.grid(column=0, row=0, columnspan=3, rowspan=2)
        confirm_frame_backbtn.grid(column=0, row=2)
        confirm_frame_startbtn.grid(column=1, row=2)

