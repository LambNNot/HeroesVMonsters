""""
Sam Phan, Project 2: "Hero vs. Monsters" Game
"""
import random
import time
import unittest

"""
Variable Setting
"""
#Constant Texts
starting_message = "Welcome, hero. You are playing Hero vs. Monsters. Please type 'Start' to begin."
break_line = "----------\n"

#Arsenal Data
sword = random.randint(2,8)
arrow = random.randint(2,8)
magic = random.randint(2,8)
Hammer = random.randint(2,8)
arsenal = [sword, arrow, magic, Hammer]


#Inventory Data
remedy = 2
elixir = 0
toolbox = 0
potion = 2
inventory = [remedy, elixir, toolbox, potion]

#Hero Data
player_name = "Hero"
player_hitpoints = 300
player_luren = 30
victories = 0
player_is_stunned = False
player_is_bleeding = False
player_is_cursed = False
player_is_blessed = False

#Enemy Data
current_enemies = []
current_enemy_hitpoints = 100
enemy_is_stunned = False
enemy_is_bleeding = False
enemy_is_cursed = False
enemy_is_blessed = False

monsters_vulnerabilties  = {
    "Dragon":"Arrow",
    "Zombie":"Sword",
    "Ghost":"Magic",
    "Minotaur": "Hammer"
}

weapon_base_damage = {
    "Arrow":50,
    "Sword":70,
    "Magic": 60,
    "Hammer": 80
}

item_healing = {
    "Remedy": 10,
    "Elixir": 0,
    "Pandora's Toolbox": 0,
    "Potion": 80
}

weapon_item_loot_values = {
    "Arrow":1,
    "Sword":3,
    "Magic": 2,
    "Hammer": 3,
    "Remedy": 2,
    "Elixir": 2,
    "Pandora's Toolbox": 8,
    "Potion": 3
}

shop_cost = {
    "Arrow":5,
    "Sword":7,
    "Magic": 3,
    "Hammer": 8,
    "Remedy": 5,
    "Elixir": 6,
    "Pandora's Toolbox": 20,
    "Potion": 8
}

monsters_damage = {
    "Dragon": 60,
    "Zombie": 10,
    "Ghost": 20,
    "Minotaur": 40
}

monsters_hitpoints = {
    "Dragon": 450,
    "Zombie": 130,
    "Ghost": 140,
    "Minotaur": 360
}

monsters_threat_level = {
    "Dragon": 6,
    "Zombie": 1,
    "Ghost": 2,
    "Minotaur": 4
}

monsters_loot = {
    "Dragon": 22,
    "Zombie": 3,
    "Ghost": 4,
    "Minotaur": 14
}

""""
Supportive Logic Functions
"""
def reset_data(): #Resets all initial variables for replay  
    #Arsenal Data
    sword = random.randint(2,8)
    arrow = random.randint(2,8)
    magic = random.randint(2,8)
    Hammer = random.randint(2,8)
    global arsenal; arsenal = [sword, arrow, magic, Hammer]
    
    #Inventory Data  
    remedy = 2
    elixir = 0
    toolbox = 0
    potion = 2
    global inventory; inventory = [remedy, elixir, toolbox, potion]

    #Hero Data
    global player_hitpoints; player_hitpoints = 300
    global victories; victories = 0
    global player_luren; player_luren = 30
    global player_is_stunned; player_is_stunned = False
    global player_is_bleeding; player_is_bleeding = False
    global player_is_cursed; player_is_cursed = False
    global player_is_blessed; player_is_blessed = False

    #Enemy Data
    global current_enemies; current_enemies = []
    global current_enemy_hitpoints; current_enemy_hitpoints = 100
    global enemy_is_stunned; enemy_is_stunned = False
    global enemy_is_bleeding; enemy_is_bleeding = False
    global enemy_is_cursed; enemy_is_cursed = False
    global enemy_is_blessed; enemy_is_blessed = False

def initialize_new_enemy_data(enemy): #Resets enemy data for each new enemy encounter
    global current_enemy_hitpoints; current_enemy_hitpoints = monsters_hitpoints[enemy]
    global enemy_is_stunned; enemy_is_stunned = False
    global enemy_is_bleeding; enemy_is_bleeding = False
    global enemy_is_cursed; enemy_is_cursed = False
    global enemy_is_blessed; enemy_is_blessed = False
    

def randomize_arsenal(min,max): 
    for i,weapon in enumerate(arsenal):
        arsenal[i] = random.randint(min,max)

