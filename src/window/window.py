import tkinter
import pygame

class Window:
    
    def __init__(self, height: int, width: int, title: str):
        
        self.dimensions = [width, height];
        self.title = title;
        
        self.window = tkinter.Tk();

        self.window.title(self.title);
        self.window.configure(width = self.dimensions[0], height
                              = self.dimensions[1]);
        self.window.attributes("-fullscreen", True);
        
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (w, h))

    
class PygameWindow:
    
    def __init__(self, width: int, height: int, title: str):
        
        self.width = width;
        self.height = height;
        self.title = title;

        pygame.init();

        self.screen = pygame.display.set_mode((self.width, self.height),
                                              pygame.RESIZABLE);

        pygame.display.set_caption(self.title);


        
        pygame.display.update();

    def __del__(self):
        pygame.quit();
