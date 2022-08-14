
HXBUF={}
HXTEMP={}
BOSSBUF={}
BOSSTEMP={}
change = True
boss_change=True
init_change=True
boss_buf_change=True
hx_buf_change=True
count =0
boss_count=0
Total_Damage=0
#技能树
Skill_Tree = {'异色神光':'镇压敌方，造成攻击112%的伤害',
            '大荒八卦阵':'绞杀敌方，造成攻击142%的伤害',
            '聚能投射':'光线射击敌方，造成攻击148%的伤害',
            '玄阳剑诀':'玄阳飞剑射向敌方，造成攻击138%的伤害',
            '灭魂针':'灭魂针射向敌方，造成攻击168%的伤害',
            '回魂术':'使用回魂法术，恢复全体以施放者血量上限的20%的血'
    }

def Skill_Value(skill_name):
    if skill_name == '异色神光':
        #技能攻击伤害 防御增强 血量恢复 单体/全体 消耗法力值
        return [1.12,0,0,0,1]
    elif skill_name == '大荒八卦阵':
        return [1.42,0,0,0,2]
    elif skill_name == '聚能投射':
        return [1.48,0,0,1,3]
    elif skill_name == '玄阳剑诀':
        return [1.38,0,0,0,4]
    elif skill_name == '灭魂针':
        return [1.68,0,0,1,5]
    elif skill_name == '回魂术':
        return [0,0,0.2,1,6]

