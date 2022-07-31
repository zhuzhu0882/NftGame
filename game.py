
import pandas as pd
import numpy as np
import time
import os
import random
import output_json
import warnings
import sys
import copy
import yaml

#人物基本面板  攻击力 防御力 生命值 治疗值 蓝条  药水 debuff buff 
#人物A B C D E
class Huaxing(object):
    #攻击力 防御力 生命值
     def __init__(self,Name,Damage,Defense,Life_Value) :
        self.Name=Name   #名称
        self.Damage=Damage  #攻击力
        self.Defense=Defense #防御力
        self.Life_Value=Life_Value #生命值
    
     def Run_Skill(self,x) :
        print("%s is running Skill" % x)

class Boss(object):
    #攻击力 防御力 生命值
     def __init__(self,Name,Damage,Defense,Life_Value) :
        self.Name=Name
        self.Damage=Damage  #攻击力
        self.Defense=Defense #防御力
        self.Life_Value=Life_Value #生命值
    
     def Run_Skill(self,x) :
        print("%s is running Skill" % x)

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

def Current_State(HX,boss):
    print(boss.Name,boss.Damage,boss.Defense,boss.Life_Value)
    for x in HX :
        print(x.Name,x.Damage,x.Defense,x.Life_Value)

def Current_Buf(HX,boss):
    total_buf = 0
    #攻击力 防御力 生命值 提升%
    hx_cur_buf =Cur_deuf(10,13,15)
    for x in HX :
        x.Damage +=hx_cur_buf.Damage
        x.Defense +=hx_cur_buf.Defense
        x.Life_Value +=hx_cur_buf.Life_Value
        print(x.Name,x.Damage,x.Defense,x.Life_Value)
    boss_cur_buf = Cur_deuf(10,13,1)
    boss.Damage +=boss_cur_buf.Damage
    boss.Defense +=boss_cur_buf.Defense
    boss.Life_Value +=boss_cur_buf.Life_Value
    print(boss.Name,boss.Damage,boss.Defense,boss.Life_Value)

def Current_Debuf(HX,boss):
    cur_debuf = 0

def HX_Round(HX,boss):
    #当前buf和debuf
    Current_Buf(HX,boss)
    Current_Debuf(HX,boss)

def Boss_Round(HX,boss):
    #当前buf和debuf
    Current_Buf(HX,boss)
    Current_Debuf(HX,boss)


#游戏回合
def Game_Round(HX,boss) :
    #当前人物状态
    Current_State(HX,boss)
    #化形的回合
    HX_Round(HX,boss)

    #Boss的回合
    Boss_Round(HX,boss)


def Game_start(HX,boss):
    #游戏一共10回合或者boss生命值为0
    #统计总伤害
    for round in range(10):
        Game_Round(HX,boss)
    


def main():
    #人物基本面板  攻击力 防御力 生命值 治疗值 蓝条  药水 debuff buff 
    #没人上限6格魔晶 初始6格 每回合恢复2格魔晶

    Huaxing_A = Huaxing('Huaxing_A',99,100,999)
    Huaxing_B = Huaxing('Huaxing_B',98,101,998)
    Huaxing_C = Huaxing('Huaxing_C',97,102,997)
    Huaxing_D = Huaxing('Huaxing_D',96,103,996)
    Huaxing_E = Huaxing('Huaxing_E',95,104,995)

    HX=[Huaxing_A,Huaxing_B,Huaxing_C,Huaxing_D,Huaxing_E]

    boss = Boss('Boss',1000,998,999)
    #boss.Run_Skill('Boss')
    #游戏开始
    Game_start(HX,boss)

main()