from inspect import EndOfBlock
from tkinter import *
from tkinter.ttk import *
from math import floor
import random

window = Tk()

### Globals

stats = ["10", "10", "10", "10", "10", "10"]
modNames = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
skillNames = [["Athletics"], 
              ["Acrobatics", "Sleight of Hand", "Stealth"], 
              [], 
              ["Aracana", "History", "Investigation", "Nature", "Religion"], 
              ["Animal Handling", "Insight", "Medicine", "Perception", "Survival"], 
              ["Intimidation", "Performance", "Persuasion"]]
classes = ["Artificer", "Barbarian", "Bard", "Blood Hunter", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

plyrLevel = 0
plyrClass = "Commoner"

weaponList = []

chkBoxStartVal = IntVar(value=0)

### Functions

def roll(i_numDice=1, i_diceSides=20):
    total = 0
    
    for i in range(i_numDice):
        total += random.randint(1, i_diceSides)
    return total

def buildRollWindow(mod, roll):
    wnd_roll = Toplevel()
    lbl_calculations = Label(master=wnd_roll, text=f"{roll} + {mod} = {roll+mod}")
    lbl_calculations.pack()


def refreshStats():
    global stats, modNames, skillNames, weaponList
    updateStats(stats, modNames, skillNames)
    clearWeapons()
    for weapon in weaponList:
        addWeapon(weapon[0], weapon[1], weapon[2], weapon[3], weapon[4], weapon[5], weapon[6])
    

def addStat(i_master, i_statName, i_statVal):
    statMod = floor((int(i_statVal)-10)/2)

    frm_stat = Frame(master=i_master, relief=GROOVE)
    btn_stat = Button(master=frm_stat, text=statMod, command=lambda : buildRollWindow(int(getModifierFromStat(frm_stats, i_statName)), roll()))
    lbl_statVal = Label(master=frm_stat, text=i_statVal)
    lbl_statName = Label(master=frm_stat, text=i_statName)
    
    lbl_statName.pack(expand=True)
    btn_stat.pack(expand=True)
    lbl_statVal.pack(expand=True)
    frm_stat.pack(expand=True)

    return frm_stat

def addProfBonus(i_profBonus, i_skillVal):
    return i_profBonus + i_skillVal

def addSkill(i_master, i_skillName, i_skillVal):
    frm_skill = Frame(master=i_master)
    chk_prof = Checkbutton(master=frm_skill, variable=chkBoxStartVal)
    lbl_skill = Label(master=frm_skill, text=i_skillName)
    btn_skill = Button(master=frm_skill, text=i_skillVal, command=lambda : buildRollWindow(int(i_skillVal), roll()))
    
    chk_prof.pack(side=LEFT, expand=True)
    btn_skill.pack(side=LEFT, expand=True)
    lbl_skill.pack(side=RIGHT, fill=BOTH, expand=True)
    frm_skill.pack()

    return frm_skill


def clearStats(i_frame):
    for child in i_frame.winfo_children():
        child.destroy()

def clearWeapons():
    for child in frm_attacks.winfo_children():
        child.destroy()

def getWeapons():
    global weaponList
    weapon_names = []
    for weapon in weaponList:
        print(weapon[0])
        weapon_names.append(weapon[0])
    return weapon_names

def updateStats(i_stats, i_statNames, i_skillNames):
    clearStats(frm_stats)
    clearStats(frm_statSkills)
    clearStats(frm_savingThrows)

    for i in range(len(i_stats)):
        addStat(frm_stats, i_statNames[i], i_stats[i])

    mods = []
    for stat in i_stats:
        mods.append(getModifierFromStat(frm_stats, stat))

    for i in range(len(i_stats)):
        addSkill(frm_savingThrows, i_statNames[i], mods[i])

    for i in range(len(i_skillNames)):
        for j in range(len(i_skillNames[i])):
            addSkill(frm_statSkills, i_skillNames[i][j], mods[i])

    
def addSpellSlot(i_master, i_spellName):
    frm_spellSlot = Frame(master=i_master)
    chk_prep = Checkbutton(master=frm_spellSlot, variable=chkBoxStartVal)
    ent_spellSlot = Entry(master=frm_spellSlot)
    ent_spellSlot.insert(0, i_spellName)
    
    chk_prep.pack(side=LEFT)
    ent_spellSlot.pack(side=RIGHT)
    frm_spellSlot.pack()

    return frm_spellSlot


def rangedAttack(i_attackBns, i_lbl_ammoCount, i_numDice=1, i_diceSides=6):
    if int(i_lbl_ammoCount["text"]) > 0:
        buildRollWindow(i_attackBns, roll(i_numDice=i_numDice, i_diceSides=i_diceSides))
        i_lbl_ammoCount["text"] = (int(i_lbl_ammoCount["text"])-1)

def addWeapon(i_weaponName, i_dmgDice="1d6", i_additionalBns=0, i_additionalDmg=0, i_isDex=False, i_ammoCount=-1):
    global weaponList

    frm_weapon = Frame(master=frm_attacks)

    weaponList.append([i_weaponName, i_dmgDice, i_additionalBns, i_additionalDmg, i_isDex, i_ammoCount])

    # need to add proficiency bonus
    attackBns = floor((int(stats[i_isDex])-10)/2 + i_additionalBns)
    dmgBns = floor((int(stats[i_isDex])-10)/2 + i_additionalDmg)

    attackText = f"{floor((int(stats[i_isDex])-10)/2)}+{i_additionalBns}"
    dmgText = f"{floor((int(stats[i_isDex])-10)/2)}+{i_additionalDmg}+{i_dmgDice}"

    numDmgDice = int(i_dmgDice.split("d")[0])
    sidesDmgDice = int(i_dmgDice.split("d")[1])

    lbl_ammoCount = None

    btn_attackBns = Button(master=frm_weapon, text=attackText, command=lambda : buildRollWindow(dmgBns, roll()))
    btn_dmg = Button(master=frm_weapon, text=dmgText, command=lambda : buildRollWindow(attackBns, roll(i_numDice=numDmgDice, i_diceSides=sidesDmgDice)) if i_ammoCount < 0 else rangedAttack(attackBns, lbl_ammoCount, i_numDice=numDmgDice, i_diceSides=sidesDmgDice))
    lbl_weaponName = Label(master=frm_weapon, text=i_weaponName)
    
    lbl_weaponName.pack(side=LEFT)
    btn_attackBns.pack(side=LEFT)
    btn_dmg.pack(side=LEFT)

    if i_ammoCount > -1:
        lbl_ammoCount = Label(master=frm_weapon, text=i_ammoCount)
        lbl_ammoCount.pack(side=LEFT)

    frm_weapon.pack()


def saveStats():
    global stats
    global modNames
    global skillNames
    global wnd_stats

    count = 0
    for child in wnd_stats.winfo_children():
        if type(child) is Entry:
            stats[count] = int(child.get())
            count+=1

    updateStats(stats, modNames, skillNames)

    wnd_stats.destroy()

def saveEditedWeapon(window, weaponName):
    weapon_info = []
    dmgDice = ""

    for child in frm_attacks.winfo_children():
        for grandchild in child.winfo_children():
            if type(grandchild) is Label:
                if grandchild["text"] == weaponName:
                    child.destroy()

    for child in window.winfo_children():
        if type(child) is Entry:
            weapon_info.append(child.get())

    tmp = ""

    for i in range(1, len(weapon_info)):
        if i < 3:
            if weaponName is not None:
                # How to save when editing an existing
                if i == 1:
                    dmgDice = weapon_info[i]
                    dmgDice += "d"
                else:
                    dmgDice += weapon_info[i]
            else:
                if i == 1:
                    tmp = weapon_info[i]
                else:
                    dmgDice += weapon_info[i]
                    dmgDice += "d"
                    dmgDice += tmp
        elif i == 6:
            if weapon_info[i] == "":
                weapon_info[i] = -1
            else:
                try:
                    weapon_info[i] = int(weapon_info[i])
                except:
                    return
        else:
            try:
                weapon_info[i] = int(weapon_info[i])
            except:
                if weapon_info[i] == "":
                    weapon_info[i] = 0
                else:
                    return
        
            if i == 5:
                if weapon_info[i] > 1 or weapon_info[i] < 0:
                    return

    addWeapon(weapon_info[0], dmgDice, weapon_info[3], weapon_info[4], weapon_info[5], weapon_info[6])

    window.destroy()
            

    wnd_weapon = Toplevel()

    lbl_weaponName = Label(master=wnd_weapon, text="Weapon name:")
    lbl_weaponNumDice = Label(master=wnd_weapon, text="Number of dice:")
    lbl_weaponDamageDice = Label(master=wnd_weapon, text="Damage dice:")
    lbl_weaponAttackBns = Label(master=wnd_weapon, text="Attack bonus:")
    lbl_weaponDmgBns = Label(master=wnd_weapon, text="Damage bonus:")
    lbl_weaponDex = Label(master=wnd_weapon, text="Dex weapon? (0|1):")
    lbl_ammoCount = Label(master=wnd_weapon, text="Ammo count:")
    
    ent_weaponName = Entry(master=wnd_weapon)
    ent_weaponNumDice = Entry(master=wnd_weapon)
    ent_weaponDamageDice = Entry(master=wnd_weapon)
    ent_weaponAttackBns = Entry(master=wnd_weapon)
    ent_weaponDmgBns = Entry(master=wnd_weapon)
    ent_weaponDex = Entry(master=wnd_weapon)
    ent_ammoCount = Entry(master=wnd_weapon)

    btn_save = Button(master=wnd_weapon, text="Save", command=lambda : saveWeapon(wnd_weapon))

    lbl_weaponName.grid(row=0, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponNumDice.grid(row=1, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponDamageDice.grid(row=2, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponAttackBns.grid(row=3, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponDmgBns.grid(row=4, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponDex.grid(row=5, column=0, sticky="e", padx=1, pady=1)
    lbl_ammoCount.grid(row=6, column=0, sticky="e", padx=1, pady=1)

    ent_weaponName.grid(row=0, column=1, sticky="w", padx=1, pady=1)
    ent_weaponDamageDice.grid(row=1, column=1, sticky="w", padx=1, pady=1)
    ent_weaponNumDice.grid(row=2, column=1, sticky="w", padx=1, pady=1)
    ent_weaponAttackBns.grid(row=3, column=1, sticky="w", padx=1, pady=1)
    ent_weaponDmgBns.grid(row=4, column=1, sticky="w", padx=1, pady=1)
    ent_weaponDex.grid(row=5, column=1, sticky="w", padx=1, pady=1)
    ent_ammoCount.grid(row=6, column=1, sticky="w", padx=1, pady=1)

    btn_save.grid(row=7, column=0, columnspan=2, sticky="snew", pady=1)

def setWeaponEditWindow(window, weaponInfo):
    count = 0
    mini = 0
    for child in window.winfo_children():
        if type(child) is Entry:
            child.delete(0, END)
            if count == 1:
                child.insert(0, weaponInfo[count].split("d")[mini])
                mini += 1
                if mini == 2:
                    count += 1
            else:
                child.insert(0, weaponInfo[count])
                count += 1


def buildWeaponEditWindow():
    global weaponList

    wnd_weapon = Toplevel()

    weaponVar = StringVar()
    weapons = {}
    for weapon in weaponList:
        weapons[weapon[0]] = weapon

    cmb_weapons = Combobox(master=wnd_weapon, textvariable=weaponVar)
    cmb_weapons["values"] = getWeapons()
    cmb_weapons.bind("<<ComboboxSelected>>", lambda event : setWeaponEditWindow(wnd_weapon, weapons[weaponVar.get()]))

    lbl_weaponName = Label(master=wnd_weapon, text="Weapon name:")
    lbl_weaponNumDice = Label(master=wnd_weapon, text="Number of dice:")
    lbl_weaponDamageDice = Label(master=wnd_weapon, text="Damage dice:")
    lbl_weaponAttackBns = Label(master=wnd_weapon, text="Attack bonus:")
    lbl_weaponDmgBns = Label(master=wnd_weapon, text="Damage bonus:")
    lbl_weaponDex = Label(master=wnd_weapon, text="Dex weapon? (0|1):")
    lbl_ammoCount = Label(master=wnd_weapon, text="Ammo count:")
    
    ent_weaponName = Entry(master=wnd_weapon)
    ent_weaponNumDice = Entry(master=wnd_weapon)
    ent_weaponDamageDice = Entry(master=wnd_weapon)
    ent_weaponAttackBns = Entry(master=wnd_weapon)
    ent_weaponDmgBns = Entry(master=wnd_weapon)
    ent_weaponDex = Entry(master=wnd_weapon)
    ent_ammoCount = Entry(master=wnd_weapon)

    btn_save = Button(master=wnd_weapon, text="Save", command=lambda : saveEditedWeapon(wnd_weapon, weaponVar.get()))

    lbl_weaponName.grid(row=0, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponNumDice.grid(row=1, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponDamageDice.grid(row=2, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponAttackBns.grid(row=3, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponDmgBns.grid(row=4, column=0, sticky="e", padx=1, pady=1)
    lbl_weaponDex.grid(row=5, column=0, sticky="e", padx=1, pady=1)
    lbl_ammoCount.grid(row=6, column=0, sticky="e", padx=1, pady=1)

    ent_weaponName.grid(row=0, column=1, sticky="w", padx=1, pady=1)
    ent_weaponDamageDice.grid(row=1, column=1, sticky="w", padx=1, pady=1)
    ent_weaponNumDice.grid(row=2, column=1, sticky="w", padx=1, pady=1)
    ent_weaponAttackBns.grid(row=3, column=1, sticky="w", padx=1, pady=1)
    ent_weaponDmgBns.grid(row=4, column=1, sticky="w", padx=1, pady=1)
    ent_weaponDex.grid(row=5, column=1, sticky="w", padx=1, pady=1)
    ent_ammoCount.grid(row=6, column=1, sticky="w", padx=1, pady=1)

    btn_save.grid(row=7, column=0, columnspan=2, sticky="snew", pady=1)
    cmb_weapons.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)


def buildStatsWindow(i_window, i_stats):
    m_lbl_str = Label(master=i_window, text="Strength")
    m_ent_str = Entry(master=i_window)
    m_ent_str.insert("0", i_stats[0])

    m_lbl_dex = Label(master=i_window, text="Dexterity")
    m_ent_dex = Entry(master=i_window)
    m_ent_dex.insert("0", i_stats[1])

    m_lbl_con = Label(master=i_window, text="Constitution")
    m_ent_con = Entry(master=i_window)
    m_ent_con.insert("0", i_stats[2])

    m_lbl_int = Label(master=i_window, text="Intelligence")
    m_ent_int = Entry(master=i_window)
    m_ent_int.insert("0", i_stats[3])

    m_lbl_wis = Label(master=i_window, text="Wisdom")
    m_ent_wis = Entry(master=i_window)
    m_ent_wis.insert("0", i_stats[4])

    m_lbl_cha = Label(master=i_window, text="Charisma")
    m_ent_cha = Entry(master=i_window)
    m_ent_cha.insert("0", i_stats[5])

    btn_save = Button(master=i_window, text="Save & Exit", command=saveStats)
    
        
    m_lbl_str.grid(row=0, column=0, sticky="e")
    m_ent_str.grid(row=0, column=1, sticky="w")

    m_lbl_dex.grid(row=1, column=0, sticky="e")
    m_ent_dex.grid(row=1, column=1, sticky="w")

    m_lbl_con.grid(row=2, column=0, sticky="e")
    m_ent_con.grid(row=2, column=1, sticky="w")

    m_lbl_int.grid(row=3, column=0, sticky="e")
    m_ent_int.grid(row=3, column=1, sticky="w")

    m_lbl_wis.grid(row=4, column=0, sticky="e")
    m_ent_wis.grid(row=4, column=1, sticky="w")

    m_lbl_cha.grid(row=5, column=0, sticky="e")
    m_ent_cha.grid(row=5, column=1, sticky="w")

    btn_save.grid(row=6, column=0, columnspan=2, sticky="nswe")

def editStats(event):
    global wnd_stats
    global stats

    wnd_stats = Toplevel(window)
    buildStatsWindow(wnd_stats, stats)


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


### Building the window

## Declaring all of the frames

# General frame splitting & assigning to larger frames
frm_charInfo = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Character info")
# frm_charAppear = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Appearance")

n_actions = Notebook(master=window)

frm_skills = Frame(master=window, relief=RAISED, borderwidth=5)
frm_profs = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Profs")

frm_combatInfo = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Stats")
frm_equipment = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Inventory")

frm_personality = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Personality")
frm_features = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Features/Traits")

frm_attackInfo = LabelFrame(master=n_actions, relief=RAISED, borderwidth=5, text="Attack Info")
frm_spells = LabelFrame(master=n_actions, relief=RAISED, borderwidth=5, text="Spells")

# Smallest frames (where necessary) & assigning to general frames
frm_stats = Frame(master=frm_skills, relief=RIDGE, borderwidth=5)
frm_savingThrows = LabelFrame(master=frm_skills, relief=RIDGE, borderwidth=5, text="Saving Throws")
frm_statSkills = LabelFrame(master=frm_skills, relief=RIDGE, borderwidth=5, text="Skills")

frm_attacks = LabelFrame(master=frm_attackInfo, relief=RAISED, borderwidth=5, text="Attacks")
frm_abilities = LabelFrame(master=frm_attackInfo, relief=RAISED, borderwidth=5, text="Abilities")

frm_spellInfo = LabelFrame(master=frm_spells, relief=RAISED, borderwidth=5, text="Spell Info")
frm_loSpells = LabelFrame(master=frm_spells, relief=RAISED, borderwidth=5, text="Lo")
frm_medSpells = LabelFrame(master=frm_spells, relief=RAISED, borderwidth=5, text="Mid")
frm_hiSpells = LabelFrame(master=frm_spells, relief=RAISED, borderwidth=5, text="Hi")

n_actions.add(frm_attackInfo, text="Attacks")
n_actions.add(frm_spells, text="Spells")

# Setting the frames onto the window
for row in range(3):
    window.rowconfigure(row, weight=1, minsize=50)
for col in range(3):
    window.columnconfigure(col, weight=1, minsize=50)

frm_charInfo.grid(row=0, column=0, sticky="nwe", padx=5, pady=2)
# frm_charAppear.grid(row=0, column=0, sticky="swe", padx=5, pady=2)
frm_combatInfo.grid(row=0, column=1, sticky="nswe", padx=5, pady=2)
frm_personality.grid(row=0, column=2, sticky="nswe", padx=5, pady=2)

frm_skills.grid(row=1, column=0, sticky="nswe", padx=5, pady=2)
frm_equipment.grid(row=1, column=1, sticky="swe", padx=5, pady=2)
frm_profs.grid(row=1, column=2, sticky="nsw", padx=5, pady=2)
frm_features.grid(row=1, column=2, sticky="nse", padx=5, pady=2)

n_actions.grid(row=2, column=0, columnspan=3, sticky="nswe", padx=5, pady=2)

frm_stats.pack(fill=Y, side=LEFT, expand=True, padx=5, pady=2)
frm_savingThrows.pack(fill=BOTH, side=RIGHT, expand=True, padx=5, pady=2)
frm_statSkills.pack(fill=BOTH, side=RIGHT, expand=True, padx=5, pady=2)

## Populating the Character info section
btn_refresh = Button(master=frm_charInfo, text="Refresh Stats", command=refreshStats)

lbl_charName = Label(master=frm_charInfo, text="Name:")
lbl_charClass = Label(master=frm_charInfo, text="Class:")
lbl_charLevel = Label(master=frm_charInfo, text="Level:")
lbl_charBg = Label(master=frm_charInfo, text="Bg:")
lbl_charRace = Label(master=frm_charInfo, text="Race:")
lbl_charAlign = Label(master=frm_charInfo, text="Align:")
lbl_charExp = Label(master=frm_charInfo, text="Exp:")

ent_charName = Entry(master=frm_charInfo)
ent_charClass = Entry(master=frm_charInfo)
ent_charLevel = Entry(master=frm_charInfo)
ent_charBg = Entry(master=frm_charInfo)
ent_charRace = Entry(master=frm_charInfo)
ent_charAlign = Entry(master=frm_charInfo)
ent_charExp = Entry(master=frm_charInfo)

# Setting the frames onto the window
for row in range(6):
    frm_charInfo.rowconfigure(row, weight=1, minsize=50)
for col in range(3):
    frm_charInfo.columnconfigure(col, weight=1, minsize=50)

btn_refresh.grid(row=0, column=2, sticky="ew", pady=1, padx=5)
lbl_charName.grid(row=0, column=0, sticky="e", pady=1)
ent_charName.grid(row=0, column=1, sticky="ew", padx=1, pady=1)

lbl_charClass.grid(row=1, column=0, sticky="e", pady=1)
ent_charClass.grid(row=1, column=1, sticky="ew", padx=1, pady=1)

lbl_charLevel.grid(row=1, column=2, sticky="e", pady=1)
ent_charLevel.grid(row=1, column=3, sticky="ew", padx=1, pady=1)

lbl_charRace.grid(row=1, column=4, sticky="e", pady=1)
ent_charRace.grid(row=1, column=5, sticky="ew", padx=1, pady=1)

lbl_charBg.grid(row=2, column=0, sticky="e", pady=1)
ent_charBg.grid(row=2, column=1, sticky="ew", padx=1, pady=1)

lbl_charAlign.grid(row=2, column=2, sticky="e", pady=1)
ent_charAlign.grid(row=2, column=3, sticky="ew", padx=1, pady=1)

lbl_charExp.grid(row=2, column=4, sticky="e", pady=1)
ent_charExp.grid(row=2, column=5, sticky="ew", padx=1, pady=1)

## Populating the Spell info section
lbl_spellClass = Label(master=frm_spellInfo, text="Spellcasting Class:")
lbl_spellAbility = Label(master=frm_spellInfo, text="Spellcasting Ability:")
lbl_spellSave = Label(master=frm_spellInfo, text="Spell Save DC:")
lbl_spellAttack = Label(master=frm_spellInfo, text="Spell Attack Bonus:")

ent_spellClass = Entry(master=frm_spellInfo)
ent_spellAbility = Entry(master=frm_spellInfo)
ent_spellSave = Entry(master=frm_spellInfo)
ent_spellAttack = Entry(master=frm_spellInfo)

# Setting the frames onto the window
frm_spellInfo.rowconfigure(0, weight=1, minsize=50)
for col in range(8):
    frm_spellInfo.columnconfigure(col, weight=1, minsize=50)

lbl_spellClass.grid(row=0, column=0, sticky="e", pady=1)
ent_spellClass.grid(row=0, column=1, sticky="ew", padx=1, pady=1)

lbl_spellAbility.grid(row=0, column=2, sticky="e", pady=1)
ent_spellAbility.grid(row=0, column=3, sticky="ew", padx=1, pady=1)

lbl_spellSave.grid(row=0, column=4, sticky="e", pady=1)
ent_spellSave.grid(row=0, column=5, sticky="ew", padx=1, pady=1)

lbl_spellAttack.grid(row=0, column=6, sticky="e", pady=1)
ent_spellAttack.grid(row=0, column=7, sticky="ew", padx=1, pady=1)

## Populating Character appearance
# lbl_charAge = Label(master=frm_charAppear, text="Age:")
# lbl_charHeight = Label(master=frm_charAppear, text="Height:")
# lbl_charWeight = Label(master=frm_charAppear, text="Weight:")
# lbl_charEyes = Label(master=frm_charAppear, text="Eyes:")
# lbl_charSkin = Label(master=frm_charAppear, text="Skin:")
# lbl_charHair = Label(master=frm_charAppear, text="Hair:")

# ent_charAge = Entry(master=frm_charAppear)
# ent_charHeight = Entry(master=frm_charAppear)
# ent_charWeight = Entry(master=frm_charAppear)
# ent_charEyes = Entry(master=frm_charAppear)
# ent_charSkin = Entry(master=frm_charAppear)
# ent_charHair = Entry(master=frm_charAppear)

# # Setting the frames onto the window
# for row in range(3):
#     frm_charAppear.rowconfigure(row, weight=1, minsize=50)
# for col in range(6):
#     frm_charAppear.columnconfigure(col, weight=1, minsize=50)

# lbl_charAge.grid(row=1, column=0, sticky="e", pady=1)
# ent_charAge.grid(row=1, column=1, sticky="ew", padx=1, pady=1)

# lbl_charHeight.grid(row=1, column=2, sticky="e", pady=1)
# ent_charHeight.grid(row=1, column=3, sticky="ew", padx=1, pady=1)

# lbl_charWeight.grid(row=1, column=4, sticky="e", pady=1)
# ent_charWeight.grid(row=1, column=5, sticky="ew", padx=1, pady=1)

# lbl_charEyes.grid(row=2, column=0, sticky="e", pady=1)
# ent_charEyes.grid(row=2, column=1, sticky="ew", padx=1, pady=1)

# lbl_charSkin.grid(row=2, column=2, sticky="e", pady=1)
# ent_charSkin.grid(row=2, column=3, sticky="ew", padx=1, pady=1)

# lbl_charHair.grid(row=2, column=4, sticky="e", pady=1)
# ent_charHair.grid(row=2, column=5, sticky="ew", padx=1, pady=1)

## Populating Combat info
lbl_ac = Label(master=frm_combatInfo, text="AC")
lbl_init = Label(master=frm_combatInfo, text="Initiative")
lbl_speed = Label(master=frm_combatInfo, text="Speed")
lbl_maxHp = Label(master=frm_combatInfo, text="Max HP")
lbl_hp = Label(master=frm_combatInfo, text="HP")
lbl_tmpHp = Label(master=frm_combatInfo, text="Temp HP")
lbl_ttlHitDice = Label(master=frm_combatInfo, text="Total Hit Dice")
lbl_hitDice = Label(master=frm_combatInfo, text="Hit Dice")
frm_ds = LabelFrame(master=frm_combatInfo, text="Death Saves")

ent_ac = Entry(master=frm_combatInfo)
ent_init = Entry(master=frm_combatInfo)
ent_speed = Entry(master=frm_combatInfo)
ent_maxHp = Entry(master=frm_combatInfo)
ent_hp = Entry(master=frm_combatInfo)
ent_tmpHp = Entry(master=frm_combatInfo)
ent_ttlHitDice = Entry(master=frm_combatInfo)
ent_hitDice = Entry(master=frm_combatInfo)

chk_dsFail1 = Checkbutton(master=frm_ds, text="F", variable=chkBoxStartVal)
chk_dsFail2 = Checkbutton(master=frm_ds, text="F", variable=chkBoxStartVal)
chk_dsFail3 = Checkbutton(master=frm_ds, text="F", variable=chkBoxStartVal)
chk_dsSucc1 = Checkbutton(master=frm_ds, text="S", variable=chkBoxStartVal)
chk_dsSucc2 = Checkbutton(master=frm_ds, text="S", variable=chkBoxStartVal)
chk_dsSucc3 = Checkbutton(master=frm_ds, text="S", variable=chkBoxStartVal)

# Setting the frames onto the window
for row in range(4):
    frm_combatInfo.rowconfigure(row, weight=1, minsize=50)
for col in range(3):
    frm_combatInfo.columnconfigure(col, weight=1, minsize=50)

lbl_ac.grid(row=1, column=0, sticky="swe", pady=1)
ent_ac.grid(row=1, column=0, sticky="new", padx=1, pady=1)

lbl_init.grid(row=1, column=1, sticky="swe", pady=1)
ent_init.grid(row=1, column=1, sticky="new", padx=1, pady=1)

lbl_speed.grid(row=1, column=2, sticky="swe", pady=1)
ent_speed.grid(row=1, column=2, sticky="new", padx=1, pady=1)

lbl_maxHp.grid(row=2, column=0, sticky="swe", pady=1)
ent_maxHp.grid(row=2, column=0, sticky="new", padx=1, pady=1)

lbl_hp.grid(row=2, column=1, sticky="swe", pady=1)
ent_hp.grid(row=2, column=1, sticky="new", padx=1, pady=1)

lbl_tmpHp.grid(row=2, column=2, sticky="swe", pady=1)
ent_tmpHp.grid(row=2, column=2, sticky="new", padx=1, pady=1)

lbl_ttlHitDice.grid(row=3, column=0, sticky="swe", padx=1, pady=1)
ent_ttlHitDice.grid(row=3, column=0, sticky="new", padx=1, pady=1)

lbl_hitDice.grid(row=3, column=1, sticky="swe", padx=1, pady=1)
ent_hitDice.grid(row=3, column=1, sticky="new", padx=1, pady=1)

frm_ds.grid(row=4, column=0, columnspan=2, sticky="sne", padx=1, pady=1)

chk_dsFail1.grid(row=4, column=1, padx=1, pady=1)
chk_dsFail2.grid(row=4, column=2, padx=1, pady=1)
chk_dsFail3.grid(row=4, column=3, padx=1, pady=1)

chk_dsSucc1.grid(row=4, column=4, padx=1, pady=1)
chk_dsSucc2.grid(row=4, column=5, padx=1, pady=1)
chk_dsSucc3.grid(row=4, column=6, padx=1, pady=1)


## Populating Personality
txt_personTraits = Text(master=frm_personality, width=65, height=20)

# Setting the frames onto the window
txt_personTraits.pack(fill=BOTH, padx=1, pady=1)

## Populating Features & Traits
txt_featuresTraits = Text(master=frm_features, width=30, height=25)

# Setting the frames onto the window
txt_featuresTraits.pack(fill=BOTH, padx=1, pady=1)

## Populating Proficiencies
lbl_langProf = Label(master=frm_profs, text="Languages")
lbl_armorProf = Label(master=frm_profs, text="Armor")
lbl_weaponsProf = Label(master=frm_profs, text="Weapons")
lbl_toolProf = Label(master=frm_profs, text="Tools")
lbl_miscProf = Label(master=frm_profs, text="Misc")

ent_langProf = Entry(master=frm_profs)
ent_armorProf = Entry(master=frm_profs)
ent_weaponsProf = Entry(master=frm_profs)
ent_toolProf = Entry(master=frm_profs)
txt_miscProf = Text(master=frm_profs, width=30, height=17)

ent_langProf.insert(0, "Common, ")

# Setting the frames onto the window
for col in range(2):
    frm_profs.columnconfigure(col, weight=1, minsize=50)
for row in range(5):
    frm_profs.rowconfigure(row, weight=1, minsize=50)

lbl_langProf.grid(row=1, column=0, sticky="nse", padx=1, pady=1)
ent_langProf.grid(row=1, column=1, sticky="nsw", padx=1, pady=1)

lbl_armorProf.grid(row=2, column=0, sticky="nse", padx=1, pady=1)
ent_armorProf.grid(row=2, column=1, sticky="nsw", padx=1, pady=1)

lbl_weaponsProf.grid(row=2, column=0, sticky="nse", padx=1, pady=1)
ent_weaponsProf.grid(row=2, column=1, sticky="nsw", padx=1, pady=1)

lbl_toolProf.grid(row=3, column=0, sticky="nse", padx=1, pady=1)
ent_toolProf.grid(row=3, column=1, sticky="nsw", padx=1, pady=1)

lbl_miscProf.grid(row=4, column=0, sticky="nse", padx=1, pady=1)
txt_miscProf.grid(row=4, column=1, sticky="nsw", padx=1, pady=1)

## Populating Attack info
btn_editWeapons = Button(master=frm_attackInfo, text="Edit Weapons", command=buildWeaponEditWindow)
btn_editWeapons.pack(expand=True)

txt_abilities = Text(master=frm_abilities, width=50, height=20)
txt_abilities.pack(expand=True, padx=1, pady=1)

frm_attacks.pack(side=LEFT, fill=BOTH, padx=5, pady=2)
frm_abilities.pack(side=RIGHT, fill=BOTH, padx=5, pady=2)

## Populating Equipment
frm_cp = LabelFrame(master=frm_equipment, text="cp")
ent_cp = Entry(master=frm_cp)
frm_sp = LabelFrame(master=frm_equipment, text="sp")
ent_sp = Entry(master=frm_sp)
frm_ep = LabelFrame(master=frm_equipment, text="ep")
ent_ep = Entry(master=frm_ep)
frm_gp = LabelFrame(master=frm_equipment, text="gp")
ent_gp = Entry(master=frm_gp)
frm_pp = LabelFrame(master=frm_equipment, text="pp")
ent_pp = Entry(master=frm_pp)

txt_equipment = Text(master=frm_equipment, width=30, height=30)

# Setting the frames onto the window
ent_cp.pack()
ent_sp.pack()
ent_ep.pack()
ent_gp.pack()
ent_pp.pack()

frm_cp.pack()
frm_sp.pack()
frm_ep.pack()
frm_gp.pack()
frm_pp.pack()

txt_equipment.pack(fill=BOTH, padx=1, pady=1)


## Populating Spells
frm_spellInfo.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=2)
frm_loSpells.grid(row=1, column=0, sticky="nswe", padx=5, pady=2)
frm_medSpells.grid(row=1, column=1, sticky="nswe", padx=5, pady=2)
frm_hiSpells.grid(row=1, column=2, sticky="nswe", padx=5, pady=2)

frm_cantrips = LabelFrame(master=frm_loSpells, relief=RIDGE, borderwidth=5, text="Cantrips")
frm_1lvl = LabelFrame(master=frm_loSpells, relief=RIDGE, borderwidth=5, text="1st Level")
frm_2lvl = LabelFrame(master=frm_loSpells, relief=RIDGE, borderwidth=5, text="2nd Level")

frm_3lvl = LabelFrame(master=frm_medSpells, relief=RIDGE, borderwidth=5, text="3rd Level")
frm_4lvl = LabelFrame(master=frm_medSpells, relief=RIDGE, borderwidth=5, text="4th Level")
frm_5lvl = LabelFrame(master=frm_medSpells, relief=RIDGE, borderwidth=5, text="5th Level")

frm_6lvl = LabelFrame(master=frm_hiSpells, relief=RIDGE, borderwidth=5, text="6th Level")
frm_7lvl = LabelFrame(master=frm_hiSpells, relief=RIDGE, borderwidth=5, text="7th Level")
frm_8lvl = LabelFrame(master=frm_hiSpells, relief=RIDGE, borderwidth=5, text="8th Level")
frm_9lvl = LabelFrame(master=frm_hiSpells, relief=RIDGE, borderwidth=5, text="9th Level")

lbl_cantripInfo = Label(master=frm_cantrips, text="X")
lbl_1lvlInfo = Label(master=frm_1lvl, text=" N/X")
lbl_2lvlInfo = Label(master=frm_2lvl, text=" N/X")
lbl_3lvlInfo = Label(master=frm_3lvl, text=" N/X")
lbl_4lvlInfo = Label(master=frm_4lvl, text=" N/X")
lbl_5lvlInfo = Label(master=frm_5lvl, text=" N/X")
lbl_6lvlInfo = Label(master=frm_6lvl, text=" N/X")
lbl_7lvlInfo = Label(master=frm_7lvl, text=" N/X")
lbl_8lvlInfo = Label(master=frm_8lvl, text=" N/X")
lbl_9lvlInfo = Label(master=frm_9lvl, text=" N/X")


frm_cantrips.pack()
frm_1lvl.pack()
frm_2lvl.pack()

frm_3lvl.pack()
frm_4lvl.pack()
frm_5lvl.pack()

frm_6lvl.pack()
frm_7lvl.pack()
frm_8lvl.pack()
frm_9lvl.pack()

lbl_cantripInfo.pack()
lbl_1lvlInfo.pack()
lbl_2lvlInfo.pack()
lbl_3lvlInfo.pack()
lbl_4lvlInfo.pack()
lbl_5lvlInfo.pack()
lbl_6lvlInfo.pack()
lbl_7lvlInfo.pack()
lbl_8lvlInfo.pack()
lbl_9lvlInfo.pack()

## Populating stats
btn_edit_stats = Button(master=frm_skills, text="Edit")
btn_edit_stats.pack()

updateStats(stats, modNames, skillNames)

wnd_stats = None

btn_edit_stats.bind("<Button-1>", editStats)

window.mainloop()