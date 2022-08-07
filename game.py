
from operator import index
import time
import os
from random import Random, randint
import sys
import copy
import numpy as np
from skill_tree import Skill_Tree
from skill_tree import Skill_Value
from skill_tree import Total_Damage
from skill_tree import count,change,HXTEMP,HXBUF,boss_change,BOSSBUF,BOSSTEMP,boss_count,init_change,boss_buf_change,hx_buf_change
#人物基本面板  攻击力 防御力 生命值 治疗值 蓝条  药水 debuff buff 
#攻击力=基本攻击力+武器符文加成攻击力+符石加成
#人物A B C D E

class Huaxing(object):
    #攻击力 防御力 生命值 技能 法力值
     def __init__(self,Name,Damage,Defense,Life_Value,Skill_Name,Mana,Buf,Ram,Buf_Count) :
        self.Name=Name   #名称
        self.Damage=Damage  #攻击力
        self.Defense=Defense #防御力
        self.Life_Value=Life_Value #生命值
        self.Skill_Name=Skill_Name
        self.Mana=Mana
        self.Buf=Buf
        self.Ram=Ram
        self.Buf_Count=Buf_Count
    
     def Run_Skill(self,x) :
        print("running Skill 造成伤害",x)

class Boss(object):
    #攻击力 防御力 生命值
     def __init__(self,Name,Damage,Defense,Life_Value,Skill_Name,Mana,Buf,Ram,Buf_Count) :
        self.Name=Name
        self.Damage=Damage  #攻击力
        self.Defense=Defense #防御力
        self.Life_Value=Life_Value #生命值
        self.Skill_Name=Skill_Name
        self.Mana=Mana
        self.Buf=Buf
        self.Ram=Ram
        self.Buf_Count=Buf_Count
    
     def Run_Skill(self,x) :
        print("running Skill 造成伤害",x)

class Cur_Buf(object):
    def __init__(self,Damage,Defense,Life_Value) :
        self.Damage=Damage  #攻击力
        self.Defense=Defense #防御力
        self.Life_Value=Life_Value #生命值

class Cur_deuf(object):
    def __init__(self,Damage,Defense,Life_Value) :
        self.Damage=Damage  #攻击力
        self.Defense=Defense #防御力
        self.Life_Value=Life_Value #生命值

def Init_State(HX,boss):
    print('-----人物基本面板初始状态-----')
    for x in HX :
        print(x.Name,x.Damage,x.Defense,x.Life_Value)

    print(boss.Name,boss.Damage,boss.Defense,boss.Life_Value) 
    print('---------------------------')

def Current_State(HX,boss):
    for x in HX :
        print(x.Name,x.Damage,x.Defense,x.Life_Value)
        if x.Life_Value <=0:
            HX.remove(x)
    print(boss.Name,boss.Damage,boss.Defense,boss.Life_Value)   

def Current_Buf(HX,boss):
    global count
    global HXBUF
    global hx_buf_change
    if hx_buf_change:
        for z,zz in zip(HX,range(5)):
            HXBUF[zz] = z.Buf
        hx_buf_change=False
    for y,yy in zip(HX,range(5)): 
        if randint(1,100) <=y.Ram:        
            L1 = [y.Damage,y.Defense,y.Life_Value,0]
            print(y.Name,'触发了被动技能攻击力防御力增加:',np.multiply(np.array(L1[0:2]),np.array(y.Buf[0:2])))
            if y.Buf[3]!=0:
                for x in HX: 
                    L1 = L1+np.multiply(np.array(L1),np.array(x.Buf))
                    pass
            else:
                L1= L1+np.multiply(np.array(L1),np.array(y.Buf))
                pass
            [y.Damage,y.Defense,y.Life_Value]=L1[0:3]
            y.Buf=[0,0,0,0]
            if y.Buf_Count==0:
                y.Buf_Count=1
        if y.Buf_Count >=1:
            y.Buf_Count +=1
            if y.Buf_Count >4:
                y.Buf=HXBUF[yy]
                [y.Damage,y.Defense] = HXTEMP[yy]
                y.Buf_Count =0

def Current_Debuf(HX,boss):
    cur_debuf = 0

def Boss_Current_Buf(HX,boss):
    global boss_count
    global BOSSBUF
    global boss_buf_change
    if boss_buf_change:
        BOSSBUF = boss.Buf
        boss_buf_change = False
    if randint(1,100) <=boss.Ram:
        L1 = [boss.Damage,boss.Defense,boss.Life_Value,0]
        print('BOSS触发了被动技能攻击力防御力增加:',np.multiply(np.array(L1[0:2]),np.array(boss.Buf[0:2])))
        if boss.Buf[3]!=0: 
            L1 = L1+np.multiply(np.array(L1),np.array(boss.Buf))
            pass
        else:
            L1= L1+np.multiply(np.array(L1),np.array(boss.Buf))
            pass
        [boss.Damage,boss.Defense,boss.Life_Value]=L1[0:3]
        boss.Buf=[0,0,0,0]
        if boss.Buf_Count==0:
            boss.Buf_Count=1
    if boss.Buf_Count >=1:
        boss.Buf_Count +=1
        if boss.Buf_Count >4:
            boss.Buf=BOSSBUF
            [boss.Damage,boss.Defense] = BOSSTEMP[0:2]
            boss.Buf_Count =0

