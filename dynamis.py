#Weapons {"Name": "",  "Jobs":[]}
    #dagger {"Name": "", "Skill Type": "Dagger", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
Oneiros_Knife = {"Name": "Oneiros Knife", "Skill Type": "Dagger", "Type":"Weapon", "DMG":27, "Delay":150, "AGI":6, "Crit Damage":3, "Jobs":["rdm","thf","brd","rng","cor"]}

    #sword {"Name": "", "Skill Type": "Sword", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
Talekeeper = {"Name": "Talekeeper", "Skill Type": "Sword", "Type":"Weapon", "DMG":42, "Delay":224, "HP":30, "MP":30, "STR":5, "Enhancing Magic Duration":5, "Song Duration":5, "Jobs":["war","rdm","pld","brd","drg","cor","dnc"]}
Brilliance = {"Name": "Brilliance", "Skill Type": "Sword", "Type":"Weapon", "DMG":48, "Delay":228, "Cure Potency":15, "Block Chance":5, "Jobs":["war","pld"]}

    #club {"Name": "",  "Skill Type": "Club", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
Moepapa_Mace = {"Name": "Moepapa Mace",  "Skill Type": "Club", "Type":"Weapon", "DMG":45, "Delay":300, "Dark Elemental Resist":30, "MND":8, "Accuracy":8, "Jobs":["war","whm","pld","blu","geo","run"]}
    
    #Katana {"Name": "", "Skill Type": "Katana", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
Mujin_Tanto = {"Name": "Mujin Tanto", "Skill Type": "Katana", "Type":"Weapon", "DMG":38, "Delay":222, "Dubtle Blow":5, "DT":-3, "Enmity":3, "Fast Cast":2, "Jobs":["nin"]}
    
    #axe {"Name": "", "Skill Type": "Axe", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
Tjukurrpa_Axe = {"Name": "Tjukurrpa Axe", "Skill Type": "Axe", "Type":"Weapon", "DMG":46, "Delay":288, "Sic/Ready Delay":-2, "Gear Haste":2, "Pet Haste":2, "Pet Accuracy":5, "Jobs":["bst"]}
   
    #handtohand {"Name": "", "Skill Type": "Hand-to-Hand", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
    
    #gsword  {"Name": "", "Skill Type": "Great Sword", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
Nightfall = {"Name": "Nifhtfall", "Skill Type": "Great Sword", "Type":"Weapon", "DMG":85, "Delay":444, "Regain":10, "Jobs":["war","pld","drk","run"]}
    #gaxe {"Name": "", "Skill Type": "Great Axe", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
Oneiros_Axe = {"Name": "Oneiros Axe", "Skill Type": "Great Axe", "Type":"Weapon", "DMG":96, "Delay":504, "HP":50, "VIT":5, "DT":-5, "Accuracy":5, "Retaliation":5, "Jobs":["war"]}
  
    #gkt  {"Name": "", "Skill Type": "Great Katana", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
    
    #polearm  
Oneiros_Lance = {"Name": "Oneiros Lance", "Skill Type": "Polearm", "Type":"Weapon", "DMG":96, "Delay":492, "HP":50, "VIT":5, "DT":-5, "Enmity":5, "Jobs":["drg"]}
    
    #scythe  {"Name": "", "Skill Type": "Scythe", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
    
    #staff  {"Name": "", "Skill Type": "Staff", "Type":"Weapon", "DMG":, "Delay":,  "Jobs":[]}
Chtonic_Staff = {"Name": "Chtonic Staff", "Skill Type": "Staff", "Type":"Weapon", "DMG":45, "Delay":356, "MDT":-5, "Pet MDT":-5, "Pet Cure Potency":5, "Jobs":all_jobs}    

    
#Grip/Shields {"Name": "",  "Jobs":[]}
Oneiros_Grip = {"Name": "Oneiros Grip", "HP":5, "MP":5, "Regen":1, "Refresh":1, "Jobs":all_jobs}
Reign_Grip = {"Name": "Reign Grip", "MND":3, "CHR":3, "Jobs":all_jobs}

#Ranged Weapons {"Name": "",  "Jobs":[]}
    #archer  {"Name": "", "Skill Type": "Archery", "Type":"Bow", "DMG":, "Delay":,  "Jobs":["rng"]}
