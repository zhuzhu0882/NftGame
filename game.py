
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
     def __init__(self,Name,Damage,Defense,Life_Value,Skill_Name,Mana,Buf,Ram,Buf_Count,Buf_Add) :
        self.Name=Name   #名称
        self.Damage=Damage  #攻击力
        self.Defense=Defense #防御力
        self.Life_Value=Life_Value #生命值
        self.Skill_Name=Skill_Name
        self.Mana=Mana
        self.Buf=Buf
        self.Ram=Ram
        self.Buf_Count=Buf_Count
        self.Buf_Add=Buf_Add
    
     def Run_Skill(self,x) :
        print("running Skill 造成伤害",x)

class Boss(object):
    #攻击力 防御力 生命值
     def __init__(self,Name,Damage,Defense,Life_Value,Skill_Name,Mana,Buf,Ram,Buf_Count,Buf_Add) :
        self.Name=Name
        self.Damage=Damage  #攻击力
        self.Defense=Defense #防御力
        self.Life_Value=Life_Value #生命值
        self.Skill_Name=Skill_Name
        self.Mana=Mana
        self.Buf=Buf
        self.Ram=Ram
        self.Buf_Count=Buf_Count
        self.Buf_Add=Buf_Add
    
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

def Init_State(HX,BOSS):
    print('-----人物基本面板初始状态-----')
    for x in HX :
        print(x.Name,x.Damage,x.Defense,x.Life_Value)

    for y in BOSS :
        print(y.Name,y.Damage,y.Defense,y.Life_Value)
    #print(BOSS.Name,BOSS.Damage,BOSS.Defense,BOSS.Life_Value) 
    print('---------------------------')

def Current_State(HX,BOSS):
    for x,xx in zip(HX,range(len(HX))) :
        print(x.Name,x.Damage,x.Defense,x.Life_Value)
        if x.Life_Value <=0:
            #HX.remove(x)
            [x.Damage,x.Defense,x.Life_Value]=[0,0,0]

    for y,yy in zip(BOSS,range(len(BOSS))) :
        print(y.Name,y.Damage,y.Defense,y.Life_Value)
        if y.Life_Value <=0:
            #HX.remove(x)
            [y.Damage,y.Defense,y.Life_Value]=[0,0,0]
    #print(BOSS.Name,BOSS.Damage,BOSS.Defense,BOSS.Life_Value)   

def Current_Buf(HX,BOSS):
    global count
    global HXBUF
    global hx_buf_change
    if hx_buf_change:
        for z,zz in zip(HX,range(len(HX))):
            HXBUF[zz] = z.Buf
        hx_buf_change=False
    for y,yy in zip(HX,range(len(HX))): 
        #if y.Life_Value >0:
        if y.Buf_Count >=4:
            y.Buf=HXBUF[yy]
            if y.Buf[3] ==0:
                if y.Buf[0] !=0:
                    y.Damage -= y.Buf_Add
                elif y.Buf[1] !=0:
                    y.Defense -= y.Buf_Add
            elif y.Buf[3] ==1:
                if y.Buf[0] !=0:
                    for k,kk in zip(HX,range(len(HX))):  
                        k.Damage -= y.Buf_Add 
                elif y.Buf[1] !=0:
                    for k,kk in zip(HX,range(len(HX))):
                        k.Defense -= y.Buf_Add 
            y.Buf_Count =0     
        if y.Life_Value <=0:
            [y.Damage,y.Defense,y.Life_Value]=[0,0,0]
        if y.Life_Value >0:
            if randint(1,100) <=y.Ram:        
                L1 = [y.Damage,y.Defense,y.Life_Value,0]
                if y.Buf_Count==0:  
                    print(y.Name,'触发了被动技能攻击力防御力增加:',np.multiply(np.array(L1[0:2]),np.array(y.Buf[0:2])))
                if y.Buf[3]!=0:
                    for x in HX: 
                        [x.Damage,x.Defense] =[x.Damage,x.Defense] + np.multiply(np.array(L1[0:2]),np.array(y.Buf[0:2]))
                else:
                    #L1= L1+np.multiply(np.array(L1),np.array(y.Buf))
                    [y.Damage,y.Defense]=[y.Damage,y.Defense]+np.multiply(np.array(L1[0:2]),np.array(y.Buf[0:2]))
                #[y.Damage,y.Defense,y.Life_Value]=L1[0:3]
                if y.Buf[0] !=0 and y.Buf_Count==0:
                    y.Buf_Add = np.multiply(np.array(L1[0]),np.array(y.Buf[0]))
                if y.Buf[1] !=0 and y.Buf_Count==0:
                    y.Buf_Add = np.multiply(np.array(L1[1]),np.array(y.Buf[1]))
                y.Buf=[0,0,0,0]
                if y.Buf_Count==0 :
                    y.Buf_Count=1
            if y.Buf_Count >=1:
                y.Buf_Count +=1


