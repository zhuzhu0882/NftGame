
class Passive_Skill(object):
    '''
    被动技能
    '''
    def __init__(self, passive_skill):
        self.passive_skill_name=passive_skill.keys()
        self.passive_skill_hurt=passive_skill.values()

    def show_passive_skill_info(self):
        print(self.passive_skill_name + ": %d" %self.passive_skill_hurt)

class Active_Skill(object):
    '''
    主动技能
    '''  
    def __init__(self, skill):
        self.active_skill_name=skill.keys()
        self.active_skill_hurt=skill.values()

    def show_active_skill_info(self):
        print(self.active_skill_name + ": %d" %self.active_skill_hurt)

class Person_Base_Attribute(object):
    '''
    人物基本含有属性：
        攻击力 防御力 生命值
    '''
    def __init__(self, base_attr):
        '''
        初始化需要传入一个1x3数组，分别为攻击力，防御力，生命值
        '''
        self.damage=base_attr['damage']
        self.defense=base_attr['defense']
        self.life_value=base_attr['life_value']

    def show_person_base_info(self):
        print("damage: %d" %self.damage)
        print("defense: %d" %self.defense)
        print("life value: %d" %self.life_value)

class Blue_Bar(object):
    '''
    蓝条：
        蓝条对技能施展有限制
    '''
    def __init__(self, consume):
        self.max_blue_bar=100
        self.use_skill_min_bule_bar=consume  
        self.current_blue_bar=self.max_blue_bar

    def show_current_blue_bar(self):
        print("current blue bar: %d" %self.current_blue_bar)

    def blue_bar_lower(self, value):
        if (self.current_blue_bar >= value):
            self.current_blue_bar = self.current_blue_bar - value

    def blue_bar_upper(self, value):
        if (self.current_blue_bar >= self.max_blue_bar):
            return

        if (self.max_blue_bar - self.current_blue_bar < value):
            self.current_blue_bar = self.max_blue_bar
            return
        
        self.current_blue_bar = self.current_blue_bar + value

    def have_use_skill(self):
        if (self.current_blue_bar < self.use_skill_min_bule_bar):
            print("has no enough blue bar")
            return False
        return True

class Person_Create(Person_Base_Attribute, Active_Skill, Passive_Skill):
    '''
    创建无蓝条人物
    '''
    def __init__(self, name, base_attr, active_skill, passive_skill):
        self.person_name=name
        self.bule_bar_limit=False
        Person_Base_Attribute.__init__(self, base_attr)
        Active_Skill.__init__(self, active_skill)
        Passive_Skill.__init__(self, passive_skill)

    def show_person_info(self):
        print("person name: %s" %self.person_name)
        super().show_person_base_info()
        super().show_active_skill_info()
        super().show_passive_skill_info()

class Person_Create_Have_Blue_Bar(Person_Base_Attribute, Active_Skill, Passive_Skill, Blue_Bar):
    '''
    创建有蓝条人物
    '''
    def __init__(self, name, base_attr, active_skill, passive_skill, consume):
        self.person_name=name
        self.bule_bar_limit=True
        Person_Base_Attribute.__init__(self, base_attr)
        Active_Skill.__init__(self, active_skill)
        Passive_Skill.__init__(self, passive_skill)
        Blue_Bar.__init__(self, consume)

    def show_person_info(self):
        print("person name: %s" %self.person_name)
        super().show_current_blue_bar()
        super().show_person_base_info()
        super().show_active_skill_info()
        super().show_passive_skill_info()

class Boss_Create(Person_Create):
    '''
    创建boss
    '''
    def __init__(self, name, base_attr, active_skill, passive_skill):
        self.person_name=name
        Person_Base_Attribute.__init__(self, base_attr)
        Active_Skill.__init__(self, active_skill)
        Passive_Skill.__init__(self, passive_skill)

    def show_person_info(self):
        print("person name: %s" %self.person_name)
        super().show_person_base_info()
        super().show_active_skill_info()
        super().show_passive_skill_info()