Aifes_Bow = {"Name": "Aifes Bow", "Skill Type": "Archery", "Type":"Bow", "DMG":79, "Delay":540, "MP":15, "Ranged Accuracy":12, "Subtle Blow":8, "Ranged Delay":-3, "Jobs":["rdm","rng"]}
    #Crossbow
    
    #Gun

mains = [Oneiros_Knife,Talekeeper,Brilliance,Moepapa_Mace,Mujin_Tanto,Tjukurrpa_Axe,Oneiros_Axe,Oneiros_Lance,Chtonic_Staff,Nightfall]
subs = [Oneiros_Knife,Talekeeper,Brilliance,Moepapa_Mace,Mujin_Tanto,Tjukurrpa_Axe]
grips = [Oneiros_Grip,Reign_Grip]

ranged = [Aifes_Bow]

#Instruments {"Name": "", "Skill Type":"Instrument", "Jobs":[]}
Oneiros_Harp = {"Name": "Oneiros Harp", "Skill Type":"String Instrument", "Regen":1, "Paeon":3, "Jobs":["brd"]}

instruments = [Oneiros_Harp]

#Ammo {"Name": "",  "Jobs":[]}

#Gear Ammo {"Name": "",  "Jobs":[]}
Oneiros_Pebble = {"Name": "Oneiros Pebble", "VIT":3, "Accuracy":3, "Jobs":["war","rdm","pld","bst","sam"]}
Oneiro_Tathlum = {"Name": "Oneiros Tathlum", "Axe Skill":2, "Jobs":["war","drk","bst","rng","run"]}
Oneiros_Cluster = {"Name": "Oneiros Cluster", "Attack":-3, "Gear Haste":1, "Jobs":["thf","bst","rng","dnc","run","cor"]}
Demonry_Core = {"Name": "Demonry Core", "DEX":2, "Pet Accuracy":3, "Jobs":["mnk","rdm","thf","bst","rng","nin","drg","cor","pup","dnc","run"]}
Demonry_Stone = {"Name": "Demonry Stone", "MP":15, "Magic Defense Bonus":1, "Jobs":["war","mnk","rdm","thf","pld","drk","bst","brd","rng","sam","nin","drg","blu","cor","dnc","run"]}
Verthandis_Gem = {"Name": "Verthandis Gem", "HP":30, "CHR":-1, "Dark Elemental Resist":-30, "Jobs":all_jobs}

ammos = [Oneiros_Pebble,Oneiro_Tathlum,Oneiros_Cluster,Demonry_Core,Demonry_Stone,Verthandis_Gem]

#Heads {"Name": "",  "Jobs":[]}
Oneiros_Barbut = {"Name": "Oneiros Barbut", "DEF":30, "VIT":9, "Evasion":-14, "PDT":-5,  "Jobs":["war","pld"]}
Oneiros_Helm = {"Name": "Oneiros Helm", "DEF":28, "DEX":9, "DA":-3, "TA":-3, "Crit Damage":3, "Jobs":["war","thf","pld","drk","bst","brd","drg","run"]}
Oneiros_Headgear = {"Name": "Oneiros Headgear", "DEF":25, "MP":50, "INT":6, "Wind Elemental Resistance":15, "Ice Elemental Resistance":-15, "Magic Accuracy":6, "Wind Elemental Attack":1, "Automaton Magic Accuracy":6, "Automaton Refresh":1, "Jobs":["whm","blm","rdm","brd","smn","pup","sch","geo"]}
Oneiros_Coif = {"Name": "Oneiros Coif", "DEF":23, "STR":4, "Ranged Attack":10, "Snapshot":-3, "Enmity":3, "Jobs":all_jobs}
Khthonios_Mask = {"Name": "Khthonios Mask", "DEF":24, "Attack":14, "Store TP":4, "Gear Haste":4, "Magic Defense Bonus":4, "Jobs":["whm","blm","rdm","brd","smn","sch","geo"]}
Khthonios_Helm = {"Name": "Khthonios Helm", "DEF":29, "HP":14, "STR":7, "INT":7, "Dark Magic Skill":9, "Pet Attack":9, "Pet Accuracy":9, "Jobs":["war","blm","thf","drk","bst","rng","nin","drg","pup","dnc","sch"]}
Leonine_Mask = {"Name": "Leonine Mask", "DEF":28, "STR":3, "AGI":3, "Crit Rate":3, "Jobs":["war","mnk","thf","bst","nin","dnc","run"]}
Acubens_Helm = {"Name": "Acubens Helm", "DEF":28, "Accuracy":-10, "Lightning Elemental Resist":-15, "Water Elemental Resist":15, "Gear Haste":6, "Jobs":["mnk","thf","bst","rng","nin","blu","cor","pup","dnc","run"]}
Nocturnus_Helm = {"Name": "Nocturnus Helm", "DEF":24, "STR":6, "DEX":6, "AGI":6, "Attack":8, "DA":2, "Occasionally Absorbs Physical Damage":5, "Jobs":["war","pld","drk","bst","sam","drg"]}
heads = [Oneiros_Barbut,Oneiros_Helm,Oneiros_Headgear,Oneiros_Coif,Khthonios_Mask,Khthonios_Helm,Leonine_Mask,Acubens_Helm,Nocturnus_Helm]