def Boss_Current_Debuf(HX,boss):
    cur_debuf = 0

def HX_Round(HX,boss):
    #当前buf和debuf
    #持续的回合数
    global change
    global HXTEMP
    if change :
        for y,i in zip(HX,range(5)):
            HXTEMP[i] = [y.Damage,y.Defense]
            #print(HXTEMP[i])
        change=False
    Current_Buf(HX,boss)
    """
    if cur_count ==3:   
        for yy,ii in zip(HX,range(5)):
            [yy.Damage,yy.Defense] = HXTEMP[ii]
    """
    #Current_Debuf(HX,boss)
    
    #HX[0].Run_Skill(boss.Defense)
    global Total_Damage
    for x in HX :
        if(x.Mana>=3):
            print(x.Name,'使用技能:'+x.Skill_Name,Skill_Tree.get(x.Skill_Name),'造成的伤害值为:',x.Damage * Skill_Value(x.Skill_Name) -boss.Defense)
            boss.Life_Value -=(x.Damage * Skill_Value(x.Skill_Name) -boss.Defense)
            Total_Damage +=(x.Damage * Skill_Value(x.Skill_Name) -boss.Defense) 
            x.Mana -=3
        else:
            print(x.Name,'使用普通攻击:','造成的伤害值为:',x.Damage-boss.Defense)
            boss.Life_Value -=(x.Damage-boss.Defense)
            Total_Damage +=(x.Damage-boss.Defense)
        x.Mana +=1
    print('当前总伤害为:',Total_Damage)
        

    #print('造成实际伤害',x.Damage * Skill_Value(x.Skill_Name) -boss.Defense)

def Boss_Round(HX,boss):
    #当前buf和debuf
    #Boss_Current_Buf(HX,boss)
    #Boss_Current_Debuf(HX,boss)
    global boss_change
    global BOSSTEMP
    if boss_change :
        BOSSTEMP = [boss.Damage,boss.Defense,boss.Life_Value]
        boss_change=False
    Boss_Current_Buf(HX,boss)
    #Current_Debuf(HX,boss)
    
    #HX[0].Run_Skill(boss.Defense)
    if len(HX) > 1:
        randint_dex = randint(0,len(HX)-1)
    else:
        randint_dex=0

    if(boss.Mana>=3):
        print(boss.Name,'使用技能:'+boss.Skill_Name,'攻击了',HX[randint_dex].Name,Skill_Tree.get(boss.Skill_Name),'造成的伤害值为:',boss.Damage * Skill_Value(boss.Skill_Name) -HX[randint_dex].Defense)
        HX[randint_dex].Life_Value -=(boss.Damage * Skill_Value(boss.Skill_Name) -HX[randint_dex].Defense)
        boss.Mana -=3
    else:
        print(boss.Name,'使用普通攻击攻击了:',HX[randint_dex].Name,'造成的伤害值为:',boss.Damage-HX[randint_dex].Defense)
        HX[randint_dex].Life_Value -=(boss.Damage-HX[randint_dex].Defense)
    boss.Mana +=1
    
    pass


#游戏回合
def Game_Round(HX,boss) :
    #化形的回合
    HX_Round(HX,boss)
    if boss.Life_Value <=0:
        print('恭喜你击败了BOSS!!')
        sys.exit()
    #Boss的回合
    Boss_Round(HX,boss)
    Current_State(HX,boss)
    if len(HX) <=0:
        print('你被击败了,游戏结束!!')
        sys.exit()
 


def Game_start(HX,boss):
    global init_change
    #人物初始状态
    if init_change:
        Init_State(HX,boss)
        init_change=False
    #游戏一共10回合或者boss生命值为0
    #统计总伤害
    for round in range(20):
        print('==============第',index(round),'回合=============')
        Game_Round(HX,boss)
    Current_State(HX,boss)


def main():
    #人物基本面板  攻击力 防御力 生命值 治疗值 蓝条  药水 debuff buff 
    #没人上限6格魔晶 初始6格 每回合恢复2格魔晶

    #print(Skill_Tree.get('异色神光')) 
    #人物基本面板  攻击力 防御力 生命值 技能名称 法力初始值 增buf 触发概率 持续回合数
    Huaxing_A = Huaxing('Huaxing_A',200,100,999,'异色神光',6,[0.3,0,0,0],30,0)
    Huaxing_B = Huaxing('Huaxing_B',198,101,998,'大荒八卦阵',7,[0,0.5,0,1],30,0)
    Huaxing_C = Huaxing('Huaxing_C',197,102,1000,'聚能投射',6,[0.3,0,0.6,0],30,0)
    Huaxing_D = Huaxing('Huaxing_D',196,103,996,'玄阳剑诀',7,[0,0.4,0,0],30,0)
    Huaxing_E = Huaxing('Huaxing_E',195,104,995,'灭魂针',8,[0.5,0,0,0],25,0)

    HX=[Huaxing_A,Huaxing_B,Huaxing_C,Huaxing_D,Huaxing_E]

    boss = Boss('Boss',360,188,9999,'灭魂针',8,[0.3,0.3,0,0],25,0)
    #boss.Run_Skill('Boss')

    #将所有打印日志输出到一个文件中
    with open("mygamefile.txt",'w+',encoding='UTF-8') as fw:
        #sys.stdout=fw
        #游戏开始
        Game_start(HX,boss)

main()
