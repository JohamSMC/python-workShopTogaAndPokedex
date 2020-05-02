import toga
import requests
from consts import *

class PokeDex(toga.App):
    def __init__(self, title, id):
        toga.App.__init__(self, title, id)

        self.title = title
        self.size = (WIDTH, HEIGTH)

        self.heading = ['Name']
        self.data = list()

        self.create_elements()
        self.load_data()

    def startup(self):
        self.main_window = toga.MainWindow("main", title=self.title, 
                                            size=self.size)

        box = toga.Box()        

        split = toga.SplitContainer()
        split.content = [self.table, box]

        self.main_window.content = split

        self.main_window.show()

    def create_elements(self):
        self.create_table()

    def create_table(self):
        self.table = toga.Table(self.heading, data = self.data,
                                on_select = self.select_element)
    
    def load_data(self):
        path = 'https://pokeapi.co/api/v2/pokemon-form?offset=0&limit=20'
        
        response = requests.get(path)

        if response:
            result = response.json()

            for pokemon in result['results']:
                name = pokemon['name']
                self.data.append(name)

        self.table.data = self.data
#CALLBACKS

    def select_element(self, widget, row):
        if row:
            print(row.name)



if __name__ == "__main__":
    pokedex = PokeDex('PokeDex', 'dev.johamSMC')
    pokedex.main_loop()