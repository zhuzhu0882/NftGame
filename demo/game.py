from person.create_person import *

class Create_Game(object):
    '''
    创建一场游戏
    '''
    def __init__(self, rounds):
        self.rounds=rounds

    def create_scenes(self):
        person=Create_Person()
        boss=person.create_boss()
        man=person.create_super_man()
        woman=person.create_super_woman()

    def game_round(self):
        pass

    def run(self):
        self.create_scenes();
        for round in range(self.rounds):
            print("current round: %d" %(round+1))
            self.game_round()
            print("\n")

