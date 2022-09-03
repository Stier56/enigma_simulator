from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from enigma_gui_component import encryption


class EnigmaScreen(BoxLayout):
    slot1_rotor_number = StringProperty('1')
    slot2_rotor_number = StringProperty('1')
    slot3_rotor_number = StringProperty('1')

    slot1_initial_position = StringProperty('a')
    slot2_initial_position = StringProperty('a')
    slot3_initial_position = StringProperty('a')

    plugboard_list = ListProperty([chr(num) for num in range(97, 123)])

    input_string = StringProperty()
    output_string = StringProperty()
    
    def __init__(self, **kwargs):
        super(EnigmaScreen, self).__init__(**kwargs)

    def change_plugboard(self, index, new_alphabet):
        new_alphabet_index = self.plugboard_list.index(new_alphabet)
        tmp = self.plugboard_list[index]
        self.plugboard_list[index] = new_alphabet
        self.plugboard_list[new_alphabet_index] = tmp

    def run_encryption(self): 
        self.output_string = encryption(self.input_string,
                                        self.slot1_rotor_number, 
                                        self.slot2_rotor_number, 
                                        self.slot3_rotor_number, 
                                        self.slot1_initial_position, 
                                        self.slot2_initial_position, 
                                        self.slot3_initial_position,
                                        self.plugboard_list)

Builder.load_file('./enigma_gui.kv')

class EnigmaApp(App):
    def __init__(self, **kwargs):
        super(EnigmaApp, self).__init__(**kwargs)
        self.title = 'Enigma Simulator'    

    def build(self):
        return EnigmaScreen()


if __name__ == '__main__':
    EnigmaApp().run()