#Neck {"Name": "",  "Jobs":[]}
Halting_Stole = {"Name": "Halting Stole", "DEX":3, "Jobs":all_jobs}
Oneiros_Torque = {"Name": "Oneiros Torque", "Evasion":5, "PDT":-2, "Jobs":["war","mnk","rdm","thf","pld","drk","bst","brd","sam","nin","drg","blu","cor","pup","dnc","run"]}
Mujin_Necklace = {"Name": "Mujin Necklace", "STR":5, "Zanshin":5, "Jobs":["war","pld","drk","drg"]}
Repelling_Collar = {"Name": "Repelling Collar", "PDT":-1, "MDT":1, "Jobs":all_jobs}
Backlash_Torque = {"Name": "Backlash Torque", "Attack":8, "Counter":1, "Jobs":all_jobs}
Jinx_Ampulla = {"Name": "Jinx Ampulla", "HP":-15, "Magic Crit Rate":1, "Jobs":["whm","blm","rdm","smn","blu","sch","geo"]}
Moepapa_Medal = {"Name": "Moepapa Medal", "DEX":6, "AGI":6, "Wind Elemental Resistance":10, "Lightning Elemental Resist":10, "Jobs":all_jobs}
Moepapa_Pendant = {"Name": "Moepapa Pendant", "INT":8, "Enmity":-5, "Magic Crit Damage":5, "Jobs":["whm","blm","rdm","brd","smn","sch","geo"]}
Tjukurrpa_Medal = {"Name": "Tjukurrpa Medal", "STR":6, "VIT":6, "Fire Elemental Resist":10, "Earth Elemental Resist":10, "Jobs":all_jobs}
Aifes_Medal = {"Name": "Aifes Medal", "INT":6, "MND":6, "Ice Elemental Resist":10, "Water Elemental Resist":10, "Jobs":all_jobs}
Beguiling_Collar = {"Name": "Beguiling Collar", "HP":20, "MP":20, "Enmity":-3, "Jobs":all_jobs}
Portus_Collar = {"Name": "Portus Collar", "Accuracy":2, "DA":2, "Jobs":["war","rdm","thf","pld","drk","bst","brd","rng","sam","nin","blu","cor","pup","dnc","run"]}
necks = [Halting_Stole,Oneiros_Torque,Mujin_Necklace,Repelling_Collar,Backlash_Torque,Jinx_Ampulla,Moepapa_Medal,Moepapa_Pendant,Tjukurrpa_Medal,Aifes_Medal,Beguiling_Collar,Portus_Collar]

#Earrings {"Name": "",  "Jobs":[]}
Choreia_Earring = {"Name": "Choreia Earring", "Step Accuracy":5, "Light Elemental Resistance":10, "Jobs":all_jobs}
Hirudinea_Earring = {"Name": "Hirudinea Earring", "HP":-5, "MP":-5, "Drain Aspir":3, "Jobs":["blm","drk","sch","geo"]}
Pagondas_Earring = {"Name": "Pagondas Earring", "DEF":10, "Jobs":all_jobs}
Oneiros_Earring = {"Name": "Oneiros Earring", "HP":15, "VIT":3, "Cure Recieved":5, "Jobs":["war","thf","pld","drk","brd","rng","sam","nin","drg","cor","pup"]}
Oneiros_Pearl = {"Name": "Oneiros Pearl", "Ranged Attack":3, "Enmity":-2, "Jobs":["rdm","thf","rng","sam","nin","cor"]}
Mujin_Stud = {"Name": "Mujin Stud", "Magic Defense Bonus":2, "Subtle Blow":4, "Jobs":["mnk","whm","rdm","thf","bst","brd","rng","sam","nin","blu","cor","dnc","run"]}