def Current_Debuf(HX,BOSS):
    cur_debuf = 0

def Boss_Current_Buf(HX,BOSS):
    global boss_count
    global BOSSBUF
    global boss_buf_change
    if boss_buf_change:
        #BOSSBUF = BOSS.Buf
        for z,zz in zip(BOSS,range(len(BOSS))):
            BOSSBUF[zz] = z.Buf
        boss_buf_change = False
    for y,yy in zip(BOSS,range(len(BOSS))): 
        #if y.Life_Value >0:
        if y.Buf_Count >=4:
            y.Buf=BOSSBUF[yy]
            if y.Buf[3] ==0:
                if y.Buf[0] !=0:
                    y.Damage -= y.Buf_Add
                elif y.Buf[1] !=0:
                    y.Defense -= y.Buf_Add
            elif y.Buf[3] ==1:
                if y.Buf[0] !=0:
                    for k in BOSS:  
                        k.Damage -= y.Buf_Add 
                elif y.Buf[1] !=0:
                    for k in BOSS:
                        k.Defense -= y.Buf_Add 
            y.Buf_Count =0
        if y.Life_Value <=0:
            [y.Damage,y.Defense,y.Life_Value]=[0,0,0]
        if y.Life_Value >0:
            if randint(1,100) <=y.Ram:
                L1 = [y.Damage,y.Defense,y.Life_Value,0]
                if y.Buf_Count==0:
                    print(y.Name,'触发了被动技能攻击力防御力增加:',np.multiply(np.array(L1[0:2]),np.array(y.Buf[0:2])))

                if y.Buf[3]!=0:
                    for x in BOSS: 
                        [x.Damage,x.Defense] =[x.Damage,x.Defense] + np.multiply(np.array(L1[0:2]),np.array(y.Buf[0:2]))
                else:
                    #L1= L1+np.multiply(np.array(L1),np.array(y.Buf))
                    [y.Damage,y.Defense]=[y.Damage,y.Defense]+np.multiply(np.array(L1[0:2]),np.array(y.Buf[0:2]))

                if y.Buf[0] !=0 and y.Buf_Count==0:
                    y.Buf_Add = np.multiply(np.array(L1[0]),np.array(y.Buf[0]))
                if y.Buf[1] !=0 and y.Buf_Count==0:
                    y.Buf_Add = np.multiply(np.array(L1[1]),np.array(y.Buf[1]))
                y.Buf=[0,0,0,0]
                if y.Buf_Count==0:
                    y.Buf_Count=1
            if y.Buf_Count >=1:
                y.Buf_Count +=1
            """
                if y.Buf_Count >4:
                    y.Buf=BOSSBUF[yy]
                    [y.Damage,y.Defense] = BOSSTEMP[yy][0:2]
                    y.Buf_Count =0
            """

def Boss_Current_Debuf(HX,BOSS):
    cur_debuf = 0