def critical_hit_roll():
    return random.randint(1,20)

def damage_roll():
    return (random.randint(85, 115)/100) #Taken from Pokemon for more RNG

def status_report(info): #Reports specific information to the player based on the argument
    print(break_line)
    match info:
        case "General":
            total_weapons = ["Arrow", "Sword", "Magic", "Hammer"]
            total_items = ["Remedy","Elixir","Pandora's Toolbox", "Potion"]
            print(f"Your arsenal contains:")
            for number in range(len(arsenal)):
                print(f"{arsenal[number]} {total_weapons[number]}(s)")
            print(f"Your inventory contains:")
            for number in range(len(inventory)):
                print(f"{inventory[number]} {total_items[number]}(s)")
            print(f"You have {player_luren} Luren (Money)!")
            print(f"You have {player_hitpoints}/300 HP remaining.")
            print(f"Nights Survived: {victories}.")
            if player_is_bleeding:
                print("You are bleeding! (You will take damage after you act!)")
            if player_is_blessed:
                print("You are blessed! (Your next attack will be a Critical Hit!)")
            if player_is_cursed:
                print("You are cursed! (You will take bonus damage after getting hit!")
        case "Economy":
            print(f"You have {player_hitpoints} HP remaining")
            print(f"You have {player_luren} Luren (Money)!")
            total_weapons = ["Arrow", "Sword", "Magic", "Hammer"]
            print(f"Your arsenal contains:")
            for number in range(0,len(arsenal)):
                print(f"{arsenal[number]} {total_weapons[number]}(s)")
            total_items = ["Remedy","Elixir","Pandora's Toolbox", "Potion"]
            print(f"Your inventory contains:")
            for number in range(0,len(arsenal)):
                print(f"{inventory[number]} {total_items[number]}(s)")
        case "Arsenal":
            print("Hero, here is your Arsenal Report:")
            total_weapons = ["Arrow", "Sword", "Magic", "Hammer"]
            print(f"Your arsenal contains:")
            for number in range(0,len(arsenal)):
                print(f"{arsenal[number]} {total_weapons[number]}")
        case "Inventory":
            total_items = ["Remedy","Elixir","Pandora's Toolbox", "Potion"]
            print(f"Your inventory contains:")
            for number in range(0,len(arsenal)):
                print(f"{arsenal[number]} {total_items[number]}")
        case "Combat":
            print(f"You have {player_hitpoints} HP remaining.")
            if player_is_bleeding:
                print("You are bleeding! (You will take damage after you act!)")
            if player_is_blessed:
                print("You are blessed! (Your next attack will be a Critical Hit!)")
            if player_is_cursed:
                print("You are cursed! (You will take bonus damage after getting hit!)")
            if player_is_stunned:
                print("You are stunned! (Your next attack will fail!)")
            if enemy_is_bleeding:
                print("The enemy is bleeding! (They will take damage after acting!)")
            if enemy_is_blessed:
                print("The enemy is blessed! (Their next attack will be a Critical Hit!)")
            if enemy_is_cursed:
                print("The enemy is cursed! (They will take bonus damage after getting hit!)")
            if enemy_is_stunned:
                print("The enemy is stunned! (Their next attack will fail!)")
        case _:
            pass
    print("End of Status Report.")

def apply_status(entity, status): #General function to apply Status conditions to either player or enemy; displays message if Status already True
    global player_is_bleeding
    global player_is_blessed
    global player_is_cursed
    global player_is_stunned
    global enemy_is_bleeding
    global enemy_is_blessed
    global enemy_is_stunned
    global enemy_is_cursed

    match status:
        case "Bleed":
            if entity == "Player":
                if player_is_bleeding:
                    print("You're already Bleeding.")
                else:
                    player_is_bleeding = True
                    print("You are now Bleeding!")
            else:
                if enemy_is_bleeding:
                    print(f"The {entity} is already Bleeding.")
                else:
                    enemy_is_bleeding = True
                    print(f"The {entity} is now Bleeding!")
        case "Blessed":
            if entity == "Player":
                if player_is_blessed:
                    print("You're already Blessed!")
                else:
                    player_is_blessed = True
                    print("You are now Blessed!")
            else:
                if enemy_is_blessed:
                    print(f"The {entity} is already Blessed.")
                else:
                    enemy_is_blessed = True
                    print(f"The {entity} is now Blessed!")
        case "Cursed":
            if entity == "Player":
                if player_is_cursed:
                    print("You're already Cursed!")
                else:
                    player_is_cursed = True
                    print("You are now Cursed!")
            else:
                if enemy_is_cursed:
                    print(f"The {entity} is already Cursed.")
                else:
                    enemy_is_cursed = True
                    print(f"The {entity} is now Cursed!")
        case "Stunned":
            if entity == "Player":
                if player_is_stunned:
                    print("You're already Stunned!")
                else:
                    player_is_stunned = True
                    print("You are now Stunned!")
            else:
                if enemy_is_stunned:
                    print(f"The {entity} is already Stunned.")
                else:
                    enemy_is_stunned = True
                    print(f"The {entity} is now Stunned!")
        case _:
            pass

