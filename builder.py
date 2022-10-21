from math import floor
from tkinter import *
from tkinter.ttk import *

def addStat(i_master, i_statName, i_statVal):
    statMod = floor((int(i_statVal)-10)/2)

    frm_skill = Frame(master=i_master, relief=GROOVE)
    btn_stat = Button(master=frm_skill, text=statMod)
    lbl_statVal = Label(master=frm_skill, text=i_statVal)
    lbl_statName = Label(master=frm_skill, text=i_statName)
    
    lbl_statName.pack(expand=True)
    btn_stat.pack(expand=True)
    lbl_statVal.pack(expand=True)
    frm_skill.pack(expand=True)

    return frm_skill

def addProfBonus(i_profBonus, i_skillVal):
    return i_profBonus + i_skillVal

def addSkill(i_master, i_skillName, i_skillVal):
    frm_skill = Frame(master=i_master)
    chk_prof = Checkbutton(master=frm_skill)
    lbl_skill = Label(master=frm_skill, text=i_skillName)
    btn_skill = Button(master=frm_skill, text=i_skillVal)
    
    chk_prof.pack(side=LEFT, expand=True)
    btn_skill.pack(side=LEFT, expand=True)
    lbl_skill.pack(side=RIGHT, fill=BOTH, expand=True)
    frm_skill.pack()

    return frm_skill

def removeStat():
    pass

def removeSkill():
    pass

def addSpellSlot(i_master, i_spellName):
    frm_spellSlot = Frame(master=i_master)
    chk_prep = Checkbutton(master=frm_spellSlot)
    ent_spellSlot = Entry(master=frm_spellSlot)
    ent_spellSlot.insert(0, i_spellName)
    
    chk_prep.pack(side=LEFT)
    ent_spellSlot.pack(side=RIGHT)
    frm_spellSlot.pack()

    return frm_spellSlot


def addAttack(i_master, i_attackName, i_attackBns, i_dmg):
    frm_attack = Frame(master=i_master)
    btn_attackBns = Button(master=frm_attack, text=i_attackBns)
    btn_dmg = Button(master=frm_attack, text=i_dmg)
    lbl_attackName = Label(master=frm_attack, text=i_attackName)
    
    lbl_attackName.pack(side=LEFT)
    btn_attackBns.pack(side=LEFT)
    btn_dmg.pack(side=LEFT)
    frm_attack.pack()

    return frm_attack



def searchForWidget(i_parent, i_name):
    children = i_parent.winfo_children()
    for child in children:
        if child["text"] == i_name:
            return child

def getModifierFromStat(i_parent, i_statName):
    children = i_parent.winfo_children()
    for child in children:
        if child.winfo_children() != None:
            if searchForWidget(child, i_statName):
                return child.winfo_children()[0]["text"]

def recursiveSearchForWidget(i_parent, i_name):
    children = i_parent.winfo_children()
    for child in children:
        if child.winfo_id() == i_name:
            return child            
        else:
            if child.winfo_children() != None:
                return searchForWidget(child, i_name)