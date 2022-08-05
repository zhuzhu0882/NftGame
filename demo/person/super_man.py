from person.person_base import *

def create_super_man():
    name="super man"
    base_attr=[100, 1000, 1000]
    active_skill=['skill', 200]
    passive_skill=['damage', 50]
    person=Person_Create(name, base_attr, active_skill, passive_skill)
    person.show_person_base_info()
    print("create %s ok" %name)