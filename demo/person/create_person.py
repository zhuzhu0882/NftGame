from person.person_base import *

class Create_Person(object):
    '''
    创建各种人物
    '''
    def __init__(self):
        pass

    def create_boss(self):
        name="boss"
        base_attr={'damage':200, 'defense':3500, 'life_value':3000}
        active_skill={'boss_skill':500}
        passive_skill={'boss_damage':60}
        person=Boss_Create(name, base_attr, active_skill, passive_skill)
        person.show_person_base_info()
        print("create %s ok" %name)

    def create_super_man(self):
        name="super man"
        base_attr={'damage':100, 'defense':1100, 'life_value':1000}
        active_skill={'skill':200}
        passive_skill={'damage':50}
        person=Person_Create(name, base_attr, active_skill, passive_skill)
        person.show_person_base_info()
        print("create %s ok" %name)

    def create_super_woman(self):
        name="super woman"
        base_attr={'damage':80, 'defense':1000, 'life_value':900}
        active_skill={'skill':200}
        passive_skill={'damage':50}
        person=Person_Create_Have_Blue_Bar(name, base_attr, active_skill, passive_skill, 15)
        person.show_person_base_info()
        print("create %s ok" %name)