def HX_Round(HX,BOSS):
    #当前buf和debuf
    #持续的回合数
    global change
    global HXTEMP
    if change :
        for yy,ii in zip(HX,range(len(HX))):
            HXTEMP[ii] = [yy.Damage,yy.Defense,yy.Life_Value]
            #print(HXTEMP[i])
        change=False
    Current_Buf(HX,BOSS)

    if len(BOSS) > 1:
        randint_dex = randint(0,len(BOSS)-1)
        while BOSS[randint_dex].Life_Value <=0:
            randint_dex = randint(0,len(BOSS)-1)
    else:
        randint_dex=0
    #Current_Debuf(HX,boss)
    global Total_Damage
    for x,i in zip(HX,range(len(HX))) :
        if x.Life_Value >0:
            if(x.Mana>=3):
                if Skill_Value(x.Skill_Name)[0] !=0:
                    if Skill_Value(x.Skill_Name)[3] ==0:
                        print(x.Name,'使用技能:'+x.Skill_Name,'攻击了',BOSS[randint_dex].Name,Skill_Tree.get(x.Skill_Name),'造成的伤害值为:',x.Damage * Skill_Value(x.Skill_Name)[0] -BOSS[randint_dex].Defense)
                        BOSS[randint_dex].Life_Value -=(x.Damage * Skill_Value(x.Skill_Name)[0] -BOSS[randint_dex].Defense)
                        Total_Damage +=(x.Damage * Skill_Value(x.Skill_Name)[0] -BOSS[randint_dex].Defense) 
                        x.Mana -=3
                    else: 
                        Cur_Damage = 0                     
                        for z in BOSS: 
                            if z.Life_Value >0:
                                z.Life_Value -=(x.Damage * Skill_Value(x.Skill_Name)[0] -z.Defense)
                                Cur_Damage  +=(x.Damage * Skill_Value(x.Skill_Name)[0] -z.Defense) 
                                Total_Damage +=(x.Damage * Skill_Value(x.Skill_Name)[0] -z.Defense) 
                        x.Mana -=3
                        #x.Damage * Skill_Value(x.Skill_Name)[0] -BOSS[randint_dex].Defense
                        print(x.Name,'使用技能:'+x.Skill_Name,'攻击了','全体BOSS',Skill_Tree.get(x.Skill_Name),'造成的全体伤害值为:',Cur_Damage)

                elif Skill_Value(x.Skill_Name)[1] !=0:
                    print(x.Name,'使用技能:'+x.Skill_Name,Skill_Tree.get(x.Skill_Name),'增加自身防御值为:',x.Defense * Skill_Value(x.Skill_Name)[1])
                    x.Defense +=(x.Defense * Skill_Value(x.Skill_Name)[1])
                    Total_Damage +=0
                    x.Mana -=3
                elif Skill_Value(x.Skill_Name)[2] !=0:
                    if Skill_Value(x.Skill_Name)[3] ==0:
                        print(x.Name,'使用技能:'+x.Skill_Name,Skill_Tree.get(x.Skill_Name),'恢复自身血量值为:',x.Life_Value * Skill_Value(x.Skill_Name)[2])
                        x.Life_Value +=(x.Life_Value * Skill_Value(x.Skill_Name)[2])
                        if x.Life_Value >=HXTEMP[i][2]:
                            x.Life_Value = HXTEMP[i][2]
                        Total_Damage +=0
                        x.Mana -=3
                    else :
                        print(x.Name,'使用技能:'+x.Skill_Name,Skill_Tree.get(x.Skill_Name),'恢复全体血量值为:',HXTEMP[i][2] * Skill_Value(x.Skill_Name)[2])
                        for y,j in zip(HX,range(len(HX))):
                            if y.Life_Value >0:
                                y.Life_Value +=HXTEMP[i][2] * Skill_Value(x.Skill_Name)[2]
                                if y.Life_Value >=HXTEMP[j][2]:
                                    y.Life_Value = HXTEMP[j][2]
                        Total_Damage +=0
                        x.Mana -=3
                    
            else:
                print(x.Name,'使用普通攻击:','攻击了',BOSS[randint_dex].Name,'造成的伤害值为:',x.Damage-BOSS[randint_dex].Defense)
                BOSS[randint_dex].Life_Value -=(x.Damage-BOSS[randint_dex].Defense)
                Total_Damage +=(x.Damage-BOSS[randint_dex].Defense)
            
            x.Mana +=1
    print('当前总伤害为:',Total_Damage)

