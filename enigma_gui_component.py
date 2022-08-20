class scrambler:
    def __init__(self, scrambler_number):
        if scrambler_number == 1: 
            self.wiring_R = [10, 21, 5, 20, 7, 2, 23, 18, 1, 11, 3, 0, 6, 24, 25, 16, 14, 17, 13, 22, 4, 15, 8, 12, 19, 9]
            self.wiring_L = [24, 8, 7, 6, 21, 18, 9, 22, 3, 11, 2, 23, 12, 0, 4, 16, 14, 20, 17, 15, 19, 25, 5, 13, 10, 1]
        elif scrambler_number == 2:
            self.wiring_R = [7, 6, 22, 2, 0, 20, 8, 15, 10, 5, 24, 9, 1, 21, 13, 19, 16, 18, 3, 14, 12, 23, 11, 4, 25, 17]
            self.wiring_L = [5, 10, 11, 13, 3, 21, 19, 1, 6, 15, 9, 18, 8, 4, 24, 7, 17, 12, 20, 14, 23, 0, 25, 22, 2, 16]
        elif scrambler_number == 3:
            self.wiring_R = [5, 15, 1, 6, 19, 22, 3, 16, 10, 21, 2, 25, 18, 0, 8, 13, 17, 11, 12, 4, 20, 9, 24, 23, 14, 7]
            self.wiring_L = [14, 24, 15, 4, 10, 21, 22, 20, 5, 13, 7, 8, 17, 9, 12, 16, 25, 6, 19, 0, 2, 11, 1, 23, 3, 18]
        elif scrambler_number == 4:
            self.wiring_R = [22, 12, 5, 17, 0, 24, 11, 19, 8, 6, 9, 4, 14, 20, 10, 23, 16, 18, 25, 7, 15, 3, 1, 2, 21, 13]
            self.wiring_L = [23, 7, 18, 5, 3, 21, 6, 13, 22, 14, 1, 24, 20, 0, 17, 8, 10, 25, 19, 11, 12, 4, 2, 16, 9, 15]
        else:
            self.wiring_R = [20, 24, 0, 3, 16, 10, 11, 15, 8, 7, 12, 5, 6, 1, 18, 4, 2, 17, 25, 21, 9, 13, 23, 19, 22, 14]
            self.wiring_L = [25, 14, 8, 22, 13, 20, 6, 15, 23, 10, 3, 21, 4, 2, 5, 1 ,17, 18, 0, 11, 9, 16, 24, 12, 19, 7]

    # Set the initial position of the scrambler
    def set_scrambler_position(self, scrambler_position):
        self.scrambler_position = scrambler_position

        tmp_R = self.wiring_R[0:self.scrambler_position]
        self.wiring_R[0:26 - self.scrambler_position] = self.wiring_R[self.scrambler_position:26]
        self.wiring_R[26 - self.scrambler_position:26] = tmp_R

        tmp_L = self.wiring_L[0:self.scrambler_position]
        self.wiring_L[0:26 - self.scrambler_position] = self.wiring_L[self.scrambler_position:26]
        self.wiring_L[26 - self.scrambler_position:26] = tmp_L


    def scrambler_rotation(self):
        self.scrambler_position = (self.scrambler_position + 1) % 26
        tmp_R = self.wiring_R[0]
        self.wiring_R[0:25] = self.wiring_R[1:26]
        self.wiring_R[25] = tmp_R
        tmp_L = self.wiring_L[0]
        self.wiring_L[0:25] = self.wiring_L[1:26]
        self.wiring_L[25] = tmp_L

    # output from right to left
    def output_RtoL(self, input):
        index = self.wiring_L.index(self.wiring_R[input])
        return index
    # output from left to right
    def output_LtoR(self, input):
        index = self.wiring_R.index(self.wiring_L[input])
        return index

class plugbord:
    def __init__(self, new_list):
        self.char_list = new_list

    def input(self, input_char):
        index = self.char_list.index(input_char)
        return index

    def output(self, output_index):
        char = self.char_list[output_index]
        return char

def reflector(input):
    wiring = [8, 13, 10, 17, 20, 6, 5, 19, 0, 12, 2, 15, 9, 1, 21, 11, 23, 3, 22, 7, 4, 14, 18, 16, 25, 24]
    output = wiring[input]

    return int(output)

# Check input string. Allow lowercase letters only.
def input_string_check(input_char):
    if ord(input_char) < 97 or ord(input_char) > 122:
        output_char = ' '
    else:
        output_char = input_char

    return output_char

def encryption(input_string, slot1_number, slot2_number, slot3_number, slot1_position, slot2_position, slot3_position, plugboard_list):
    # Set scrambler for each slot
    scrambler1 = scrambler(int(slot1_number))
    scrambler2 = scrambler(int(slot2_number))
    scrambler3 = scrambler(int(slot3_number))

    # Set the initial position of the scrambler
    scrambler1.set_scrambler_position(ord(slot1_position) - 97)
    scrambler2.set_scrambler_position(ord(slot2_position) - 97)
    scrambler3.set_scrambler_position(ord(slot3_position) - 97)

    # Create an instance of the plugboard
    using_plugbord = plugbord(plugboard_list)

    scrambler1_count = 0
    scrambler2_count = 0

    input_string_list = list(input_string)
    output = []
    for input_char in input_string_list:
        input_char = input_string_check(input_char)
        if input_char == ' ':
            output.append(' ')
            continue

        input_char_index = using_plugbord.input(input_char)

        out = scrambler1.output_RtoL(input_char_index)
        out = (out + (scrambler2.scrambler_position - scrambler1.scrambler_position)) % 26

        out = scrambler2.output_RtoL(out)
        out = (out + (scrambler3.scrambler_position - scrambler2.scrambler_position)) % 26

        out = scrambler3.output_RtoL(out)
        out = reflector(out)


        out = scrambler3.output_LtoR(out)
        out = (out + (scrambler2.scrambler_position - scrambler3.scrambler_position)) % 26
        if scrambler2_count == 26:
            scrambler3.scrambler_rotation()
            scrambler2_count = 1

        out = scrambler2.output_LtoR(out)
        out = (out + (scrambler1.scrambler_position - scrambler2.scrambler_position)) % 26    
        if scrambler1_count == 26:
            scrambler2.scrambler_rotation()
            scrambler1_count = 1
            scrambler2_count = scrambler2_count + 1

        out = scrambler1.output_LtoR(out)
        scrambler1.scrambler_rotation()
        scrambler1_count = scrambler1_count + 1

        output.append(using_plugbord.output(out))

    output_string = "".join(output)
    return output_string




