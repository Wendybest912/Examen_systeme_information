from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def insert_token(self, machine):
        pass

    @abstractmethod
    def eject_token (self, machine):
        pass

    @abstractmethod
    def turn_crank (self, machine):
        pass

    @abstractmethod
    def distribution(self, machine):
        pass


class NO_TOKEN(State):
    def insert_token(self, machine ):
        print("Pièce insérée !")
        machine.set_state(machine.one_token_state)


    def eject_token (self, machine):
        print("aucune pièce a retiré")

    def turn_crank (self, machine):
        print("veuillez inseré une pièce")

    def distribution(self, machine):
        print("veuillez inseré une pièce")

class ONE_TOKEN(State):
    def insert_token(self, machine ):
        print("Pièce deja insérée !")

    def eject_token (self, machine):
        print("pièce retiré")
        machine.set_state(machine.no_token_state)

    def turn_crank (self, machine):
        print("manivelle tourné")
        machine.current_state.distribution(machine)

    def distribution(self, machine):
        if machine.numbers_of_balls > 0:
            machine.numbers_of_balls -= 1
            print("boule distribué")
        else:
            print("machine vide")
            machine.set_state(machine.sold_out_state)

class SOLD_OUT(State):
    def insert_token(self, machine ):
        print("machine vide")

    def eject_token (self, machine):
        print("machine vide")

    def turn_crank (self, machine):
        print("machine vide")

    def distribution(self, machine):
        print("machine vide")

class SURPRISE(State):
    def insert_token(self, machine):
        print("Félicitations ! Vous avez gagné une boule surprise !")
        machine.set_state(machine.no_token_state)

    def eject_token(self, machine):
        print("Vous avez remporté une boule gratuite !")
        machine.set_state(machine.no_token_state)

    def turn_crank(self, machine):
        print("Vous avez remporté une boule gratuite !")
        machine.set_state(machine.no_token_state)

    def distribution(self, machine):
        print("Boule surprise distribuée gratuitement !")
        if machine.numbers_of_balls > 0:
            machine.numbers_of_balls -= 1
        machine.set_state(machine.no_token_state)

class GiftBall:
    def __init__(self, numbers_of_balls):
        self.numbers_of_balls = numbers_of_balls
        self.one_token_state = ONE_TOKEN()
        self.no_token_state = NO_TOKEN()
        self.sold_out_state = SOLD_OUT()
        self.surprise_state = SURPRISE()
    
        if self.numbers_of_balls > 0 :
            self.current_state = self.one_token_state
        else : 
            self.current_state = self.sold_out_state


    def insert_token(self):
        self.current_state.insert_token(self)
    
    def eject_token(self):
        self.current_state.eject_token(self)
    
    def turn_crank(self):
        self.current_state.turn_crank(self)
    
    def set_state(self, state):
        self.current_state = state



    