def Boss_Round(HX,BOSS):
    #当前buf和debuf
    #Boss_Current_Buf(HX,BOSS)
    #Boss_Current_Debuf(HX,BOSS)
    global boss_change
    global BOSSTEMP
    if boss_change :
        #BOSSTEMP = [BOSS.Damage,BOSS.Defense,BOSS.Life_Value]
        for y,i in zip(BOSS,range(len(BOSS))):
            BOSSTEMP[i] = [y.Damage,y.Defense,y.Life_Value]
        boss_change=False
    Boss_Current_Buf(HX,BOSS)
    #Current_Debuf(HX,BOSS)
    
    #HX[0].Run_Skill(BOSS.Defense)
    if len(HX) > 1:
        randint_dex = randint(0,len(HX)-1)
        while HX[randint_dex].Life_Value <=0:
            randint_dex = randint(0,len(HX)-1)
    else:
        randint_dex=0

    for x,j in zip(BOSS,range(len(BOSS))) :
        if x.Life_Value >0:
            if(x.Mana>=3):
                if Skill_Value(x.Skill_Name)[0] !=0:
                    if Skill_Value(x.Skill_Name)[3] ==0:
                        print(x.Name,'使用技能:'+x.Skill_Name,'攻击了',HX[randint_dex].Name,Skill_Tree.get(x.Skill_Name),'造成的伤害值为:',x.Damage * Skill_Value(x.Skill_Name)[0] -HX[randint_dex].Defense)
                        HX[randint_dex].Life_Value -=(x.Damage * Skill_Value(x.Skill_Name)[0] -HX[randint_dex].Defense)
                        x.Mana -=3
                    else:
                        #print(x.Name,'使用技能:'+x.Skill_Name,'攻击了','全体HX',Skill_Tree.get(x.Skill_Name),'造成的伤害值为:',x.Damage * Skill_Value(x.Skill_Name)[0] -HX[randint_dex].Defense)
                        print(x.Name,'使用技能:'+x.Skill_Name,'攻击了','全体HX')
                        for z in HX: 
                            if z.Life_Value >0:
                                print('对',z.Name,'造成了伤害值为:',(x.Damage * Skill_Value(x.Skill_Name)[0] -z.Defense))
                                z.Life_Value -=(x.Damage * Skill_Value(x.Skill_Name)[0] -z.Defense)                              
                        x.Mana -=3
            else:
                print(x.Name,'使用普通攻击攻击了:',HX[randint_dex].Name,'造成的伤害值为:',x.Damage-HX[randint_dex].Defense)
                HX[randint_dex].Life_Value -=(x.Damage-HX[randint_dex].Defense)
        x.Mana +=1
    pass


#游戏回合
def Game_Round(HX,BOSS) :
    #化形的回合
    HX_Round(HX,BOSS)
    boss_value=0
    #if BOSS.Life_Value <=0:
    for z in BOSS :
        if z.Life_Value >0:
            boss_value =1
            break
    if boss_value != 1:
        print('恭喜你击败了BOSS!!')
        sys.exit()
    #Boss的回合
    Boss_Round(HX,BOSS)
    Current_State(HX,BOSS)
    hx_value =0
    for x in HX :
        if x.Life_Value >0:
            hx_value =1
            break
    if hx_value != 1:
        print('你被击败了,游戏结束!!')
        sys.exit()
 


def Game_start(HX,BOSS):
    global init_change
    #人物初始状态
    if init_change:
        Init_State(HX,BOSS)
        init_change=False
    #游戏一共10回合或者boss生命值为0
    #统计总伤害
    for round in range(40):
        print('==============第',index(round),'回合=============')
        Game_Round(HX,BOSS)
    Current_State(HX,BOSS)


def main():
    #人物基本面板  攻击力 防御力 生命值 治疗值 蓝条  药水 debuff buff 
    #没人上限6格魔晶 初始6格 每回合恢复2格魔晶

    #print(Skill_Tree.get('异色神光')) 
    #人物基本面板  攻击力 防御力 生命值 技能名称 法力初始值 增buf 触发概率 持续回合数 buf增加的值
    Huaxing_A = Huaxing('Huaxing_A',200,100,3999,'异色神光',6,[0.3,0,0,0],30,0,0)
    Huaxing_B = Huaxing('Huaxing_B',198,101,3998,'大荒八卦阵',7,[0,0.5,0,1],30,0,0)
    Huaxing_C = Huaxing('Huaxing_C',197,102,3000,'聚能投射',6,[0.3,0,0,0],30,0,0)
    Huaxing_D = Huaxing('Huaxing_D',196,103,3996,'玄阳剑诀',7,[0,0.4,0,0],30,0,0)
    Huaxing_E = Huaxing('Huaxing_E',195,104,3995,'回魂术',8,[0.5,0,0,0],25,0,0)

    HX=[Huaxing_A,Huaxing_B,Huaxing_C,Huaxing_D,Huaxing_E]

    boss1 = Boss('1号Boss',360,138,9999,'灭魂针',8,[0,0.3,0,0],25,0,0)
    boss2 = Boss('2号Boss',380,148,9999,'异色神光',8,[0.5,0,0,1],30,0,0)
    BOSS= [boss1,boss2]
    #boss.Run_Skill('Boss')

    #将所有打印日志输出到一个文件中
    with open("mygamefile.txt",'w+',encoding='UTF-8') as fw:
        #sys.stdout=fw
        #游戏开始
        Game_start(HX,BOSS)

main()
