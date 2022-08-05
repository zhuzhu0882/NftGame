from person.person_base import *

def create_boss():
    name="boss"
    base_attr=[200, 3000, 3000]
    active_skill=['boss_skill', 500]
    passive_skill=['boss_damage', 60]
    person=Boss_Create(name, base_attr, active_skill, passive_skill)
    person.show_person_base_info()
    print("create %s ok" %name)
