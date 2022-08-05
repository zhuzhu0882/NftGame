from person.person_base import *

def create_super_woman():
    name="super woman"
    base_attr=[80, 800, 900]
    active_skill=['skill', 200]
    passive_skill=['damage', 50]
    person=Person_Create_Have_Blue_Bar(name, base_attr, active_skill, passive_skill, 15)
    person.show_person_base_info()
    print("create %s ok" %name)
