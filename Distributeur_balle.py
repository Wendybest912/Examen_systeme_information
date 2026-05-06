from enum import Enum, auto

class GiftBall:
    def __init__(self, numbers_of_balls):
        self.numbers_of_balls = numbers_of_balls
        self.current_state = State.NO_TOKEN

    def insert_token(self):
        if self.current_state == State.NO_TOKEN:
            print("piece inséré !")
            self.current_state = State.ONE_TOKEN 

        elif self.current_state == State.ONE_TOKEN:
            print("piece déjà inséré")

        elif self.current_state == State.SOLD_OUT:
            print("plus de boules")


    def eject_token (self):
        if self.current_state == State.ONE_TOKEN:
            self.current_state = State.NO_TOKEN
            print("piece éjecté")

        elif self.current_state == State.NO_TOKEN :
            print("aucune piece a rétourné ")

        elif self.current_state == State.SOLD_OUT:
            print("plus de boules")

    def turn_crank (self):
        if self.current_state == State.ONE_TOKEN:
            print("manivelle tournéé")
            self.distribution()

        elif self.current_state == State.NO_TOKEN :
            print("aucune piece inséré ")

        elif self.current_state == State.SOLD_OUT:
            print("plus de boules")

    def distribution(self):
        if self.current_state == State.ONE_TOKEN:
            print("Une boule est distribuée ")
            self.numbers_of_balls -= 1

            if self.numbers_of_balls > 0:
                self.current_state = State.NO_TOKEN
            else:
                print("La machine est maintenant vide.")
                self.current_state = State.SOLD_OUT

class State(Enum):
    NO_TOKEN = auto()
    ONE_TOKEN = auto()
    SOLD_OUT = auto()



machine = GiftBall(3)

machine.insert_token()
machine.turn_crank()

machine.insert_token()
machine.eject_token()

machine.insert_token()
machine.turn_crank()
machine.turn_crank()

machine.insert_token()
machine.turn_crank()
machine.insert_token()