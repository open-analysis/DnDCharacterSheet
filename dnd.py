from tkinter import *
from tkinter.ttk import *
from builder import *

window = Tk()

## Declaring all of the frames

# General frame splitting & assigning to larger frames
frm_charInfo = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Character info")
frm_charAppear = LabelFrame(master=window, relief=RAISED, borderwidth=5, text="Appearance")

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
frm_combatInfo.grid(row=0, column=1, sticky="nswe", padx=5, pady=2)
frm_charAppear.grid(row=0, column=0, sticky="swe", padx=5, pady=2)
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
lbl_charAge = Label(master=frm_charAppear, text="Age:")
lbl_charHeight = Label(master=frm_charAppear, text="Height:")
lbl_charWeight = Label(master=frm_charAppear, text="Weight:")
lbl_charEyes = Label(master=frm_charAppear, text="Eyes:")
lbl_charSkin = Label(master=frm_charAppear, text="Skin:")
lbl_charHair = Label(master=frm_charAppear, text="Hair:")

ent_charAge = Entry(master=frm_charAppear)
ent_charHeight = Entry(master=frm_charAppear)
ent_charWeight = Entry(master=frm_charAppear)
ent_charEyes = Entry(master=frm_charAppear)
ent_charSkin = Entry(master=frm_charAppear)
ent_charHair = Entry(master=frm_charAppear)

# Setting the frames onto the window
for row in range(3):
    frm_charAppear.rowconfigure(row, weight=1, minsize=50)
for col in range(6):
    frm_charAppear.columnconfigure(col, weight=1, minsize=50)

lbl_charAge.grid(row=1, column=0, sticky="e", pady=1)
ent_charAge.grid(row=1, column=1, sticky="ew", padx=1, pady=1)

lbl_charHeight.grid(row=1, column=2, sticky="e", pady=1)
ent_charHeight.grid(row=1, column=3, sticky="ew", padx=1, pady=1)

lbl_charWeight.grid(row=1, column=4, sticky="e", pady=1)
ent_charWeight.grid(row=1, column=5, sticky="ew", padx=1, pady=1)

lbl_charEyes.grid(row=2, column=0, sticky="e", pady=1)
ent_charEyes.grid(row=2, column=1, sticky="ew", padx=1, pady=1)

lbl_charSkin.grid(row=2, column=2, sticky="e", pady=1)
ent_charSkin.grid(row=2, column=3, sticky="ew", padx=1, pady=1)

lbl_charHair.grid(row=2, column=4, sticky="e", pady=1)
ent_charHair.grid(row=2, column=5, sticky="ew", padx=1, pady=1)

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
chk_dsFail1 = Checkbutton(master=frm_ds, text="F")
chk_dsFail2 = Checkbutton(master=frm_ds, text="F")
chk_dsFail3 = Checkbutton(master=frm_ds, text="F")
chk_dsSucc1 = Checkbutton(master=frm_ds, text="S")
chk_dsSucc2 = Checkbutton(master=frm_ds, text="S")
chk_dsSucc3 = Checkbutton(master=frm_ds, text="S")

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
addAttack(frm_attacks, "Axe", "+4", "+2")

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

addStat(frm_stats, "Strength", "10")
addStat(frm_stats, "Dexterity", "10")
addStat(frm_stats, "Constitution", "10")
addStat(frm_stats, "Intelligence", "10")
addStat(frm_stats, "Wisdom", "10")
addStat(frm_stats, "Charisma", "10")

## Populating Skills
strMod = getModifierFromStat(frm_stats, "Strength")
dexMod = getModifierFromStat(frm_stats, "Dexterity")
conMod = getModifierFromStat(frm_stats, "Constitution")
intMod = getModifierFromStat(frm_stats, "Intelligence")
wisMod = getModifierFromStat(frm_stats, "Wisdom")
chaMod = getModifierFromStat(frm_stats, "Charisma")

addSkill(frm_savingThrows, "Strength", strMod)
addSkill(frm_savingThrows, "Dexerity", dexMod)
addSkill(frm_savingThrows, "Constitution", conMod)
addSkill(frm_savingThrows, "Intelligence", intMod)
addSkill(frm_savingThrows, "Wisdome", wisMod)
addSkill(frm_savingThrows, "Charisma", chaMod)

addSkill(frm_statSkills, "Acrobatics", dexMod)
addSkill(frm_statSkills, "Animal Handling", wisMod)
addSkill(frm_statSkills, "Arcana", intMod)
addSkill(frm_statSkills, "Athletics", strMod)
addSkill(frm_statSkills, "Deceoption", chaMod)
addSkill(frm_statSkills, "History", intMod)
addSkill(frm_statSkills, "Insight", wisMod)
addSkill(frm_statSkills, "Intimidation", chaMod)
addSkill(frm_statSkills, "Investigation", intMod)
addSkill(frm_statSkills, "Medicine", wisMod)
addSkill(frm_statSkills, "Nature", intMod)
addSkill(frm_statSkills, "Perception", wisMod)
addSkill(frm_statSkills, "Performance", chaMod)
addSkill(frm_statSkills, "Persuasion", chaMod)
addSkill(frm_statSkills, "Religion", intMod)
addSkill(frm_statSkills, "Sleight of Hand", dexMod)
addSkill(frm_statSkills, "Stealth", dexMod)
addSkill(frm_statSkills, "Survival", wisMod)


def saveStats():
    global strMod
    global dexMod
    global conMod
    global intMod
    global wisMod
    global chaMod

    window = wnd_stats

    count = 0
    for child in window.winfo_children():
        if type(child) is Entry:
            if count == 0:
                strMod = int(child.get())
                count+=1
            elif count == 1:
                dexMod = int(child.get())
                count+=1
            elif count == 2:
                conMod = int(child.get())
                count+=1
            elif count == 3:
                intMod = int(child.get())
                count+=1
            elif count == 4:
                wisMod = int(child.get())
                count+=1
            elif count == 5:
                charMod = int(child.get())
            else:
                break

    window.destroy()

    pass

def buildWindow(i_window, i_mods):
    m_lbl_str = Label(master=i_window, text="Strength")
    m_ent_str = Entry(master=i_window)
    m_ent_str.insert("0", i_mods[0])

    m_lbl_dex = Label(master=i_window, text="Dexterity")
    m_ent_dex = Entry(master=i_window)
    m_ent_dex.insert("0", i_mods[1])

    m_lbl_con = Label(master=i_window, text="Constitution")
    m_ent_con = Entry(master=i_window)
    m_ent_con.insert("0", i_mods[2])

    m_lbl_int = Label(master=i_window, text="Intelligence")
    m_ent_int = Entry(master=i_window)
    m_ent_int.insert("0", i_mods[3])

    m_lbl_wis = Label(master=i_window, text="Wisdom")
    m_ent_wis = Entry(master=i_window)
    m_ent_wis.insert("0", i_mods[4])

    m_lbl_cha = Label(master=i_window, text="Charisma")
    m_ent_cha = Entry(master=i_window)
    m_ent_cha.insert("0", i_mods[5])

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

wnd_stats = None

def editStats(event):
    global wnd_stats

    print("Editing stats")
    wnd_stats = Toplevel(window)
    mods = [strMod, dexMod, conMod, intMod, wisMod, chaMod]
    buildWindow(wnd_stats, mods)

btn_edit_stats.bind("<Button-1>", editStats)

window.mainloop()