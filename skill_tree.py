
Total_Damage=0
#技能树
Skill_Tree = {'异色神光':'镇压敌方单体，造成攻击152%的伤害',
            '大荒八卦阵':'绞杀敌方单体，造成攻击142%的伤害',
            '聚能投射':'光线射击敌方单体，造成攻击148%的伤害',
            '玄阳剑诀':'玄阳飞剑射向敌方单体，造成攻击138%的伤害',
            '灭魂针':'灭魂针射向敌方单体，造成攻击168%的伤害',
    }

def Skill_Value(skill_name):
    if skill_name == '异色神光':
        return 1.52
    elif skill_name == '大荒八卦阵':
        return 1.42
    elif skill_name == '聚能投射':
        return 1.48
    elif skill_name == '玄阳剑诀':
        return 1.38
    elif skill_name == '灭魂针':
        return 1.68