ears = [Choreia_Earring,Hirudinea_Earring,Pagondas_Earring,Oneiros_Earring,Oneiros_Pearl,Mujin_Stud]
ears2 = [Choreia_Earring,Hirudinea_Earring,Pagondas_Earring,Oneiros_Earring,Oneiros_Pearl,Mujin_Stud]

#Body {"Name": "",  "Jobs":[]}
Nocturnus_Mail = {"Name": "Nocturnus Mail", "DEF":49, "STR":10, "DEX":10, "VIT":10, "Accuracy":12, "TA":1, "Occasionally Absorbs Magic Damage":5, "Jobs":["war","pld","drk","bst","sam","drg"]}

bodies = [Nocturnus_Mail]

#Gloves {"Name": "", " "Jobs":[]}
Khthonios_Gloves = {"Name": "Khthonios Gloves", "DEF":23, "AGI":6, "Ranged Attack":8, "Enmity":-3, "Recycle":5, "Jobs":["war","pld","drk","rng","sam","cor"]}
Avesta_Bangles = {"Name": "Avesta Bangles", "Magic Accuracy":6, "Enfeebling Magic Skill":9, "Elemental Magic Skill":9, "Dark Magic Skill":9, "Automaton Magic Skills":9, "Jobs":["mnk","whm","blm","rdm","thf","drk","brd","rng","smn","blu","cor","pup","geo","run"]}
Tjukurrpa_Gauntlets = {"Name": "Tjukurrpa Gauntlets", "DEF":30, "HP":30, "MP":30, "Accuracy":5, "Enmity":3, "PDT":-3, "Jobs":["war","pld","drk","drg"]}

hands = [Khthonios_Gloves,Avesta_Bangles,Tjukurrpa_Gauntlets]

#Ring {"Name": "",  "Jobs":[]}
Corneus_Ring = {"Name": "Corneus Ring", "VIT":6, "Enmity":2, "Jobs":all_jobs}
Oneiros_Annulet = {"Name": "Oneiros Annulet", "AGI":-5, "Accuracy":8, "Jobs":all_jobs}
Karka_Ring = {"Name": "Karka Ring", "MND":6, "Magic Accuracy":1, "Jobs":all_jobs}
Blobnag_Ring = {"Name": "Blobnag Ring", "AGI":6, "Ranged Accuracy":3, "Jobs":all_jobs}
Oneiros_Ring = {"Name": "Oneiros Ring", "Accuracy":3, "DA":3, "Jobs":["war","mnk","thf","bst","brd","rng","sam","nin","drg","cor","pup","dnc"]}
Mujin_Band = {"Name": "Mujin Band", "DEX":4, "Skillchain Bonus":4, "Jobs":all_jobs}
Galdr_Ring = {"Name": "Galdr Ring", "INT":6, "Magic Attack Bonus":1, "Jobs":all_jobs}
Strigoi_Ring = {"Name": "Strigoi Ring", "STR":6, "Attack":3, "Jobs":all_jobs}
Demonry_Ring = {"Name": "Demonry Ring", "Attack":5, "TA Damage":3, "Jobs":["mnk","thf","drk","bst","sam","drg","dnc","run"]}
Veela_Ring = {"Name": "Veela Ring", "CHR":6, "Enmity":-2, "Jobs":all_jobs}
Moepapa_Ring = {"Name": "Moepapa Ring", "AGI":5, "Dagger Skill":3, "Marksmanship Skill":3, "Jobs":all_jobs}
Moepapa_Annulet = {"Name": "Moepapa Annulet", "STR":5, "Great Sword Skill":3, "Great Katana Skill":3, "Jobs":all_jobs}
Zilant_Ring = {"Name": "Zilant Ring", "DEX":6, "Accuracy":3, "Jobs":all_jobs}
Tjukurrpa_Annulet = {"Name": "Tjukurrpa Annulet", "MND":5, "Sword Skill":3, "Club Skill":3, "Jobs":all_jobs}
Tjukurrpa_Ring = {"Name": "Tjukurrpa Ring", "DEX":5, "Axe Skill":3, "Katana Skill":3, "Jobs":all_jobs}
Succor_Ring = {"Name": "Succor Ring", "MP":30, "DT":-3, "Jobs":all_jobs}
Alert_Ring = {"Name": "Alert Ring", "Accuracy":-3, "Evasion":6, "Jobs":all_jobs}
Aifes_Annulet = {"Name": "Aifes Annulet", "INT":5, "Scythe Skill":3, "Staff Skill":3, "Jobs":all_jobs}
Aifes_Ring = {"Name": "Aifes Ring", "STR":5, "Polearm Skill":3, "Archery Skill":3, "Jobs":all_jobs}
Portus_Annulet = {"Name": "Portus Annulet", "Accuracy":6, "Gaurding Skill":3, "Evasion":3, "Shield Skill":3, "Parrying Skill":3, "Jobs":all_jobs};
Portus_Ring = {"Name": "Portus Ring", "VIT":4, "Hand to Hand Skill":4, "Polearm Skill":4, "Jobs":all_jobs}

