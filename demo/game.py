from person.boss import create_boss
from person.super_man import create_super_man
from person.super_woman import create_super_woman

class Create_Game(object):
    def __init__(self, rounds):
        self.rounds=rounds

    def create_scenes(self):
        boss=create_boss()
        man=create_super_man()
        woman=create_super_woman()

    def game_round(self):
        pass

    def run(self):
        self.create_scenes();
        for round in range(self.rounds):
            print("current round: %d" %(round+1))
            self.game_round()
            print("\n")

