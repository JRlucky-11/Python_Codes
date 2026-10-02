class Myhome:
    def __init__(self, room_name, is_on = False):
        self.room_name = room_name
        self.is_on = is_on
    def turn_on(self):
        self.is_on = True
        print("Room Light is On.")
    def turn_off(self):
        self.is_on = False
        print("Room Light is Off.")

myroom = Myhome(room_name= "lvroom")
myroom.turn_on()
myroom.turn_off()