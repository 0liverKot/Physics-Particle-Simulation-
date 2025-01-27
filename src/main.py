import arcade 
import arcade.gui
from particle import Particle
import tkinter as tk 

WINDOW_TITLE = 'Physics Simulation'

root = tk.Tk()
WINDOW_HEIGHT = root.winfo_screenheight()
WINDOW_WIDTH = root.winfo_screenwidth()



class MyWindow(arcade.View):

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.BLACK
        self.window.set_fullscreen()
        
        # initialising UI manager and enabling
        self.manager = arcade.gui.UIManager()
        self.manager.enable()


        self.menu_button = arcade.gui.UIFlatButton(x=25, y=WINDOW_HEIGHT - 75, width=50, height=50, text='=')
        self.manager.add(self.menu_button)

        particle_list = [] 


        pass

    def reset(self):

        pass
\
    def on_draw(self):

        self.clear()

        arcade.start_render()
        self.manager.draw()
        pass



def main():
    
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    simulation = MyWindow()

    window.show_view(simulation)

    arcade.run()




if __name__ == '__main__':
    main()