rings = [Corneus_Ring,Oneiros_Annulet,Karka_Ring,Blobnag_Ring,Oneiros_Ring,Mujin_Band,Galdr_Ring,Strigoi_Ring,Demonry_Ring,Veela_Ring,Moepapa_Ring,Moepapa_Annulet,Zilant_Ring,Tjukurrpa_Annulet,Tjukurrpa_Ring,Succor_Ring,Alert_Ring,Aifes_Annulet,Aifes_Ring,Portus_Annulet,Portus_Ring]
rings2 = [Corneus_Ring,Oneiros_Annulet,Karka_Ring,Blobnag_Ring,Oneiros_Ring,Mujin_Band,Galdr_Ring,Strigoi_Ring,Demonry_Ring,Veela_Ring,Moepapa_Ring,Moepapa_Annulet,Zilant_Ring,Tjukurrpa_Annulet,Tjukurrpa_Ring,Succor_Ring,Alert_Ring,Aifes_Annulet,Aifes_Ring,Portus_Annulet,Portus_Ring]

#Cape {"Name": "",  "Jobs":[]}
Oneiros_Cappa = {"Name": "Oneiros Cappa", "DEF":14, "VIT":5, "Pet PDT":-3, "Jobs":["war","mnk","rdm","thf","pld","drk","bst","brd","rng","sam","nin","drg","blu","cor","pup","dnc","run"]}
Oneiros_Cape = {"Name": "Oneiros Cape", "DEF":5, "Magic Accuracy":4, "Jobs":["whm","blm","rdm","brd","smn","blu","pup","sch","geo"]}
Veela_Cape = {"Name": "Veela Cape", "DEF":5, "MP":10, "Fast Cast":1, "Jobs":["whm","blm","brd","smn","pup","sch","geo"]}
Mujin_Mantle = {"Name": "Mujin Mantle", "DEF":9, "Accuracy":5, "Evasion":5, "Magic Evasion":5, "Jobs":["war","mnk","thf","bst","brd","rng","sam","nin","drg","cor","pup","dnc"]}
Tjukurrpa_Mantle = {"Name": "Tjukurrpa Mantle", "DEF":9, "AGI":3, "Magic Attack Bonus":3, "Enmity":-3, "Jobs":["thf","rng","nin","cor"]}
Aifes_Mantle = {"Name": "Aifes Mantle", "DEF":7, "AGI":4, "Accuracy":4, "Store TP":2, "Pet Attack":10, "Jobs":all_jobs}
Hecates_Cape = {"Name": "Hecates Cape", "DEF":4, "MP":7, "Magic Accuracy":3, "Magic Attack Bonus":3,  "Jobs":["whm","blm","rdm","brd","smn","blu","sch","geo"]}

capes = [Oneiros_Cappa,Oneiros_Cape,Veela_Cape,Mujin_Mantle,Tjukurrpa_Mantle,Aifes_Mantle,Hecates_Cape]

