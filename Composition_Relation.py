class Engine:
    def start(self):
        print("Engine Strated")     # Has a relation... Composition
class car:
    def __init__(self):
        self.Engine = Engine()
    def start(self):
        self.Engine.start()

car1 = car()
car1.start()