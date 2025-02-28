import arcade 
import arcade.csscolor
import arcade.gui
from particle import Particle
import tkinter as tk 
import time

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

        self.simulate_button = arcade.gui.UIFlatButton(x=WINDOW_WIDTH - 75, y=WINDOW_HEIGHT -75, width=50, height=50)
        self.manager.add(self.simulate_button)

        # assign functions to the buttons
        self.reveal_button.on_click = self.on_click_reveal
        self.simulate_button.on_click = self.start_simulation

        # holds the id of most recently selcted selectable item to be added to simulation 
        self.currently_selected = None 

        self.simulation = False

        self.particle_list = [] 


        pass

    def reset(self):

        pass


    def on_click_reveal(self, event):
        ''' menu for selectable items revealed '''



        self.manager.remove(self.reveal_button)

        # testing if select menu has been created before 
        try:
            self.select_anchor_layout == None
        except AttributeError:
            # does not exist so is created here 

            # box containing the selectable options for the simualtor 
            self.select_box = arcade.gui.widgets.UIBoxLayout(space_between = 20)

            particle_button = arcade.gui.widgets.UIFlatButton(text='particle', width=150)
            self.select_box.add(particle_button)
            return_button = arcade.gui.widgets.UIFlatButton(text='return', width=150)
            self.select_box.add(return_button)

            particle_button.on_click = self.on_click_particle
            return_button.on_click = self.on_click_return

            # create widget to hold the select box
            self.select_anchor_layout = arcade.gui.UIAnchorWidget(child=self.select_box, anchor_x='left', anchor_y='top',
                                                                  align_y=-25, size_hint_min=100)
            self.select_anchor_border = arcade.gui.UIBorder(child=self.select_anchor_layout)

        self.manager.add(self.select_anchor_border)
        self.manager.add(self.select_anchor_layout)


    def on_click_particle(self, event): 
        self.currently_selected = 'particle'

    def on_click_return(self, event):
        self.manager.remove(self.select_anchor_border)
        self.manager.remove(self.select_anchor_layout)
        self.manager.add(self.reveal_button)


    def on_mouse_press(self, x, y, button, key_modifiers):
        
        if self.currently_selected == 'particle':
            
            p = Particle(x, y, WINDOW_WIDTH, WINDOW_HEIGHT)
            self.particle_list.append(p)

            self.on_draw()




    def on_key_press(self, symbol, modifiers):
        pass


    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.BLACK)

    def on_draw(self):

        self.clear()
        self.manager.draw()
        for particle in self.particle_list:
            particle.draw()


    def on_update(self, delta_time=1):

        if self.simulation is True:
            for particle in self.particle_list:
                particle.move()


    def start_simulation(self, event): 
        self.simulation = True




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