#Belt {"Name": "",  "Jobs":[]}
Oneiros_Rope = {"Name": "Oneiros Rope", "DEF":4, "Store TP":2, "Occult Acumen":20, "Jobs":all_jobs}
Mujin_Obi = {"Name": "Mujin Obi", "DEF":4, "MP":30, "Avatar Attack":10, "Jobs":["whm","blm","rdm","pld","drk","smn","blu","sch","geo","run"]}
Oneiros_Sash = {"Name": "Oneiros Sash", "DEF":5, "HP":20, "MP":20, "Magic Attack Bonus":4, "Conserve MP":4, "Jobs":["whm","blm","rdm","smn","sch","geo"]}
Oneiros_Belt = {"Name": "Oneiros Belt", "DEF":8, "HP":45, "STR":3, "PDT":-2, "Jobs":["war","mnk","rdm","thf","pld","drk","bst","brd","sam","nin","drg","blu","cor","dnc","run"]}
Oneiros_Cest = {"Name": "Oneiros Cest", "DEF":5, "Accuracy":9, "Store TP":3, "Gear Haste":3, "Jobs":["war","rdm","thf","pld","drk","bst","brd","rng","sam","nin","drg","blu","cor","dnc","run"]}
Fierce_Belt = {"Name": "Fierce Belt", "Attack":15, "Jobs":["war","mnk","rdm","thf","pld","drk","bst","bst","brd","rng","sam","nin","drg","blu","cor","dnc","run"]}
Demonry_Sash = {"Name": "Demonry Sash", "DEF":5, "MND":3, "CHR":3, "Magic Accuracy":3, "Jobs":["whm","blm","rdm","brd","smn","sch","geo"]}
Moepapa_Stone = {"Name": "Moepapa Stone", "DEF":5, "CHR":5, "Gear Haste":5, "Pet Haste":3, "Jobs":["bst","drg","smn","pup"]}
Fatality_Belt = {"Name": "Fatality Belt", "DEF":7, "DEX":4, "Accuracy":4, "Jobs":["war","rdm","thf","pld","drk","bst","brd","rng","sam","nin","drg","blu","cor","dnc","run"]}
Tjukurppa_Belt = {"Name": "Tjukurrpa Belt", "STR":5, "DA":1, "Jobs":["war","mnk","thf","bst","nin","drg","blu","pup","dnc","run"]}
Bobcat_Belt = {"Name": "Bobcat Belt", "DEF":6, "STR":8, "Attack":-6, "Store TP":-6, "Jobs":["war","rdm","thf","pld","drk","bst","brd","rng","sam","nin","drg","blu","cor","dnc","run"]}
Marching_Belt = {"Name": "Marching Belt", "DEF":3, "Wind Instrument Skill":3,  "Jobs":["brd"]}

waists = [Oneiros_Rope,Mujin_Obi,Oneiros_Sash,Oneiros_Belt,Oneiros_Cest,Fierce_Belt,Demonry_Sash,Moepapa_Stone,Fatality_Belt,Tjukurppa_Belt,Bobcat_Belt,Marching_Belt]

#Legs  {"Name": "",  "Jobs":[]}
legs = []

#Feet  {"Name": "",  "Jobs":[]}
Ryuga_Sune_Ate = {"Name": "Ryuga Sune-Ate", "DEF":20, "HP":30, "VIT":7, "Accuracy":4, "Evasion":4, "Gear Haste":3, "Automaton Skills":5, "Jobs":["mnk","thf","drk","bst","nin","sam","drg","pup","dnc","run"]}
Aifes_Pumps = {"Name": "Aifes Pump", "DEF":20, "MP":20, "MND":7, "Magic Accuracy":-4, "Conserve MP":4, "Enmity":-5, "Automaton Cure Potency":4, "Jobs":["whm","blm","rdm","brd","smn","pup","sch","geo"]}
Agronas_Leggings = {"Name": "Agronas Leggings", "DEF":15, "STR":4, "Accuracy":3, "DA":2, "Gear Slow":4, "Jobs":["mnk","thf","bst","rng","nin","blu","cor","pup","dnc","run"]}

feet = [Ryuga_Sune-Ate,Aifes_Pumps,Agronas_Leggings]