def enemy_drops(enemy): #Generates and adds random weapons/items given a monster
    print(break_line)
    global player_luren
    bonus_multiplier = random.randint(80, 120)/100
    loot_budget = clamp((victories//2) // bonus_multiplier, 0, 32)
    total_luren = round(monsters_loot[enemy] * bonus_multiplier)
    total_loot = []
    loot_table = []
    loot_messages = []
    match enemy:
        case "Dragon":
            loot_table = ["Arrow","Sword","Magic","Hammer","Pandora's Toolbox"]
        case "Zombie":
            loot_table = ["Arrow","Sword","Hammer","Remedy","Potion"]
        case "Ghost":
            loot_table = ["Magic","Remedy","Elixir","Potion"]
        case "Minotaur":
            loot_table = ["Arrow","Sword","Hammer","Pandora's Toolbox"]
        case _:
            pass
    while loot_budget > 0 and len(loot_table) > 0: #Uses a budget system to moderate randomized drops (Similar to approach_phase())
        dropping_loot = random.choice(loot_table)
        if(weapon_item_loot_values[dropping_loot] > loot_budget): #Eliminates droppable items based on available loot_budget
            loot_table.remove(dropping_loot)
            continue
        loot_budget -= weapon_item_loot_values[dropping_loot]
        total_loot.append(dropping_loot)
    player_luren += total_luren
    print(f"You have earned {total_luren} Luren for slaying the {enemy}!") 
    for loot in set(total_loot):
        loot_messages.append(f"{total_loot.count(loot)} {loot}(s)")
    if(loot_messages != []):
        print(f"The {enemy} also dropped:\n {', '.join(loot_messages)}!")
    for loot in total_loot:
        match loot:
            case "Arrow":
                arsenal[0] += 1
            case "Sword":
                arsenal[1] += 1
            case "Magic":
                arsenal[2] += 1
            case "Hammer":
                arsenal[3] +=1
            case "Remedy":
                inventory[0] += 1
            case "Elixir":
                inventory[1] += 1
            case "Pandora's Toolbox":
                inventory[2] += 1
            case "Potion":
                inventory[3] += 1

def menu_selection_index(minimum_index, maximum_index): #Foolproofing player menu selection for misinputs
    while True:
        index = input()
        if index.isnumeric():
            index = clamp(int(index), minimum_index, maximum_index)
            break
    return index

def generate_random_options(options, quantity): #Returns a random list with values from a predetermined one
    options_generated = []
    for number in range(quantity):
        random_option_index = random.randint(0,len(options)-1)
        options_generated.append(options.pop(random_option_index))
    return options_generated

""""
Main Gameplay Loop: Key Phases
"""
def interim_phase(): #Non-combat phase
    print(break_line)
    print(f"It is time to rest, {player_name}. There's a nearby town!")
    interim_options = ["Status Report", "Rest"]
    interim_options.extend(generate_random_options(["Shop","Hunt","Visit Bulletin"], 2))
        
    selected_index = 1
    while selected_index == 1: #Makeshift do-while loop; Status Report will return player to menu until they select a diff option (without reloading options)
        print("What are you looking to do here? (Type the number to select)")
        for number in range(0,4):
            print(f"{number + 1}) {interim_options[number]}")
        selected_index = menu_selection_index(1,4)
        if selected_index == 1:
            status_report("General")
            print(break_line)
    match(interim_options[selected_index-1]):

        case "Rest":
            interim_rest()

        case "Shop":
            interim_shop()
                
        case "Hunt":
            interim_hunt()
        
        case "Visit Bulletin":
            interim_visit()
        
        case _:
            interim_phase()

def approach_phase(threat_budget = 1): #Generates list of monsters to fight for the Night
    print(break_line)
    print_delay(f"The dusk settles...", 1)
    threat_budget = victories + 1
    spawnable_monsters = ["Dragon", "Zombie", "Ghost", "Minotaur"]
    while (threat_budget > 0): #Randomly fills current_enemies based on number of victories
        spawning_monster = random.choice(spawnable_monsters)
        if(monsters_threat_level[spawning_monster] > threat_budget): #Eliminates spawnable monsters based on available threat_budget
            spawnable_monsters.remove(spawning_monster)
            continue
        threat_budget -= monsters_threat_level[spawning_monster]
        current_enemies.append(spawning_monster)
    print_delay(f"The monsters rest not under nightfall, and nor will you, {player_name}. You are beginning Night {victories+1}.", 1)

def encounter_phase(): #Runs encounter messages for each monster
    global victories
    global player_hitpoints
    global player_is_stunned 
    print(break_line)
    print_delay(f"Traveling by night alone, the perils await. You see {len(current_enemies)} silhouette(s) ahead.")
    for enemy in range(len(current_enemies)):
        print_delay(f"You encounter the next monster: a {current_enemies[0]}! ({len(current_enemies)-1} silhouette(s) following.)", 2)
        initialize_new_enemy_data(current_enemies[0])
        fight_phase(current_enemies[0])
        if(player_hitpoints <= 0):
            break
    victories += 1
    player_is_stunned = False
    print_delay(f"The gloom retreats as the sun rises...", 1)

def fight_phase(monster): #Actual combat-loop
    global current_enemy_hitpoints
    global player_hitpoints
    while player_hitpoints > 0 and current_enemy_hitpoints > 0: #Has to check for enemy HP here because of Bleed damage
        select_action()
        if(current_enemy_hitpoints > 0): #Has to check again for post-player-action kills
            monster_action(monster)
        else:
            break
    if player_hitpoints > 0:
        print(f"You have successfully slain the {monster}!")
        enemy_drops(current_enemies.pop(0))

"""
Gameplay Loop: Support Functions for Non-Combat Phases
"""

def interim_hunt(): #Hunt - Loses HP for free, random enemy drops
    print(break_line)
    global player_hitpoints
    print_delay(f"{player_name}, you have opted to hunt during the day. You'll receive bonus loot from slaying weakened monsters.")
    random_hunt = random.choice(list(monsters_vulnerabilties.keys()))
    print_delay(f"You found a random weakened {random_hunt}!")
    hunt_damage = calculate_enemy_attack_damage(random_hunt, 0)
    enemy_drops(random_hunt)
    player_hitpoints -= hunt_damage
    print(f"You took {hunt_damage} damage from hunting.")

def interim_rest(): #Rest - Heal and remove Bleeding; Can pay for full heal
    print(break_line)
    print_delay(f"{player_name}, you have opted to rest for the day.")
    global player_luren 
    global player_hitpoints
    global player_is_bleeding
    print(f"You have {player_hitpoints} HP remaining and {player_luren} Luren (Gold).")
    if(player_luren >= 12):
        if(input("Would you like to rest at the nearby Inn for an extra small payment? (Yes/No)\n").lower() == "yes"):
            player_luren -= 12
            player_hitpoints = 300
            print(f"Your HP has been fully recovered! You {player_luren} Luren left.")
        else:
            player_hitpoints += 80
            player_hitpoints = clamp(player_hitpoints, 0, 300)
            print(f"You now have {player_hitpoints} HP remaining and {player_luren} Luren (Gold).")
    if(player_is_bleeding):
        player_is_bleeding = False
        print("You are no longer bleeding.")

def interim_shop(): #Shop - Generates random assortment of weapons/items that can be purchased
    print(break_line)
    shop_options = generate_random_options(["Arrow", "Sword","Magic","Hammer", "Remedy","Elixir","Pandora's Toolbox","Potion"], 4)
    purchases = 0
    while True:
        purchases_penalty = clamp((purchases-2), 0, purchases)
        print(f"You have {player_hitpoints} HP remaining and {player_luren} Luren (Gold).")
        print("What would you like to buy?")
        print("1) Leave Shop \n2) Economy Status")
        for number in range(1,5):
            print(f"{number+2}) {shop_options[number-1]} for {shop_cost[shop_options[number-1]] + purchases_penalty} Luren")
        
        selected_index = menu_selection_index(1,6)
        
        if(selected_index == 1): #Leave Shop selected
            break
        elif(selected_index == 2): #Economy Status selected
            print("Here is your Economy Status Report:")
            status_report("Economy")
            print(break_line)
            continue
        elif(player_luren < shop_cost[shop_options[selected_index-3]] + purchases_penalty):
            print(f"{player_name}, you do not have enough Luren for that purchase.")
        else:
            shop_purchase(shop_options[selected_index-3], shop_cost[shop_options[selected_index-3]] + purchases_penalty)
            purchases += 1
        print(break_line)

def shop_purchase(item, cost): #Actually adds the purchase to your arsenal/inventory
    global player_luren
    weapons_list = list(weapon_base_damage.keys())
    items_list = list(item_healing.keys())
    player_luren -= cost
    if(item in weapons_list):
        arsenal[weapons_list.index(item)] += 1
    elif(item in items_list):
        inventory[items_list.index(item)] += 1
    print(f"You've purchased 1 {item}.")

def interim_visit(): #Visit - Encounter random NPC
    print(break_line)
    print_delay("You've opted to visit the bulletin...")
    all_visitors = ["Jester", "King's Merchant"]
    visitor = random.choice(all_visitors)
    print_delay(f"You ended up visiting the {visitor}")
    visit(visitor)

def visit(visitor): #Contains all random Visitor NPC code
    global player_luren
    print(break_line)
    match visitor:
        case "Jester":
            print_delay(f"Jester: 'Chaos improves all, don't you think?' (Yes/No)")
            if input().lower() == "yes":
                randomize_arsenal(int((victories/2)+1), clamp(int((victories*1.5)+1), 0, 12))
                player_luren -= 8
                player_luren = clamp(player_luren, 0, player_luren)
                print_delay("The Jester randomized your arsenal and took some Luren!")
            else:
                print_delay(f"Jester: 'Hehehe, you will change your mind one day, {player_name}.'")
                
        case "King's Merchant":
            print_delay(f"Merchant: 'I've finally found you, {player_name}! Here, the King offers his countenance.'")
            player_luren += 20
            print_delay("You received 20 Luren!")


"""
Support Functions for Combat
"""

def calculate_player_attack_damage(weapon_type, monster, roll):
    multipliers = damage_roll()
    damage = weapon_base_damage[weapon_type]
    global enemy_is_cursed
    global current_enemy_hitpoints

    if weapon_type == "Magic": #Randomizes Magic base damage (INTENDED MECHANIC)
        damage = random.randint(20,120)
    if weapon_type == monsters_vulnerabilties[monster]: #Checks for Monster Weaknesses
        multipliers *= 2
        print(f"{monster}s seem to be vulnerable to {weapon_type} attacks!")
    if(enemy_is_cursed): #Checks if Enemy has Cursed Status
        damage += current_enemy_hitpoints*0.2
        enemy_is_cursed = False
        print_delay(f"The {monster} took bonus damage from its curse!")
    if roll >= 20: #Checks for a critical hit
        multipliers *= 2
        print_delay("You landed a critical hit!")
    return int(damage * multipliers)

def player_attack(weapon, monster): #Specific chance bonuses for each weapon
    print(break_line)
    global current_enemy_hitpoints
    global player_hitpoints
    global enemy_is_bleeding
    global enemy_is_cursed
    global enemy_is_blessed
    global enemy_is_stunned
    global player_is_blessed
    global player_is_stunned
    global player_is_bleeding

    if(player_is_stunned): #Checks if Player is Stunned
        print_delay(f"You were stunned! The {monster} makes its move!")
        player_is_stunned = False
        return None
    
    print_delay(f"You attacked with your {weapon}.")
    roll = critical_hit_roll()
    multipliers = 1
    
    if (player_is_blessed): #Checks if Player is Blessed
        roll += 20
        player_is_blessed = False
        print(f"Your blessing empowered your attack!")
    total_damage = calculate_player_attack_damage(weapon, monster, roll)
    match weapon:
        case "Arrow":
            if monster == "Ghost":
                print(f"Arrows seem to have no effect on the {monster}")
                multipliers = 0
            if monster == "Dragon":
                roll *= 1.5
            if int(roll) >= 15:
                multipliers *= 2
                print("Your arrow found a vital!")
        case "Sword":
            if monster == "Zombie":
                roll += 6
            if monster == "Minotaur":
                print(f"The {monster} shattered the sword! Its shards flew everywhere!")
                roll += 16
                apply_status("Player", "Bleed")
            if int(roll) >= 16:
                apply_status(monster, "Bleed")
        case "Magic":
            if monster == "Ghost" or monster == "Dragon":
                roll += 5
                if enemy_is_blessed:
                    enemy_is_blessed = False
                    print(f"You've removed the {monster}'s Blessing!")
            if roll >= 10:
                apply_status(monster, "Cursed")
            elif roll <= 5:
                apply_status(monster, "Blessed")
        case "Hammer":
            if monster == "Minotaur" or monster == "Zombie":
                roll *= 1.5
            if int(roll) >= 16:
                apply_status(monster, "Stunned")
        case _:
            pass

    total_damage *= multipliers
    current_enemy_hitpoints -= total_damage
    print_delay(f"You dealt {total_damage} to the {monster}!")

    if player_is_bleeding:
        bleed_damage = int(player_hitpoints * (1/10))
        player_hitpoints -= bleed_damage
        print_delay(f"You took {bleed_damage} damage from Bleeding.")
    

def calculate_enemy_attack_damage(enemy, roll):
    multipliers = damage_roll()
    damage = monsters_damage[enemy]
    global player_is_cursed
    global player_hitpoints

    if(roll >= 20): #Apply Critical-hit Multiplier
        multipliers *= 2
        print_delay(f"The {enemy} landed a Critical Hit!")
    if(player_is_cursed): #Checks for Cursed Status
        damage += player_hitpoints*0.2
        player_is_cursed = False
        print_delay("You took bonus damage from your curse!")
    return int(damage * multipliers)

def monster_action(monster): #Function for Monster "AI"
    print(break_line)
    global current_enemy_hitpoints
    global player_hitpoints
    global player_is_bleeding
    global player_is_cursed
    global player_is_stunned
    global enemy_is_blessed
    global enemy_is_stunned
    global enemy_is_bleeding

    if(enemy_is_stunned): #Checks if enemy is Stunned
        print_delay(f"The enemy {monster} is stunned! It is unable to move!")
        enemy_is_stunned = False
        return None
    
    print_delay(f"The {monster} attacked.")
    roll = critical_hit_roll()
    multipliers = clamp(victories/8, 1, 3) #Enemy Damage scales with number of victories

    if (enemy_is_blessed): #Checks if enemy is Blessed
        roll += 20
        enemy_is_blessed = False
        print(f"The enemy's Blessing empowered its attack!")
    total_damage = calculate_enemy_attack_damage(monster, roll)
    match monster:
        case "Dragon": 
            if current_enemy_hitpoints <= monsters_hitpoints["Dragon"]*0.25: #Dragon's "Desperation Bonus"
                roll *= 1.5
                print("The Dragon is Desperate!")
            if roll <= 4:
                enemy_is_blessed = True
                print("The Dragon Blessed itself for its next attack!")
            if roll >= 14:
                current_enemy_hitpoints += int(monsters_hitpoints["Dragon"] * (1/8))
                print(f"The Dragon healed itself during its attack! (+ {int(monsters_hitpoints['Dragon'] * (1/8))} HP)")
            if roll >= 30: #If-Elif Branch used for 3 different level of attacks
                print("The Dragon unleashed its full wrath!")
                multipliers *= 2
                destroy_arsenal(16)
                destroy_inventory(16)
                print("The Dragon destroyed a bunch of items and weapons!")
                player_is_stunned = True
                player_is_cursed = True
                print("The Dragon has Cursed and Stunned you!")
            elif roll >= 20:
                print("The Dragon unleashed a devastating attack!")
                multipliers * 1.5
                destroy_inventory(8)
                destroy_arsenal(8)
                print("The Dragon destroyed a bunch of items and weapons!")
                player_is_cursed = True
                print("The Dragon has Cursed you!")
            elif roll >= 14:
                player_is_cursed = True
                print("The Dragon has Cursed you!")
        case "Zombie":
            if roll >= 20:
                apply_status("Player","Bleed")
        case "Ghost":
            if roll >= 12:
                apply_status("Player","Cursed")
            if roll >= 14:
                destroy_inventory(5)
                print("The Ghost made some items vanish!")
        case "Minotaur":
            if current_enemy_hitpoints <= monsters_hitpoints["Minotaur"]*0.25: #Minotaur's "Desperation Bonus"
                multipliers *= 2
                destroy_arsenal(5)
                print("The Minotaur's Desperate attack destroyed some of your weapons!")
            if roll >= 20:
                apply_status("Player","Stunned")
            if roll >= 18:
                destroy_arsenal(5)
                print("The Minotaur broke several of your weapons!")
            if roll >= 14:
                apply_status("Player", "Bleed")
        case _:
            pass

    total_damage *= multipliers
    player_hitpoints -= int(total_damage)
    print_delay(f"You took {int(total_damage)} damage from the {monster}!")

    if(enemy_is_bleeding):
        bleed_damage = int(monsters_hitpoints[monster]*(1/10))
        current_enemy_hitpoints -= bleed_damage
        print_delay(f"The {monster} took {bleed_damage} damage from bleeding.")


def select_action(): #Presents Action Select Menu
    print(break_line)
    actionable_options = ["Attack", "Use Item", "Status Report"]

    print(f"The enemy {current_enemies[0]} stands ahead.")
    print(f"{current_enemies[0]} HP: {current_enemy_hitpoints}/{monsters_hitpoints[current_enemies[0]]}\n")
    print(f"Your current HP: {player_hitpoints}/300")

    print((f"What would you like to do, {player_name}?"))
    for option in actionable_options:
        print(f"{actionable_options.index(option)+1}) {option}")
    selected_index = menu_selection_index(1, 3)
    if selected_index == 1:
        select_weapon()
    elif selected_index == 2:
        select_item()
    else:
        print("Here is your Combat Status Report:")
        status_report("Combat")
        select_action()

def select_weapon(): #Presents Weapon Select Menu
    print(break_line)
    print("Select a weapon from your arsenal to attack with:")
    global player_hitpoints
    all_weapons = list(weapon_base_damage.keys())

    if(arsenal == [0,0,0,0]): #LOSS CONDITION
        print_delay(f"You have no more weapons to fight with! WATCH OUT, {player_name}!")
        player_hitpoints = 1
        return None
    
    if(arsenal == [arsenal[0],0,0,0] and current_enemies[0] == "Ghost") and not enemy_is_bleeding: #SPECIAL LOSS CONDITION FOR GHOSTS
        print_delay(f"You have no more weapons to fight the Ghost! WATCH OUT, {player_name}!")
        player_hitpoints = 1
        return None

    for weapon in range(len(arsenal)):
        print(f"{weapon+1}) {all_weapons[weapon]} ({arsenal[weapon]} remaining.)")
    print("5) Cancel")

    selected_index = menu_selection_index(1,5)
    
    if selected_index == 5: #Exits select_weapon "menu"
        select_action()
    elif arsenal[selected_index-1] == 0:
        print(f"You are out of {all_weapons[selected_index-1]}s!")
        select_weapon()
    else:
        player_attack(all_weapons[selected_index-1],current_enemies[0])
        arsenal[selected_index-1] -= 1


def select_item(): #Presents Item Select Menu
    print(break_line)
    print("Select an item from your inventory to use:")
    all_items = list(item_healing.keys())
    for item in range(len(inventory)):
        print(f"{item+1}) {all_items[item]} ({inventory[item]} remaining.)")
    print("5) Cancel")

    selected_index = menu_selection_index(1, 5)
    
    if selected_index == 5: # Exits select_item "menu"
        select_action()
    elif inventory[selected_index-1] == 0:
        print(f"You are out of {all_items[selected_index-1]}s!")
        select_item()
    else:
        use_item(all_items[selected_index-1])
        inventory[selected_index-1] -= 1

def use_item(item): #Contains code for all Items
    print(break_line)
    global player_hitpoints
    global current_enemy_hitpoints
    global player_is_bleeding
    global player_is_blessed
    global player_is_cursed
    global player_is_stunned

    print_delay(f"You used {item}.")
    
    match item:
        case "Remedy":
            player_is_bleeding = False
            player_is_cursed = False
            player_is_stunned = False
            print_delay(f"The Remedy restored {item_healing[item]} HP and cured all negative statuses!")
        case "Elixir":
            player_is_blessed = True
            print_delay(f"The Elixir blessed {player_name}!")
        case "Pandora's Toolbox":
            instant_toolbox_damage = 0
            total_toolbox_damage = 0
            print_delay(f"You opened Pandora's Toolbox!...")
            for weapon in range(0,3):
                random_weapon = random.choice(list(weapon_base_damage.keys()))
                print_delay(f"\n{random_weapon}(s) burst forth!")
                instant_toolbox_damage = calculate_player_attack_damage(random_weapon, current_enemies[0], random.randint(0,20))
                print(f"The {current_enemies[0]} took {instant_toolbox_damage} damage!")
                total_toolbox_damage += instant_toolbox_damage
            current_enemy_hitpoints -= total_toolbox_damage
            current_enemy_hitpoints = clamp(current_enemy_hitpoints, 1, monsters_hitpoints[current_enemies[0]])
            print_delay(f"...After the {current_enemies[0]} took {total_toolbox_damage} damage, the box vanished!")
        case "Potion":
            print_delay(f"The Potion restored 80 HP!")
        case _:
            pass
    player_hitpoints += item_healing[item]
    player_hitpoints = clamp(player_hitpoints, 0, 300)
    select_action() #Items are instantaneous/do not take a turn

def destroy_arsenal(damage_value): #Randomly removes a number of weapons
    for number in range(damage_value):
        random_index = random.randint(0,3)
        if arsenal[random_index] > 0:
            arsenal[random_index] -= 1

def destroy_inventory(damage_value):
    for number in range(damage_value): #Randomly removes a number of items
        random_index = random.randint(0,3)
        if inventory[random_index] > 0:
            inventory[random_index] -= 1    

def test_calc_player_dmg():
    pass

"""
Non-Game Related functions
"""
def clamp(value, minimum_value, maximum_value): #Clamp functions make life easier
    return max(minimum_value,min(value,maximum_value))

def print_delay(string, delay_in_seconds = 1): #Makes text a little more readable
    print(string)
    time.sleep(delay_in_seconds)

"""
Function Testing
"""
class TestCalculations(unittest.TestCase):

    def setUp(self):
        print("Setting up test...")

    def tearDown(self):
        print("Tearing down test...")

    def test_calculate_player_attack_damage(self):
        random.seed(7357) #Makes damage_roll Multiplier = 0.96
        self.assertEqual(calculate_player_attack_damage("Arrow","Dragon", 0), 96)
        random.seed(7357)
        self.assertEqual(calculate_player_attack_damage("Arrow","Dragon", 20), 192)
        random.seed(7357)
        self.assertEqual(calculate_player_attack_damage("Arrow","Zombie", 0), 48)
        random.seed(7357)
        self.assertEqual(calculate_player_attack_damage("Arrow","Minotaur", 0), 48)
        random.seed(7357)
        self.assertEqual(calculate_player_attack_damage("Arrow","Minotaur", 20), 96)

    def test_calculate_enemy_attack_damage(self):
        random.seed(7357) #Makes damage_roll Multiplier = 0.96
        self.assertEqual(calculate_enemy_attack_damage("Dragon", 0), 57)
        random.seed(7357)
        self.assertEqual(calculate_enemy_attack_damage("Dragon", 20), 115)
        random.seed(7357)
        self.assertEqual(calculate_enemy_attack_damage("Zombie", 0), 9)
        random.seed(7357)
        self.assertEqual(calculate_enemy_attack_damage("Ghost", 0), 19)
        random.seed(7357)
        self.assertEqual(calculate_enemy_attack_damage("Minotaur", 0), 38)

    def test_player_stunned(self): #Testing player_attack early return None if played is Stunned
        global player_is_stunned; player_is_stunned = True
        self.assertIsNone(player_attack("Arrow","Dragon"))

    def test_monster_stunned(self): #Testing monster_action early return None if enemy is Stunned
        global enemy_is_stunned; enemy_is_stunned = True
        self.assertIsNone(monster_action("Dragon"))

    def test_player_loss_condition(self): #Testing early return None if player does not have weapons or a Pandora's Toolbox
        global arsenal; arsenal = [0,0,0,0]
        global inventory; inventory = [0,0,0,0]
        self.assertIsNone(select_weapon())

    def test_clamp(self):
        self.assertEqual(clamp(4, 0, 10), 4)
        self.assertEqual(clamp(11, 0, 10), 10)
        self.assertEqual(clamp(-20.0, 0, 10), 0)
        self.assertEqual(clamp(10.01, 0, 10), 10)

"""if __name__ == '__main__':
    unittest.main()"""



"""
Game Start Code
"""
def launch_game():
    print(break_line)
    print(starting_message)
    if(input().lower() == "start"):
        run_gameplay()
    else:
        launch_game()

def run_gameplay():
    reset_data()
    global player_name; player_name = input("What is your name, Hero?\n")
    while player_hitpoints > 0:
        interim_phase()
        approach_phase()
        encounter_phase()
    print(break_line)
    print(f"You have fallen {player_name}, but do not give up. Determination will continue your story.")
    print(f"You survived through {victories} nights!")
    launch_game()

random.seed()
launch_game()
