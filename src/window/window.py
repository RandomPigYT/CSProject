import tkinter

class Window:
    
    def __init__(self, height: int, width: int, title: str):
        
        self.dimensions = [width, height];
        self.title = title;
        
        self.window = tkinter.Tk();

        self.window.title(self.title)
        self.window.configure(width = self.dimensions[0], height
                              = self.dimensions[1]);
        
        self.window.mainloop();

