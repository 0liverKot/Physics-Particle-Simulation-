import arcade 
import arcade.csscolor
import arcade.csscolor
import arcade.gui
from particle import Particle
import tkinter as tk 

WINDOW_TITLE = 'Physics Simulation'

root = tk.Tk()
WINDOW_HEIGHT = root.winfo_screenheight()
WINDOW_WIDTH = root.winfo_screenwidth()



class SimulationWindow(arcade.View):

    def __init__(self):
        super().__init__()

        
        # initialising UI manager and enabling
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # creating button and adding to window 
        self.reveal_button = arcade.gui.UIFlatButton(x=25, y=WINDOW_HEIGHT - 75, width=50, height=50, text='=')
        self.manager.add(self.reveal_button)

        # assign on_click_menu function to the button
        self.reveal_button.on_click = self.on_click_reveal

        # holds the id of most recently selcted selectable item to be added to simulation 
        currently_selected = None 

        particle_list = [] 


        pass

    def reset(self):

        pass


    def on_click_reveal(self, event):
        ''' menu for selectable items revealed '''

        print(event)

        self.manager.remove(self.reveal_button)

        # testing if select menu has been created before 
        try:
            self.select_anchor_layout == None
        except AttributeError:
            # does not exist so is created here 

            # box containing the selectable options for the simualtor 
            self.select_box = arcade.gui.widgets.UIBoxLayout(space_between = 20)

            particle_button = arcade.gui.widgets.UIFlatButton(text='particle')
            self.select_box.add(particle_button)
            return_button = arcade.gui.widgets.UIFlatButton(text='return')
            self.select_box.add(return_button)

            particle_button.on_click = self.on_click_particle
            return_button.on_click = self.on_click_return

            # create widget to hold the select box
            self.select_anchor_layout = arcade.gui.UIAnchorWidget(child=self.select_box, anchor_x='left', anchor_y='top', align_x=25, align_y=-25)
            self.select_anchor_layout.add(child=self.select_box)


        self.manager.add(self.select_anchor_layout)


    def on_click_particle(self, event): 
        currently_selected = 'particle'

    def on_click_return(self, event):
        self.manager.remove(self.select_anchor_layout)
        self.manager.add(self.reveal_button)

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):

        self.clear()

        arcade.start_render()
        self.manager.draw()
        pass


class MenuView(arcade.View):

    def on_show_view(self): 
        arcade.set_background_color(arcade.csscolor.AQUA)

    def on_draw(self):
        self.clear()
        arcade.draw_text('Main Menu', WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, font_size = 50, anchor_x = 'center')
        arcade.draw_text('Click To Advance', WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 75, font_size = 25, anchor_x = 'center')

    def on_mouse_press(self, x, y, button, modifiers):
        simulation_window = SimulationWindow()
        self.window.show_view(simulation_window)


def main():
    
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()




if __name__ == '__main__':
    main()