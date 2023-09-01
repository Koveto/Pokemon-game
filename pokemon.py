import os, sys, math, random

# Main Program
def main():
    """ Main Program

        1. Welcome
        2. Enter Names
        3. Team Builder
        4. Order Select
        5. Battle System
        6. Play again?
            - 1 = Back to #4
            - 2 = Back to #3
            - 3 = Back to #2
            - 4 = Close Game
    """
    input(('\n' * DISPLAY) + '     Welcome to the World of Pokemon!\n\n     >> Press "Enter" to begin. ')
    playing = True
    while playing:
        name1, name2 = input(("\n" * DISPLAY) + '     Player 1, enter your name...\n\n     >> '), input(('\n' * DISPLAY) + "     Player 2, enter your name...\n\n     >> ")
        playing1 = True
        while playing1:
            team1, team2 = teamBuilder([], name1), teamBuilder([], name2)
            input(('\n'*DISPLAY)+'     Next, each player will select their team order.\n' + "     Don't look while your opponent selects!" + '\n\n     >> Press "Enter" to continue. ')
            playingSet = True
            while playingSet:
                team1, team2 = orderSelect(name1, team1, name2, team2), orderSelect(name2, team2, name1, team1)
                result = battleSystem(name1, team1, name2, team2)
                flag = True
                while flag:
                    choice = input(('\n'*DISPLAY)+'     Please enter your desired input...\n\n\n     1 - Return to Order Select with same teams\n\n     2 - Return to Team Builder\n\n     3 - Change Names\n\n     4 - Close Game\n\n     >> ')
                    if '1' in choice:
                        flag = False
                    elif '2' in choice:
                        flag, playingSet = False, False
                    elif '3' in choice:
                        flag, playingSet, playing1 = False, False, False
                    elif '4' in choice:
                        flag, playingSet, playing1, playing = False, False, False, False
                    else:
                        input(("\n" * DISPLAY)+'     Your input could not be understood. Please try again.\n\n     >> Press "Enter" to continue. ')




# Template Specie
class Template():
    name = "Template"
    elements = ('','')
    maxHP = 50

    """ Pokemon Properties

        Status[0] = Main Status (ex. PAR or SLP)
        Status[1] = Turns left ^
        Status[2] = Secondary Status (ex. Confused)
        Status[3] = Turns left ^
        Status[4] = Flinch? (ex. 0 or 1)

        Charge = Is charging? (0 or 1)

        Attack/Defense = Buff/Debuff Multiplier
        - 2 by default for math purposes
        - Buffs: 1.5x (3), 2x (4), 2.5x (5), 3x (6)
        - Debuffs: .66x (1), .5x (0), .4x (-1), .33x (-2)

        Speed = Buff/Debuff Multiplier
        - 1.0 by default
        - Multiplied by 0.8 for buffs, by 1.2 for debuffs

        Accuracy = Buff/Debuff Multiplier
        - 1.0 by default
        - Multiplied by 1.1 for buffs, by .9 for debuffs
        
        Protect[0] = Protecting?
        Protect[1] = Turns in a row protecting
    """

    def __init__(self):
        hp = self.maxHP
        status = ['',0,'',0,'',0]
        charge = 0
        attack = 2
        defense = 2
        speed = 1
        accuracy = 1
        protect = [0,0]
        self.hp = hp
        self.status = status
        self.charge = charge
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.accuracy = accuracy
        self.protect = protect
    def getHP(self):
        return self._hp
    def getStatus(self):
        return self._status
    def getCharge(self):
        return self._charge
    def getAttack(self):
        return self._attack
    def getDefense(self):
        return self._defense
    def getSpeed(self):
        return self._speed
    def getAccuracy(self):
        return self._accuracy
    def getProtect(self):
        return self._protect
    def setHP(self, value):
        if value < 0:
            value = 0
        if value > self.maxHP:
            value = self.maxHP
        if type(value) != int:
            value = math.ceil(value)
        self._hp = value
    def setStatus(self, value):
        self._status = value
    def setCharge(self, value):
        self._charge = value
    def setAttack(self, value):
        self._attack = value
    def setDefense(self, value):
        self._defense = value
    def setSpeed(self, value):
        self._speed = value
    def setAccuracy(self, value):
        self._accuracy = value
    def setProtect(self, value):
        self._protect = value      
    hp = property(getHP, setHP)
    status = property(getStatus, setStatus)
    charge = property(getCharge, setCharge)
    attack = property(getAttack, setAttack)
    defense = property(getDefense, setDefense)
    speed = property(getSpeed, setSpeed)
    accuracy = property(getAccuracy, setAccuracy)
    protect = property(getProtect, setProtect)
    

    """ Info [Pokemon]

        1. Make a list of types that at least one of the Pokemon's types is weak/resistant to
            - Resistances0, Weaknesses0
        2. Check effectiveness and organize types into new lists
            - 2x & 1/2x goes to Resistances1/Weaknesses1
            - 4x & 1/4x goes to Resistances2/Weaknesses2
        3. Print Name/HP/Type(s)
        4. Print Weaknesses and Resistances
        5. Calculate and Print Immunities
        6. Print Move Data
    """

    # Initial Lists
    def __str__(self):
        resistances0 = []
        resistances1 = []
        resistances2 = []
        weaknesses0 = []
        weaknesses1 = []
        weaknesses2 = []
        immunities = []
        if len(self.elements) == 2:
            for i in self.elements:
                for ii in elementList:
                    if effectiveness(ii, i) < 1:
                        if ii not in resistances0:
                            resistances0.append(ii)
                    elif effectiveness(ii, i) > 1:
                        if ii not in weaknesses0:
                            weaknesses0.append(ii)
        else:
            for i in elementList:
                if effectiveness(i, self.elements) < 1:
                    if i not in resistances0:
                            resistances0.append(i)
                elif effectiveness(i, self.elements) > 1:
                    if i not in weaknesses0:
                        weaknesses0.append(i)


                        
        # Check effectiveness and organize types into new lists
        if len(self.elements) == 2:
            for i in resistances0:
                typeMultiplier = effectiveness(i,self.elements[0]) * effectiveness(i,self.elements[1])
                if typeMultiplier == .5:
                    resistances1.append(i)
                elif typeMultiplier == .25:
                    resistances2.append(i)
                elif typeMultiplier == 0:
                    immunities.append(i)
            for i in weaknesses0:
                typeMultiplier = effectiveness(i,self.elements[0]) * effectiveness(i,self.elements[1])
                if typeMultiplier == 2:
                    weaknesses1.append(i)
                elif typeMultiplier == 4:
                    weaknesses2.append(i)
            print(('\n' * DISPLAY) + '     ' + self.name + '\n\n     Maximum HP: ' + str(self.maxHP) + '\n     Type: ' + self.elements[0] + ' / ' + self.elements[1])
        else:
            for i in resistances0:
                typeMultiplier = effectiveness(i,self.elements)
                if typeMultiplier == .5:
                    resistances1.append(i)
                elif typeMultiplier == .25:
                    resistances2.append(i)
                elif typeMultiplier == 0:
                    immunities.append(i)
            for i in weaknesses0:
                typeMultiplier = effectiveness(i,self.elements)
                if typeMultiplier == 2:
                    weaknesses1.append(i)
                elif typeMultiplier == 4:
                    weaknesses2.append(i)
            print(('\n' * DISPLAY) + '     ' + self.name + '\n\n     Maximum HP: ' + str(self.maxHP) + '\n     Type: ' + self.elements)



        # Print Weaknesses and Resistances
        if weaknesses1 or weaknesses2:
            print('\n     Weaknesses:')
        for i in range(len(weaknesses1)):
            if weaknesses1[i] == weaknesses1[-1]:
                if i == 0:
                    if weaknesses2:
                        print('     \t' + weaknesses1[i] + ', ',end='')
                    else:
                        print('     \t' + weaknesses1[i],end='')
                else:
                    if weaknesses2:
                        print(weaknesses1[i] + ', ', end='')
                    else:
                        print(weaknesses1[i], end='')
            elif i == 0:
                print('     \t' + weaknesses1[i] + ', ', end='')
            else:
                print(weaknesses1[i] + ', ', end='')
        for i in range(len(weaknesses2)):
            if not weaknesses1:
                print('     \t' + weaknesses2[i] + ' (4X)',end='')
            else:
                if weaknesses2[i] == weaknesses2[-1] or weaknesses2[i] == weaknesses2[0]:
                    print(weaknesses2[i] + ' (4X)', end='')
                else:
                    print(weaknesses2[i] + ' (4X), ', end='')
        if resistances1 or resistances2:
            print('\n\n     Resistances:')
        for i in range(len(resistances1)):
            if resistances1[i] == resistances1[-1]:
                if i == 0:
                    if resistances2:
                        print('     \t' + resistances1[i] + ', ',end='')
                    else:
                        print('     \t' + resistances1[i],end='')
                else:
                    if resistances2:
                        print(resistances1[i] + ', ', end='')
                    else:
                        print(resistances1[i], end='')
            elif i == 0:
                print('     \t' + resistances1[i] + ', ', end='')
            else:
                print(resistances1[i] + ', ', end='')
        for i in range(len(resistances2)):
            if resistances2[i] == resistances2[-1]:
                print(resistances2[i] + ' (1/4)', end='')
            else:
                print(resistances2[i] + ' (1/4), ', end='')



        # Calculate and Print Immunities
        if immunities:
            print('\n\n     Immunities:')
            for i in range(len(immunities)):
                if immunities[i] == immunities[-1]:
                    if i == 0:
                        print('     \t' + immunities[i], end='')
                    else:
                        print(immunities[i], end='')
                elif i == 0:
                    print('     \t' + immunities[i] + ', ', end='')
                else:
                    print(immunities[i] + ', ', end='')



        # Print Data
        print('\n\n     Move List:')
        for i in self.moves:
            moveInfo = moveData[i]
            if len(moveInfo) == 5:
                if moveInfo[4] != 100:
                    state = stateInfo(moveInfo[3],0)
                    damage = moveInfo[2]
                    if moveInfo[1] in self.elements:
                        damage *= 1.5
                        damage = math.ceil(damage)
                    print('     \t' + i + ' (' + moveInfo[1] + ', ' + str(damage) + ' Damage, ' + str(moveInfo[0]) + '% Accuracy, May ' + state)
                else:
                    state = stateInfo(moveInfo[3],1)
                    damage = moveInfo[2]
                    if moveInfo[1] in self.elements:
                        damage *= 1.5
                        damage = math.ceil(damage)
                    print('     \t' + i + ' (' + moveInfo[1] + ', ' + str(damage) + ' Damage, ' + str(moveInfo[0]) + '% Accuracy, ' + state)
            elif type(moveInfo[2]) == int:
                damage = moveInfo[2]
                if moveInfo[1] in self.elements:
                    damage *= 1.5
                    damage = math.ceil(damage)
                print('     \t' + i + ' (' + moveInfo[1] + ', ' + str(damage) + ' Damage, ' + str(moveInfo[0]) + '% Accuracy)')
            else:
                state = stateInfo(moveInfo[2],1)
                print('     \t' + i + ' (' + moveInfo[1] + ', ' + str(moveInfo[0]) + '% Accuracy, ' + state)
        return ''





# Calculates Type Effectiveness
def effectiveness(element1, element2):
    """ Effectiveness Calculator

        Element1 = Attacking type
        Element2 = Defending type

        1. Determines index number of each type (ex. Normal = 0)
        2. Cursor goes down chart by attacking type number
        3. Cursor goes right chart by defending type number
        4. Number at cursor position is effectiveness
    """
    for element in elementList:
        if element1 == element:
            element1 = elementList.index(element)
    for element in elementList:
        if element2 == element:
            element2 = elementList.index(element)
    cursor = 0
    newlines = []
    accumulator = -1
    for i in elementData:
        accumulator += 1
        if i == '\n':
            newlines.append(accumulator)
    for i in range(element1):
        cursor = int(newlines[i])
    if element1 != 0:
        cursor += (2 * element2) + 1
    else:
        cursor += 2 * element2
    effectiveness = int(elementData[cursor])
    if effectiveness == 5:
        effectiveness = 0.5
    return effectiveness





# Calculates Damage from Base Damage
def calculator(aggressor, recipient, baseDamage, element, weather, lightScreen):
    """ Damage Calculator

        1. Determines type effectiveness by move type and recipient types
        2. Multiplies base damage by type effectiveness
        3. Multiplies damage by several factors
            - Burned Pokemon do 1/2 damage
            - Light Screen multiplies damage by 2/3
            - Under rain, Fire does half and Water doubles
        4. Multiplies damage by user's attack multiplier and recipient's defense multiplier
            - x/2 if buffed, 2/x if debuffed
        5. Multiplies damage by STAB (Same Type Attack Bonus)
            - If move type is the Pokemon's type, 1.5x damage
        6. Returns damage and type effectiveness
    """
    if len(recipient.elements) == 2:
        typeMultiplier = effectiveness(element, recipient.elements[0])
        typeMultiplier *= effectiveness(element, recipient.elements[1])
    else:
        typeMultiplier = effectiveness(element, recipient.elements)
    damage = baseDamage
    damage *= typeMultiplier
    if aggressor.status[0] == 'BRN':
        damage *= .5
    if weather[0] == 'Rain' and element == "Fire":
        damage *= .5
    if weather[0] == 'Rain' and element == "Water":
        damage *= 2
    if weather[0] == 'Sandstorm' and 'Rock' in recipient.elements:
        damage *= .5
    if lightScreen > -1:
        damage *= (2 / 3)
    if aggressor.attack / 2 < 1:
        damage *= 2 / (2 + (2 - aggressor.attack))
    else:
        damage *= aggressor.attack / 2
    if recipient.defense / 2 < 1:
        damage /= 2 / (2 + (2 - recipient.defense))
    else:
        damage /= recipient.defense / 2
    if element in aggressor.elements:
        damage *= 1.5
        damage = math.ceil(damage)
    return damage, typeMultiplier





# Process for choosing teams of six
def teamBuilder(team, playerName):
    """ Team Building Process

        1. Display Page
        2. Respond to Input
            - Page Navigation
            - View Team
                - Remove Pkmn
            - Identify Selection
            - Info [Pokemon]
            - Add to team
        3. Display final team
        4. Respond to Input
            - Display Team
            - Remove Pkmn
    """

    # Display Page
    if len(team) == 0:
        input(('\n' * DISPLAY) + '     ' + playerName + ' will now build his/her team.\n\n     >> Press "Enter" to continue. ')
    order = ('first','second','third','fourth','fifth','sixth')
    pageNumber = 0
    if len(pokemonList) < 9:
        nPages = 1
    else:
        nPages = int(math.ceil(len(pokemonList) / 9))
    while len(team) != 6:
        flag = False
        while not flag:
            print(('\n' * DISPLAY) + '     ' + playerName + ", choose your " + order[len(team)] + " Pokemon...\n")
            accumulator = 0
            for i in pokemonList[0+(pageNumber * 9):9+(pageNumber * 9)]:
                accumulator += 1
                number = str((accumulator + (9 * pageNumber)))
                if int(number) < 10:
                    number = "0" + str(number)
                if len(i.elements) == 2:
                    print('     ' + number + " - " + i.name + " (" + i.elements[0] + " / " + i.elements[1] + ")")
                else:
                    print('     ' + number + " - " + i.name + " (" + i.elements + ")")
            choice = input('\n     PAGE ' + str(pageNumber + 1) + ' OF ' + str(nPages) + ' - Navigate by returning "Back" or "Next"\n     Return "page" and number to jump to a specific page.\n\n     Return the name or number of your selection.\n     Return "info" and name or number for Pokemon details.\n     Return "team" to view and edit your team.\n\n     >> ').lower()



            # Page Navigation
            if 'next' in choice:
                if (pageNumber + 1) == nPages:
                    pageNumber = 0
                else:
                    if pageNumber < nPages:
                        pageNumber += 1
            elif 'back' in choice:
                if pageNumber == 0:
                    pageNumber = (nPages - 1)
                else:
                    if pageNumber == 0:
                        pageNumber = (nPages - 1)
                    else:
                        pageNumber -= 1
            elif 'page' in choice:
                newChoice = ''
                for i in choice:
                    if i in '0123456789':
                        newChoice += i
                if int(newChoice) > nPages or int(newChoice) == 0:
                    input(("\n" * DISPLAY) + '     Please enter a valid page number.\n\n     >> Press "Enter" to continue. ')
                else:
                    pageNumber = int(newChoice) - 1



                # View Team
            elif 'team' in choice:
                if not team:
                    input(("\n" * DISPLAY) + '     ' + playerName + "'s team is empty.\n\n" + '     >> Press "Enter" to continue. ')
                    print('\n' * DISPLAY)
                else:
                    print('\n' * DISPLAY)
                    flag1 = False
                    while not flag1:
                        print(("\n" * DISPLAY) + '     ' + playerName + "'s team:\n")
                        for i in range(6):
                            if len(team) - 1 >= i:
                                if len(team[i].elements) == 2:
                                    print('     ' + str(i + 1) + " - " + team[i].name + " (" + str(team[i].maxHP) + 'HP, ' + team[i].elements[0] + " / " + team[i].elements[1] + ")")
                                else:
                                    print('     ' + str(i + 1) + " - " + team[i].name + " (" + str(team[i].maxHP) + 'HP, ' + team[i].elements + ")")
                            else:
                                print('     ' + str(i + 1) + " -")
                        choice = input('\n     Return "remove" and the name or number of a Pokemon to remove it.\n     If you are happy with your team, press "Enter" to add more Pokemon.\n\n     >> ').lower()



                        # Remove Pkmn
                        if 'remove' in choice:
                            chosenPkmn = None
                            inputCheck = False
                            for i in team:
                                if i.name.lower() in choice:
                                    chosenPkmn = i
                            if chosenPkmn == None:
                                for i in range(len(team)):
                                    if str(i + 1) in choice:
                                        chosenPkmn = team[i]
                                if chosenPkmn == None:
                                    input(('\n' * DISPLAY) + '     Please specify a Pokemon to remove by providing its number or name.\n     >> Press "Enter" to continue. ')
                                    inputCheck = True
                            if chosenPkmn != None:
                                team.remove(chosenPkmn)
                                input(('\n' * DISPLAY) + '     ' + chosenPkmn.name + ' has been removed from your team.\n\n     >> Press "Enter" to continue. ')
                                if not team:
                                    flag1 = True
                            else:
                                if inputCheck:
                                    inputCheck = False
                                else:
                                    flag1 = True
                        else:
                            flag1 = True
            else:


                # Identify Selection
                chosenPkmn = None
                inputCheck = False
                for i in pokemonList:
                    if i.name.lower() in choice:
                        chosenPkmn = i()
                if chosenPkmn == None:
                    for i in range(len(pokemonList)):
                        if str(i + 1) in choice:
                            chosenPkmn = pokemonList[i]()



                # Info [Pokemon]
                if 'info' in choice:
                    if chosenPkmn != None:
                        print(chosenPkmn)
                        input('     >> Press "Enter" to continue. ')
                        inputCheck, chosenPkmn = True, None
                    else:
                        input(('\n' * DISPLAY) + '     Please provide the number or name of the ' + 'Pokemon you want to learn about.\n\n     >> Press "Enter" to continue. ')
                        inputCheck = True



                # Add Pokemon
                if chosenPkmn != None:
                    flag = True
                    team.append(chosenPkmn)
                    input(('\n' * DISPLAY) + '     ' + chosenPkmn.name + ' is added to your team.\n\n     >> Press "Enter" to continue. ')
                    print('\n' * DISPLAY)
                else:
                    if not inputCheck:
                        input(("\n" * DISPLAY)+'     Your input could not be understood. Please try again.\n\n     >> Press "Enter" to continue. ')



    # Display final team
    flag = False
    while not flag:
        stepper = 0
        print()
        for i in team:
            stepper += 1
            if len(i.elements) == 2:
                print('     ' + str(stepper) + " - " + i.name + " (" + i.elements[0] + " / " + i.elements[1] + ")")
            else:
                print('     ' + str(stepper) + " - " + i.name + " (" + i.elements + ")")
        choice = input('\n     ' + playerName + ', is this your final team?\n     Return "Yes" or "No".\n\n     >> ').lower()
        if 'no' in choice:
            flag1 = False
            while not flag1:



                # Display team
                print(("\n" * DISPLAY) + '     ' + playerName + "'s team:\n")
                stepper = 0
                for i in team:
                    stepper += 1
                    if len(i.elements) == 2:
                        print('     ' + str(stepper) + " - " + i.name + " (" + i.elements[0] + " / " + i.elements[1] + ")")
                    else:
                        print('     ' + str(stepper) + " - " + i.name + " (" + i.elements + ")")
                choice = input('\n     Return "remove" and the name or number of a Pokemon to remove it.\n\n     If you are happy with your team, press "Enter" to finalize it.\n\n     >> ').lower()



                # Remove Pkmn
                if 'remove' in choice:
                    chosenPkmn = None
                    inputCheck = False
                    for i in team:
                        if i.name.lower() in choice:
                            chosenPkmn = i
                    if chosenPkmn == None:
                        for i in range(len(team)):
                            if str(i + 1) in choice:
                                chosenPkmn = team[i]
                        if chosenPkmn == None:
                            input(('\n' * DISPLAY) + '     Please provide the number or name of ' + 'the Pokemon you would like to remove.\n\n     >> Press "Enter" to continue. ')
                            print('\n' * DISPLAY)
                            inputCheck = True
                    if chosenPkmn != None:
                        team.remove(chosenPkmn)
                        input(('\n' * DISPLAY) + '     ' + chosenPkmn.name + ' has been removed from your team.\n\n     >> Press "Enter" to continue. ')
                        if len(team) != 6:
                            teamBuilder(team, playerName)
                            flag1, flag = True, True
                    else:     
                        if inputCheck:
                            inputCheck = False
                else:
                    flag1 = True
                    print('\n' * DISPLAY)
        elif 'yes' in choice:
            flag = True
            print('\n' * DISPLAY)
        else:
            input(("\n" * DISPLAY) + '     Your input could not be understood. Please try again.\n\n     >> Press "Enter" to continue. ')
            print('\n' * DISPLAY)
    return team





# Players select team order
def orderSelect(name, team, opponentName, opponentTeam):
    """ Order Selection

        1. Team Display
        2. Respond to Input
            - Info [Pokemon]
        3. Create new team
        4. Finalize team
    """

    # Displays teams
    input(('\n' * DISPLAY) + '     ' + name + ' will now select his/her order.\n\n     >> Press "Enter" to continue. ')
    flag = False
    while not flag:
        print(('\n' * DISPLAY) + '     ' + name + "'s team:")
        stepper = 0
        newTeam = []
        for i in team:
            stepper += 1
            if len(i.elements) == 2:
                print('     ' + str(stepper) + " - " + i.name + " (" + str(i.maxHP) + 'HP, ' + i.elements[0] + " / " + i.elements[1] + ")")
            else:
                print('     ' + str(stepper) + " - " + i.name + " (" + str(i.maxHP) + 'HP, ' + i.elements + ")")
        print("\n     " + opponentName + "'s team:")
        for i in opponentTeam:
            if len(i.elements) == 2:
                print("     ? - " + i.name + " (" + str(i.maxHP) + 'HP, ' + i.elements[0] + " / " + i.elements[1] + ")")
            else:
                print("     ? - " + i.name + " (" + str(i.maxHP) + 'HP, ' + i.elements + ")")
        choice = input('\n     Return the order of your team in the form "123456".\n\n     To view more information about a Pokemon, return "info" \n     and its name or number (the number displayed above).\n\n     >> ').lower()



        # Info [Pokemon]
        if 'info' in choice:
            chosenPkmn = None
            for i in pokemonList:
                if i.name.lower() in choice:
                    chosenPkmn = i()
            if chosenPkmn == None:
                for i in range(len(team)):
                    if str(i + 1) in choice:
                        chosenPkmn = team[i]
            if chosenPkmn != None:
                print(chosenPkmn)
                input('     >> Press "Enter" to continue')
            else:
                input(('\n' * DISPLAY) + '     Please provide the number or name of the Pokemon you would like to remove.\n\n     >> Press "Enter" to continue. ')
        else:



            # Create new team
            if "1" in choice and "2" in choice and "3" in choice and "4" in choice and "5" in choice and "6" in choice:
                for i in choice:
                    if i in ('1','2','3','4','5','6'):
                        newTeam.append(team[int(i) - 1])



                # Finalize team
                print('\n' * DISPLAY)
                flag1 = False
                while not flag1:
                    stepper = 0
                    for i in newTeam:
                        stepper += 1
                        if len(i.elements) == 2:
                            print('     ' + str(stepper) + " - " + i.name + " (" + str(i.maxHP) + 'HP, ' + i.elements[0] + " / " + i.elements[1] + ")")
                        else:
                            print('     ' + str(stepper) + " - " + i.name + " (" + str(i.maxHP) + 'HP, ' + i.elements + ")")
                    choice = input('\n     ' + name + ', is this your final team?\n\n     >> ').lower()
                    if 'yes' in choice:
                        flag1, flag = True, True
                        print()
                    elif 'no' not in choice:
                        input(("\n" * DISPLAY) + '     Your input could not be understood. Please try again.\n\n     >> Press "Enter" to continue. ')
                        print('\n' * DISPLAY)
                    elif 'no' in choice:
                        flag1 = True
            else:
                input(("\n" * DISPLAY) + '     Your input could not be understood. Please try again.\n\n     >> Press "Enter" to continue. ')
                print('\n' * DISPLAY)
    return newTeam





# Returns status effect of move
def stateInfo(effect,accuracy):
    """ Status Information

        Checks all possible move effects and returns string
    """
    if effect == 'SLP':
        state = 'Puts to Sleep)'
    elif effect == 'PSN':
        if accuracy:
            state = 'Poisons)'
        else:
            state = 'Poison)'
    elif effect == 'PAR':
        if accuracy:
            state = 'Paralyzes)'
        else:
            state = 'Paralyze)'
    elif effect == 'BRN':
        if accuracy:
            state = 'Burns)'
        else:
            state = 'Burn)'
    elif effect == 'FRZ':
        if accuracy:
            state = 'Freezes)'
        else:
            state = 'Freeze)'
    elif effect == 'BPS':
        state = 'Badly Poisons)'
    elif effect == 'BIND':
        state = 'Binds)'
    elif effect == 'TRAP':
        state = 'Traps)'
    elif effect == 'CONFUSE':
        if accuracy:
            state = 'Confuses)'
        else:
            state = 'Confuse)'
    elif effect == 'LEECH_SEED':
        state = 'Implants)'
    elif effect == 'FLINCH':
        if accuracy:
            state = 'Flinches)'
        else:
            state = 'Flinch)'
    elif effect == 'RECOIL':
        state = 'Takes Recoil)'
    elif effect == 'CHARGE':
        state = 'Takes Two Turns)'
    elif effect == 'ATTACK_DOWN_1' or effect == 'ATTACK_DOWN_2':
        if accuracy:
            state = 'Lowers Attack)'
        else:
            state = 'Lower Attack)'
    elif effect == 'ATTACK_UP_1' or effect == 'ATTACK_UP_2':
        if accuracy:
            state = 'Increases Attack)'
        else:
            state = 'Increase Attack)'
    elif effect == 'DEFENSE_DOWN_1' or effect == 'DEFENSE_DOWN_2':
        if accuracy:
            state = 'Lowers Defense)'
        else:
            state = 'Lower Defense)'
    elif effect == 'DEFENSE_UP_1' or effect == 'DEFENSE_UP_2':
        if accuracy:
            state = 'Increases Defense)'
        else:
            state = 'Increase Defense)'
    elif effect == 'SPEED_DOWN_1' or effect == 'SPEED_DOWN_2':
        if accuracy:
            state = 'Lowers Speed)'
        else:
            state = 'Lower Speed)'
    elif effect == 'SPEED_UP_1' or effect == 'SPEED_UP_2':
        if accuracy:
            state = 'Increases Speed)'
        else:
            state = 'Increase Speed)'
    elif effect == 'ACCURACY_DOWN':
        if accuracy:
            state = 'Lowers Accuracy)'
        else:
            state = 'Lower Accuracy)'
    elif effect == 'PROTECT':
        state = 'Protects)'
    elif effect == 'SPIN':
        state = 'Removes Spikes)'
    elif effect == 'LIGHT_SCREEN':
        state = 'Team Defense Up)'
    elif effect == 'SPIKES':
        state = 'Damages on Switch)'
    elif effect == 'TOXIC_SPIKES':
        state = 'Poisons on Switch)'
    elif effect == 'RAIN':
        state = 'Summons Rain)'
    elif effect == 'SANDSTORM':
        state = 'Summons Sandstorm)'
    elif effect == 'SHELL_SMASH':
        state = 'Defense Down/Attack Up)'
    elif effect == 'QUIVER_DANCE':
        state = 'ATK/DEF/Speed Up)'
    elif effect == 'SUPERPOWER':
        state = 'User ATK+DEF Down)'
    elif effect == 'CLOSE_COMBAT':
        state = 'User DEF Down)'
    elif effect == 'LEAF_STORM':
        state = 'User ATK Down)'
    elif effect == 'FELL_STINGER':
        state = 'ATK Up if Faint)'
    elif effect == 'VENOSHOCK':
        state = 'X2 if Poisoned)'
    elif effect == 'WAKE_UP_SLAP':
        state = '30 if Asleep)'
    elif effect == 'WHIRLWIND':
        state = 'Switches Opponent)'
    elif effect == 'SAFEGUARD':
        state = 'Status Protection)'
    elif effect == 'TAILWIND':
        state = 'Doubles Speed)'
    elif effect == 'ENDEAVOR':
        state = 'Opponent HP = Your HP)'
    elif effect == 'SUCKER_PUNCH':
        state = 'If Attacked)'
    elif effect == 'SUPER_FANG':
        state = "Halves Opponent's HP)"
    elif effect == 'HAZE':
        state = 'Resets All Stats)'
    elif effect == 'ELECTRO_BALL':
        state = 'Speed Difference)'
    elif effect == 'PRIORITY':
        if accuracy:
            state = 'Goes First)'
        else:
            state = 'Go First)'
    elif effect == 'PURSUIT':
        state = 'Hits Before Switch)'
    elif effect == 'SWIFT':
        state = 'Never Misses)'
    elif effect == 'HEAL':
        state = 'Heals 1/2 HP)'
    elif effect == 'REST':
        state = 'Heals/Puts to Sleep)'
    return state





# Displays Battle Information
def display(msg, currentPkmn, name1, name2):
    """ Battle Display

        Returns string including Pokemon names, HP bars, and statuses
    """
    msgLength = 0
    for i in msg:
        if i == '\n':
            msgLength += 1
    display = ('\n' * DISPLAY) + (' ' * (70 - len(currentPkmn[1].name) - len(name2))) + name2 + "'s  " + currentPkmn[1].name + '\n\n' + (' ' * (39 - len(currentPkmn[1].status[0]))) + currentPkmn[1].status[0] + ' HP ' + str(currentPkmn[1].hp) + '/' + str(currentPkmn[1].maxHP) + ' ' + ('.' * round(25 - ((currentPkmn[1].hp / currentPkmn[1].maxHP) * 100) / 4)) + ('|' * round(((currentPkmn[1].hp / currentPkmn[1].maxHP) * 100) / 4)) + '\n\n     ' + name1 + "'s  " + currentPkmn[0].name + '\n\n     ' + ('|' * round(((currentPkmn[0].hp / currentPkmn[0].maxHP) * 100) / 4) + ('.' * round(25 - ((currentPkmn[0].hp / currentPkmn[0].maxHP) * 100) / 4))) + ' HP ' + str(currentPkmn[0].hp) + '/' + str(currentPkmn[0].maxHP) + ' ' + currentPkmn[0].status[0] + ('\n' * (13 - msgLength) + msg) + '\n\n     >> '
    return display





# Singles Battle System
def battleSystem(name1, team1, name2, team2):
    """ Battle System

        1. Reset Board Data
        2. Determine 50 Turn Tie
        3. Display Attacks
        4. Interpret Choice
            - Info [Pokemon]
            - Finalize Attack
            - Switch Pokemon
                - Info [Pokemon]
                - Finalize Switch
            - Forfeit Match
        5. Switch Pokemon
        6. Determine Speeds
        7. Priority Update
            - Priority Moves
            - Sucker Punch
            - Protect
        8. Use Moves
            - Check Faint, Switch, Charge, Whirlwind, Pursuit
                - Check Status
                    - Check Accuracy
                        - Damaging Attacks
                            - Calculate & Perform Attack
                            - Added Effect
                                - Main Status
                                - Secondary Status
                                - Buffs/Debuffs
                                - Other
                        - Status Moves
                            - Main Status
                            - Secondary Status
                            - Buffs/Debuffs
                            - Other
        9. Status Damage
        10. Update Board Data
        11. Fainted Pokemon
            - Display Pokemon
            - Info [Pokemon]
            - Switch Pokemon
            - Battle End
    """

    # Reset Board Data
    input(("\n" * DISPLAY) + "     Next, the battle will begin.\n\n     Remember, don't look " + 'while your opponent is selecting their action!\n\n     >> Press "Enter" to continue. ')
    input(('\n' * DISPLAY) + (' ' * 35) + "BATTLE BEGIN!" + ('\n' * 12))
    input(('\n' * DISPLAY) + '     ' + name1 + ' sends out ' + team1[0].name + '!\n\n     >> Press "Enter to continue. ')
    input(('\n' * DISPLAY) + '     ' + name1 + ' sends out ' + team1[0].name + '!' + '\n\n     ' + name2 + ' sends out ' + team2[0].name + '!\n\n     >> Press "Enter" to continue. ')
    for a in [team1,team2]:
        for i in a:
            i.hp = i.maxHP
            i.status = ['',0,'',0,'',0]
            i.charge = 0
            i.attack = 2
            i.defense = 2
            i.speed = 1
            i.accuracy = 1
            i.protect = [0,0]
    turnNumber = 0
    spikes = [0,0]  # Player 1, Player 2
    safeguard = [0,0]
    lightScreen = [-1,-1]
    tailwind = [0,0]
    weather = ["",0]  # "Rain" , number of turns left
    move1, move2 = '', ''
    currentPkmn = [team1[0],team2[0]]
    repeat = ([name1, team1, move1],[name2, team2, move2])
    flag = False
    while not flag:
        turnNumber += 1



        # Determine 50 Turn Tie
        if turnNumber == 51:
            fainted1 = 0
            fainted2 = 0
            for i in team1:
                if i.hp == 0:
                    fainted1 += 1
            for i in team2:
                if i.hp == 0:
                    fainted2 += 1
            if fainted1 > fainted2:
                input(('\n' * DISPLAY) + (' ' * 35) + name2.upper() + " WON!" + ('\n' * 12))
                return name2
            elif fainted1 < fainted2:
                input(('\n' * DISPLAY) + (' ' * 35) + name1.upper() + " WON!" + ('\n' * 12))
                return name1
            else:
                percent1 = 0
                percent2 = 0
                for i in team1:
                    fainted1 += i.hp / i.maxHP
                for i in team2:
                    fainted2 += i.hp / i.maxHP
                if fainted1 < fainted2:
                    input(('\n' * DISPLAY) + (' ' * 35) + name2.upper() + " WON!" + ('\n' * 12))
                    return name2
                elif fainted1 > fainted2:
                    input(('\n' * DISPLAY) + (' ' * 35) + name1.upper() + " WON!" + ('\n' * 12))
                    return name1



        # Display Attacks
        for i in repeat:
            if currentPkmn[repeat.index(i)].charge != 1:
                input(('\n' * DISPLAY) + '     ' + i[0] + "'s turn!\n\n     >> Press " + '"Enter" to continue. ')
                names = []
                for pkmn in i[1]:
                    names.append(pkmn.name.lower())
                moves = []
                for move in currentPkmn[repeat.index(i)].moves:
                    moves.append(move.lower())
                flag1 = False
                while not flag1:
                    msg = ''
                    accumulator = 0
                    for move in currentPkmn[repeat.index(i)].moves: 
                        accumulator += 1
                        moveInfo = moveData[move]
                        if len(moveInfo) == 5:
                            if moveInfo[4] != 100:
                                state = stateInfo(moveInfo[3],0)
                                damage = moveInfo[2]
                                if moveInfo[1] in currentPkmn[repeat.index(i)].elements:
                                    damage *= 1.5
                                    damage = math.ceil(damage)
                                msg += '     ' + str(accumulator) + '  -  "' + move + '"  (' + moveInfo[1] + ', ' + str(damage) + ' Damage, ' + str(moveInfo[0]) + '% Accuracy, May ' + state + '\n'
                            else:
                                state = stateInfo(moveInfo[3],1)
                                damage = moveInfo[2]
                                if moveInfo[1] in currentPkmn[repeat.index(i)].elements:
                                    damage *= 1.5
                                    damage = math.ceil(damage)
                                msg += '     ' + str(accumulator) + '  -  "' + move + '"  (' + moveInfo[1] + ', ' + str(damage) + ' Damage, ' + str(moveInfo[0]) + '% Accuracy, ' + state + '\n'
                        elif type(moveInfo[2]) is int:
                            damage = moveInfo[2]
                            if moveInfo[1] in currentPkmn[repeat.index(i)].elements:
                                damage *= 1.5
                                damage = math.ceil(damage)
                            msg += '     ' + str(accumulator) + '  -  "' + move + '"  (' + moveInfo[1] + ', ' + str(damage) + ' Damage, ' + str(moveInfo[0]) + '% Accuracy)\n'
                        else:
                            state = stateInfo(moveInfo[2],1)
                            msg += '     ' + str(accumulator) + '  -  "' + move + '"  (' + moveInfo[1] + ', ' + str(moveInfo[0]) + '% Accuracy, ' + state + '\n'
                    msg += '\n     5  -  "Switch"  Pokemon\n     6  -  "Forfeit"  Battle\n\n     Return "Info" and Name to learn more about a Pokemon.\n\n     ' + i[0] + ', input a command:'
                    choice = input(display(msg,currentPkmn,name1,name2)).lower()



                    # Info [Pokemon]
                    if 'info' in choice:
                        chosenPkmn = None
                        for pkmn in pokemonList:
                            if pkmn.name.lower() in choice:
                                chosenPkmn = pkmn()
                        if chosenPkmn == None:
                            for pkmn in range(len(i[1])):
                                if str(pkmn + 1) in choice:
                                    chosenPkmn = i[1][pkmn]
                        if chosenPkmn != None:
                            print('\n' * DISPLAY)
                            print(chosenPkmn)
                            input('     >> Press "Enter" to continue')
                        else:
                            input(display("     Please provide the number or name of the Pokemon you\n     would like to learn more about.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()



                        # Finalize Attack
                    elif '1' == choice or currentPkmn[repeat.index(i)].moves[0].lower() in choice:
                        if choice == '1':
                            finalize = input(display('     Use ' + currentPkmn[repeat.index(i)].moves[int(choice) - 1] + '?',currentPkmn,name1,name2)).lower()
                            if finalize == 'yes':
                                i[2] = 'attack' + str(int(choice) - 1)
                                flag1 = True
                        else:
                            finalize = input(display('     Use ' + choice.title() + '?',currentPkmn,name1,name2)).lower()
                            if finalize == 'yes':
                                i[2] = 'attack' + str(moves.index(choice))
                                flag1 = True
                    elif '2' == choice or currentPkmn[repeat.index(i)].moves[1].lower() in choice:
                        if choice == '2':
                            finalize = input(display('     Use ' + currentPkmn[repeat.index(i)].moves[int(choice) - 1] + '?',currentPkmn,name1,name2)).lower()
                            if finalize == 'yes':
                                i[2] = 'attack' + str(int(choice) - 1)
                                flag1 = True
                        else:
                            finalize = input(display('     Use ' + choice.title() + '?',currentPkmn,name1,name2)).lower()
                            if finalize == 'yes':
                                i[2] = 'attack' + str(moves.index(choice))
                                flag1 = True
                    elif '3' == choice or currentPkmn[repeat.index(i)].moves[2].lower() in choice:
                        if choice == '3':
                            finalize = input(display('     Use ' + currentPkmn[repeat.index(i)].moves[int(choice) - 1] + '?',currentPkmn,name1,name2)).lower()
                            if finalize == 'yes':
                                i[2] = 'attack' + str(int(choice) - 1)
                                flag1 = True
                        else:
                            finalize = input(display('     Use ' + choice.title() + '?',currentPkmn,name1,name2,repeat.index(i))).lower()
                            if finalize == 'yes':
                                i[2] = 'attack' + str(moves.index(choice))
                                flag1 = True
                    elif '4' == choice or currentPkmn[repeat.index(i)].moves[3].lower() in choice:
                        if choice == '4':
                            finalize = input(display('     Use ' + currentPkmn[repeat.index(i)].moves[int(choice) - 1] + '?',currentPkmn,name1,name2)).lower()
                            if finalize == 'yes':
                                i[2] = 'attack' + str(int(choice) - 1)
                                flag1 = True
                        else:
                            finalize = input(display('     Use ' + choice.title() + '?',currentPkmn,name1,name2)).lower()
                            if finalize == 'yes':
                                i[2] = 'attack' + str(moves.index(choice))
                                flag1 = True



                        # Switch Pokemon
                    elif '5' == choice or 'switch' in choice:
                        if currentPkmn[repeat.index(i)].status[2] == 'TRAP':
                            input(display('     ' + currentPkmn[repeat.index(i)].name + " is trapped by " + currentPkmn[repeat.index(i)].status[4] + "! You can't switch!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        else:
                            msg = ''
                            accumulator = 0
                            for pkmn in i[1]:
                                accumulator += 1
                                pkmnStatus = ' ' + pkmn.status[0]
                                if pkmn.hp > 0:
                                    if len(pkmn.elements) == 2:
                                        msg += '     ' + str(accumulator) + '  -  "' + pkmn.name + '"  (' + str(pkmn.hp) + '/' + str(pkmn.maxHP) + 'HP,  ' + pkmn.elements[0] + ' / ' + pkmn.elements[1] + ')' + pkmnStatus + '\n'
                                    else:
                                        msg += '     ' + str(accumulator) + '  -  "' + pkmn.name + '"  (' + str(pkmn.hp) + '/' + str(pkmn.maxHP) + 'HP,  ' + pkmn.elements + ')' + pkmnStatus + '\n'
                                else:
                                    if len(pkmn.elements) == 2:
                                        msg += '     X  -  "' + pkmn.name + '"  (0/' + str(pkmn.maxHP) + 'HP,  ' + pkmn.elements[0] + ' / ' + pkmn.elements[1] + ')' + pkmnStatus + '\n'
                                    else:
                                        msg += '     X  -  "' + pkmn.name + '"  (0/' + str(pkmn.maxHP) + 'HP,  ' + pkmn.elements + ')' + pkmnStatus + '\n'
                            msg += '     7  -  "Back"  to  Menu  Select\n\n     Return  "Info"  &  Number/Name  for  more  details\n\n     ' + i[0] + ', input a command:'
                            flag2 = False
                            while not flag2:
                                choice = input(display(msg,currentPkmn,name1,name2)).lower()



                                # Info [Pokemon]
                                if 'info' in choice:
                                    chosenPkmn = None
                                    for pkmn in pokemonList:
                                        if pkmn.name.lower() in choice:
                                            chosenPkmn = pkmn()
                                    if chosenPkmn == None:
                                        for pkmn in range(len(i[1])):
                                            if str(pkmn + 1) in choice:
                                                chosenPkmn = i[1][pkmn]
                                    if chosenPkmn != None:
                                        print('\n' * DISPLAY)
                                        print(chosenPkmn)
                                        input('     >> Press "Enter" to continue')
                                    else:
                                        input(display("     Please provide the number or name of the Pokemon you\n     would like to learn more about.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()



                                    # Finalize Switch
                                elif '1' == choice or '2' == choice or '3' == choice or '4' == choice or '5' == choice or '6' == choice:
                                    if i[1][int(choice) - 1].hp < 1:
                                        input(display("     You cannot switch to a fainted Pokemon.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()
                                    elif i[1][int(choice) - 1] == currentPkmn[repeat.index(i)]:
                                        input(display("     " + currentPkmn[repeat.index(i)].name + " is already in battle.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()
                                    else:
                                        finalize = input(display('     Switch to ' + names[int(choice) - 1].capitalize() + '?',currentPkmn,name1,name2)).lower()
                                        if finalize == 'yes':
                                            i[2] = 'switch' + str(int(choice) - 1)
                                            flag2, flag1 = True, True
                                elif choice in names:
                                    if i[1][names.index(choice)].hp < 1:
                                        input(display("     You cannot switch to a fainted Pokemon.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()
                                    elif i[1][names.index(choice)] == currentPkmn[repeat.index(i)]:
                                        input(display("     " + currentPkmn[repeat.index(i)].name + " is already in battle.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()
                                    else:
                                        finalize = input(display('     Switch to ' + choice.capitalize() + '?',currentPkmn,name1,name2)).lower()
                                        if finalize == 'yes':
                                            i[2] = 'switch' + str(names.index(choice))
                                            flag2, flag1 = True, True
                                elif '7' in choice or 'back' in choice:
                                    flag2 = True
                                else:
                                    input(display("     Your input could not be understood. Please try again.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()
                        # Forfeit Match
                    elif '6' in choice or 'forfeit' in choice:
                        input(('\n' * DISPLAY) + '     ' + i[0] + ' forfeited the match!\n\n     >> Press "Enter" to continue. ')
                        return False
                    else:
                        input(display("     Your input could not be understood. Please try again.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()



        if turnNumber == 50:
            input(('\n' * DISPLAY) + (' ' * 38) + "FINAL TURN!" + ('\n' * 12))
        else:
            input(('\n' * DISPLAY) + (' ' * 38) + "TURN #" + str(turnNumber) + ('\n' * 12))
        if weather[0] == 'Rain':
            input(display('     It continues to rain...',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
        elif weather[0] == 'Sandstorm':
            input(display('     The sandstorm continues...',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
        debugtext = '\nP1 team:\n'
        for team in (repeat[0][1],repeat[1][1]):
            for i in team:
                debugtext += str(i.name) + ': '
                debugtext += str(i.hp) + ' HP, '
                debugtext += str(i.status) + ' Status, '
                debugtext += str(i.charge) + ' Charge, '
                debugtext += str(i.attack) + ' Attack, '
                debugtext += str(i.defense) + ' Defense, '
                debugtext += str(i.speed) + ' Speed, '
                debugtext += str(i.accuracy) + ' Accuracy, '
                debugtext += str(i.protect) + ' Protect\n'
            if team == repeat[0][1]:
                debugtext += '\nP2 team:\n'
        debug('Turn number: ' + str(turnNumber) + '\nWeather: ' + weather[0] + ', ' + str(weather[1]) + '\nSpikes: ' + str(spikes[0]) + ', ' + str(spikes[1]) + '\nSafeguard: ' + str(safeguard[0]) + ', ' + str(safeguard[1]) + '\nTailwind: ' + str(tailwind[0]) + ', ' + str(tailwind[1]) + '\nLight Screen: ' + str(lightScreen[0]) + ', ' + str(lightScreen[1]) + '\nP1 name: ' + str(repeat[0][0]) + '\nP2 name: ' + str(repeat[1][0]) + '\nP1 pokemon: ' + str(currentPkmn[0].name) + '\nP2 pokemon: ' + str(currentPkmn[1].name) + '\nP1 attack: ' + str(repeat[0][2]) + '\nP2 attack: ' + str(repeat[1][2]) + debugtext)



        # Switch Pokemon
        pursuitCheck = [False,False]
        if 'switch' in repeat[0][2]:
            if 'switch' not in repeat[1][2]:
                if 'Pursuit' == currentPkmn[1].moves[int(repeat[1][2][6])]:
                    pursuitCheck[1] = True
                    damage, typeEffectiveness = calculator(currentPkmn[1],currentPkmn[0],moveData[currentPkmn[1].moves[int(repeat[1][2][6])]][2],moveData[currentPkmn[1].moves[int(repeat[1][2][6])]][1],weather,lightScreen[0])
                    currentPkmn[0].hp -= damage
                    if typeEffectiveness != 1:
                        if typeEffectiveness == 0:
                            input(display('     ' + name2 + "'s " + currentPkmn[1].name + ' uses Pursuit!\n\n     But the opposing ' + currentPkmn[0].name + ' is immune!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        elif typeEffectiveness < 1:
                            input(display('     ' + name2 + "'s " + currentPkmn[1].name + " uses Pursuit!\n\n     It's not very effective...",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        else:
                            input(display('     ' + name2 + "'s " + currentPkmn[1].name + " uses Pursuit!\n\n     It's super effective!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ') 
                    else:
                        input(display('     ' + name2 + "'s " + currentPkmn[1].name + ' uses Pursuit!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
            if currentPkmn[0].hp != 0:
                currentPkmn[0].attack, currentPkmn[0].defense, currentPkmn[0].speed = 2, 2, 1
                currentPkmn[0] = team1[int(repeat[0][2][6])]
                input(display('     ' + name1 + ' switches to ' + currentPkmn[0].name + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                if spikes[0] == 1:
                    currentPkmn[0].hp -= 10
                    input(display('     ' + name1 + ' switches to ' + currentPkmn[0].name + '!\n\n     ' + currentPkmn[0].name + ' takes damage from spikes!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                elif spikes[0] == 2 and "Poison" not in currentPkmn[0].elements:
                    currentPkmn[0].status[0], currentPkmn[0].status[1] = "PSN", -1
                    input(display('     ' + name1 + ' switches to ' + currentPkmn[0].name + '!\n\n     ' + currentPkmn[0].name + ' is poisoned by Toxic Spikes!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
        if 'switch' in repeat[1][2]:
            if 'switch' not in repeat[0][2]:
                if 'Pursuit' == currentPkmn[0].moves[int(repeat[0][2][6])]:
                    pursuitCheck[0] = True
                    damage, typeEffectiveness = calculator(currentPkmn[0],currentPkmn[1],moveData[currentPkmn[0].moves[int(repeat[0][2][6])]][2],moveData[currentPkmn[0].moves[int(repeat[0][2][6])]][1],weather,lightScreen[1])
                    currentPkmn[1].hp -= damage
                    if typeEffectiveness != 1:
                        if typeEffectiveness == 0:
                            input(display('     ' + name1 + "'s " + currentPkmn[0].name + ' uses Pursuit!\n\n     But the opposing ' + currentPkmn[1].name + ' is immune!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        elif typeEffectiveness < 1:
                            input(display('     ' + name1 + "'s " + currentPkmn[0].name + " uses Pursuit!\n\n     It's not very effective...",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        else:
                            input(display('     ' + name1 + "'s " + currentPkmn[0].name + " uses Pursuit!\n\n     It's super effective!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ') 
                    else:
                        input(display('     ' + name1 + "'s " + currentPkmn[0].name + ' uses Pursuit!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
            if currentPkmn[1].hp != 0:
                currentPkmn[1].attack, currentPkmn[1].defense, currentPkmn[1].speed = 2, 2, 1
                currentPkmn[1] = team2[int(repeat[1][2][6])]
                input(display('     ' + name2 + ' switches to ' + currentPkmn[1].name + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                if spikes[1] == 1:
                    currentPkmn[1].hp -= 10
                    input(display('     ' + name2 + ' switches to ' + currentPkmn[1].name + '!\n\n     ' + currentPkmn[1].name + ' takes damage from spikes!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                elif spikes[1] == 2 and "Poison" not in currentPkmn[1].elements:
                    currentPkmn[1].status[0], currentPkmn[1].status[1] = "PSN", -1
                    input(display('     ' + name2 + ' switches to ' + currentPkmn[1].name + '!\n\n     ' + currentPkmn[1].name + ' is poisoned by Toxic Spikes!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')



        # Determine Speeds
        speeds = [0,0]
        speeds[0], speeds[1] = currentPkmn[0].maxHP * currentPkmn[0].speed, currentPkmn[1].maxHP * currentPkmn[1].speed
        for i in range(2):
            if currentPkmn[i].status[0] == 'PAR':
                speeds[i] *= 2
                speeds[i] = math.ceil(speeds[i])
            if tailwind[i] > 0:
                speeds[i] *= .5
                speeds[i] = math.ceil(speeds[i])
        order = []
        if speeds[0] < speeds[1]:
            order.append([repeat[0][0],repeat[0][2],currentPkmn[0],team1])
            order.append([repeat[1][0],repeat[1][2],currentPkmn[1],team2])
            electroBall = speeds[1] - speeds[0]
        elif speeds[0] > speeds[1]:
            order.append([repeat[1][0],repeat[1][2],currentPkmn[1],team2])
            order.append([repeat[0][0],repeat[0][2],currentPkmn[0],team1])
            electroBall = speeds[0] - speeds[1]
        else:
            electroBall = 1
            if random.randint(0,1) == 0:
                order.append([repeat[0][0],repeat[0][2],currentPkmn[0],team1])
                order.append([repeat[1][0],repeat[1][2],currentPkmn[1],team2])
            else:
                order.append([repeat[1][0],repeat[1][2],currentPkmn[1],team2])
                order.append([repeat[0][0],repeat[0][2],currentPkmn[0],team1])



        # Priority Moves
        suckerPunch = 0
        newOrder = []
        if 'switch' not in order[1][1] and 'switch' not in order[0][1]:
            if len(moveData[order[1][2].moves[int(order[1][1][6])]]) > 3:
                if len(moveData[order[0][2].moves[int(order[0][1][6])]]) > 3:
                    if moveData[order[0][2].moves[int(order[0][1][6])]][3] != 'PRIORITY' and moveData[order[1][2].moves[int(order[1][1][6])]][3] == 'PRIORITY':
                        newOrder = []
                        newOrder.append(order[1])
                        newOrder.append(order[0])
                        order = newOrder
                else:
                    if moveData[order[1][2].moves[int(order[1][1][6])]][3] == 'PRIORITY':
                        newOrder = []
                        newOrder.append(order[1])
                        newOrder.append(order[0])
                        order = newOrder


                        
        # Sucker Punch
        if 'switch' not in order[1][1]:
            if 'switch' not in order[0][1]:
                if len(moveData[order[1][2].moves[int(order[1][1][6])]]) > 3:
                    if moveData[order[1][2].moves[int(order[1][1][6])]][3] == 'SUCKER_PUNCH':
                        if type(moveData[order[0][2].moves[int(order[0][1][6])]][2]) == int:
                            suckerPunch = 1
                            newOrder = []
                            newOrder.append(order[1])
                            newOrder.append(order[0])
                        else:
                            suckerPunch = 2
                            newOrder = []
                            newOrder.append(order[1])
                            newOrder.append(order[0])
            else:
                if len(moveData[order[1][2].moves[int(order[1][1][6])]]) > 3:
                    if moveData[order[1][2].moves[int(order[1][1][6])]][3] == 'SUCKER_PUNCH':
                        suckerPunch = 2
        if 'switch' not in order[0][1]:
            if 'switch' not in order[1][1]:
                if len(moveData[order[0][2].moves[int(order[0][1][6])]]) > 3:
                    if moveData[order[0][2].moves[int(order[0][1][6])]][3] == 'SUCKER_PUNCH':
                        if type(moveData[order[1][2].moves[int(order[1][1][6])]][2]) == int:
                            suckerPunch = 1
                            newOrder = order
                        else:
                            suckerPunch = 2
            else:
                if len(moveData[order[0][2].moves[int(order[0][1][6])]]) > 3:
                    if moveData[order[0][2].moves[int(order[0][1][6])]][3] == 'SUCKER_PUNCH':
                        suckerPunch = 2
        if newOrder:
            order = newOrder



        # Protect
        if 'switch' not in order[1][1]:
            if moveData[order[1][2].moves[int(order[1][1][6])]][2] == 'PROTECT':
                newOrder = []
                newOrder.append(order[1])
                newOrder.append(order[0])
                order = newOrder



        # Check Faint, Switch, Charge, Whirlwind, Pursuit
        whirlwind = False
        for i in order:
            if int(i[1][6]) > 3:
                ifPursuit = False
            else:
                if order.index(i) == 0:
                    if pursuitCheck[0]:
                        ifPursuit = True
                    else:
                        ifPursuit = False
                else:
                    if pursuitCheck[1]:
                        ifPursuit = True
                    else:
                        ifPursuit = False
            charge = False
            if 'switch' not in i[1]:
                if len(moveData[i[2].moves[int(i[1][6])]]) > 3:
                    if moveData[i[2].moves[int(i[1][6])]][3] == 'CHARGE' and i[2].charge == 0:
                        charge = True
                    if charge:
                        i[2].charge = 1
                        input(display('     ' + i[0] + "'s " + i[2].name + ' is charging ' + i[2].moves[int(i[1][6])] + '...',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
            if i[2].hp != 0 and not whirlwind and not ifPursuit and 'switch' not in i[1] and not charge:



                # Check Status
                if order.index(i) == 0:
                    recipient = order[1][2]
                    spCheck = order[1][1]
                else:
                    recipient = order[0][2]
                    spCheck = order[0][1]
                attack = True
                if order.index(i) == 0 and suckerPunch == 2 or 'switch' in spCheck and suckerPunch == 2:
                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it failed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                    attack = False
                if i[2].status[5]:
                    input(display('     ' + i[0] + "'s " + i[2].name + ' flinches. It cannot move!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                    i[2].status[5] = 0
                    attack = False
                if i[2].status[0] == 'PAR':
                    input(display('     ' + i[0] + "'s " + i[2].name + ' is paralyzed...',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                    if random.randint(0,3) == 0:
                        attack = False
                        input(display('     ' + i[0] + "'s " + i[2].name + ' is paralyzed...\n\n     It cannot move!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                if i[2].status[2] == 'CONFUSE':
                    if i[2].status[3] != 0:
                        input(display('     ' + i[0] + "'s " + i[2].name + ' is confused...',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        if random.randint(0,2) == 0:
                            attack = False
                            i[2].hp -= i[2].maxHP / 8
                            input(display('     ' + i[0] + "'s " + i[2].name + ' is confused...\n\n     It hurts itself in confusion!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                    else:
                        i[2].status[2] = ''
                        input(display('     ' + i[0] + "'s " + i[2].name + ' snaps out of confusion!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                if i[2].status[0] == 'FRZ':
                    input(display('     ' + i[0] + "'s " + i[2].name + ' is frozen...',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                    if i[2].status[0] == 'FRZ' and moveData[i[2].moves[int(i[1][6])]][1] == 'Fire':
                        i[2].status[0], i[2].status[1] = '', 0
                        input(display('     ' + i[0] + "'s " + i[2].name + ' is frozen...\n\n     But it thaws out!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                    else:
                        if random.randint(0,4) != 0:
                            attack = False
                            input(display('     ' + i[0] + "'s " + i[2].name + ' is frozen...\n\n     It cannot move!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        else:
                            i[2].status[0], i[2].status[1] = '', 0
                            input(display('     ' + i[0] + "'s " + i[2].name + ' is frozen...\n\n     But it thaws out!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                if i[2].status[0] == 'SLP':
                    if i[2].status[1] != 0:
                        input(display('     ' + i[0] + "'s " + i[2].name + ' is asleep.',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        attack = False
                    else:
                        i[2].status[0] = ''
                        input(display('     ' + i[0] + "'s " + i[2].name + ' wakes up!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                if attack:



                    # Check Accuracy
                    if currentPkmn[0] == i[2]:
                        indexNumber = 0
                        oppositeIndex = 1
                    else:
                        indexNumber = 1
                        oppositeIndex = 0
                    accuracy = moveData[i[2].moves[int(i[1][6])]][0] * i[2].accuracy
                    if 'Swift' == i[2].moves[int(i[1][6])] or 'Thunder' == i[2].moves[int(i[1][6])] and weather[0] == 'Rain' or 'Hurricane' == i[2].moves[int(i[1][6])] and weather[0] == 'Rain':
                        accuracy = 100
                    if accuracy == 100 or random.randint(0, 100) <= accuracy:



                        # Damaging Attacks
                        if type(moveData[i[2].moves[int(i[1][6])]][2]) == int:



                            # Calculate & Perform Attack
                            damage, typeEffectiveness = calculator(i[2],recipient,moveData[i[2].moves[int(i[1][6])]][2],moveData[i[2].moves[int(i[1][6])]][1],weather,lightScreen[oppositeIndex])
                            if typeEffectiveness == 1:
                                protecting = False
                                damage, typeMultiplier = calculator(i[2],recipient,moveData[i[2].moves[int(i[1][6])]][2],moveData[i[2].moves[int(i[1][6])]][1],weather,lightScreen[oppositeIndex])
                                if len(moveData[i[2].moves[int(i[1][6])]]) > 3:
                                    if moveData[i[2].moves[int(i[1][6])]][3] == "VENOSHOCK" and recipient.status[0] == "PSN" or moveData[i[2].moves[int(i[1][6])]][3] == "VENOSHOCK" and recipient.status[0] == "BPS" or moveData[i[2].moves[int(i[1][6])]][3] == "WAKE_UP_SLAP" and recipient.status[0] == "SLP":
                                        damage *= 2
                                if recipient.protect[0] == 1:
                                    if random.randint(0,recipient.protect[1]) == 0:
                                        protecting = True
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it was blocked by ' + recipient.name + "'s Protect!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        recipient.hp -= damage
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                else:
                                    recipient.hp -= damage
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')                      
                                if recipient.status[0] == 'FRZ' and moveData[i[2].moves[int(i[1][6])]][1] == 'Fire':
                                    recipient.status[0], recipient.status[1] = '', 0
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' thaws out!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            else:
                                damage, typeMultiplier = calculator(i[2],recipient,moveData[i[2].moves[int(i[1][6])]][2],moveData[i[2].moves[int(i[1][6])]][1],weather,lightScreen[oppositeIndex])
                                protecting = False
                                if recipient.protect[0] == 1:
                                    if random.randint(0,recipient.protect[1]) == 0:
                                        protecting = True
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it was blocked by ' + recipient.name + "'s Protect!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        recipient.hp -= damage
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        if typeMultiplier == 0:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But the opposing ' + recipient.name + ' is immune!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        elif typeMultiplier < 1:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It's not very effective...",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        else:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It's super effective!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ') 
                                else:
                                    recipient.hp -= damage
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    if typeMultiplier == 0:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But the opposing ' + recipient.name + ' is immune!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif typeMultiplier < 1:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It's not very effective...",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It's super effective!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')                  
                                if recipient.status[0] == 'FRZ' and moveData[i[2].moves[int(i[1][6])]][1] == 'Fire':
                                    recipient.status[0], recipient.status[1] = '', 0
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' thaws out!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')



                            # Added Effect
                            if len(moveData[i[2].moves[int(i[1][6])]]) == 5 and recipient.hp != 0:
                                accuracy = moveData[i[2].moves[int(i[1][6])]][4]
                                if accuracy == 100 or random.randint(0, 100) <= accuracy:



                                    # Main Status
                                    if moveData[i[2].moves[int(i[1][6])]][3] == 'PAR' or moveData[i[2].moves[int(i[1][6])]][3] == 'PSN' or moveData[i[2].moves[int(i[1][6])]][3] == 'BRN' or moveData[i[2].moves[int(i[1][6])]][3] == 'FRZ':
                                        if 'Electric' not in recipient.elements and moveData[i[2].moves[int(i[1][6])]][3] == 'PAR':
                                            if not protecting:
                                                recipient.status[0], recipient.status[1] = moveData[i[2].moves[int(i[1][6])]][3],-1
                                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' is paralyzed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        elif 'Poison' not in recipient.elements and moveData[i[2].moves[int(i[1][6])]][3] == 'PSN':
                                            if not protecting:
                                                recipient.status[0], recipient.status[1] = moveData[i[2].moves[int(i[1][6])]][3],-1
                                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' is poisoned!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        elif 'Fire' not in recipient.elements and moveData[i[2].moves[int(i[1][6])]][3] == 'BRN':
                                            if not protecting:
                                                recipient.status[0], recipient.status[1] = moveData[i[2].moves[int(i[1][6])]][3],-1
                                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' is burnt!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        elif 'Ice' not in recipient.elements and moveData[i[2].moves[int(i[1][6])]][3] == 'FRZ':
                                            if not protecting:
                                                recipient.status[0], recipient.status[1] = moveData[i[2].moves[int(i[1][6])]][3],-1
                                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' is frozen!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'BPS':
                                        if 'Poison' not in recipient.elements:
                                            if not protecting:
                                                recipient.status[0], recipient.status[1] = 'BPS', 0
                                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The opposing ' + recipient.name + ' is badly poisoned!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'SLP':
                                        if 'Grass' not in recipient.elements:
                                            if not protecting:
                                                if recipient.status[0] != 'SLP':
                                                    recipient.status[0], recipient.status[1] = 'SLP',random.randint(2,4)
                                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The opposing ' + recipient.name + ' is put to sleep!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                                else:
                                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it failed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')



                                        # Secondary Status
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'BIND' and safeguard[oppositeIndex] != 1:
                                        if moveData[i[2].moves[int(i[1][6])]][1] not in recipient.elements:
                                            if not protecting:
                                                recipient.status[2], recipient.status[3], recipient.status[4] = 'BIND', random.randint(5,6), i[2].moves[int(i[1][6])]
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'TRAP' and safeguard[oppositeIndex] != 1:
                                        recipient.status[2], recipient.status[3], recipient.status[4] = 'TRAP', random.randint(3,6), i[2].moves[int(i[1][6])]
                                        input(display('     The opposing ' + recipient.name + ' is trapped by ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'CONFUSE' and safeguard[oppositeIndex] != 1:
                                        if not protecting:
                                            recipient.status[2], recipient.status[3] = 'CONFUSE', random.randint(2,5)
                                            input(display('     The opposing ' + recipient.name + ' becomes confused!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'LEECH_SEED' and safeguard[oppositeIndex] != 1:
                                        if 'Grass' not in recipient.elements:
                                            if not protecting:
                                                recipient.status[2], recipient.status[3] = 'LEECH_SEED', -1
                                                input(display('     The opposing ' + recipient.name + ' is implanted by Leech Seed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'FLINCH':
                                        if not protecting:
                                            recipient.status[5] = 1



                                        # Buffs/Debuffs
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'ATTACK_DOWN_1':
                                        if not protecting:
                                            recipient.attack -= 1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Attack fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'ATTACK_UP_1':
                                        i[2].attack += 1
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Attack rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'ATTACK_UP_2':
                                        i[2].attack += 2
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Attack sharply rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'DEFENSE_DOWN_1':
                                        if not protecting:
                                            recipient.defense -= 1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Defense fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'DEFENSE_UP_1':
                                        if not protecting:
                                            i[2].defense += 1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Defense rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'DEFENSE_DOWN_2':
                                        if protecting:
                                            recipient.defense -= 2
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Defense harshly fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'ACCURACY_DOWN':
                                        if not protecting:
                                            recipient.accuracy -= .1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Accuracy fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'SPEED_DOWN_1':
                                        if not protecting:
                                            recipient.speed *= 1.2
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Speed fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'SPEED_DOWN_2':
                                        if not protecting:
                                            recipient.speed *= 1.44
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Speed sharply fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'SPEED_UP_1':
                                        i[2].speed *= .8
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Speed rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'SPEED_UP_2':
                                        i[2].speed *= .64
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Speed sharply rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')



                                        # Other
                                    elif moveData[i[2].moves[int(i[1][6])]][3] == 'SPIN':
                                        spikes[indexNumber] = 0
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     Spikes were removed off the ' + i[2].name + "'s side!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            if len(moveData[i[2].moves[int(i[1][6])]]) > 3:
                                if moveData[i[2].moves[int(i[1][6])]][3] == 'RECOIL':
                                    if not protecting:
                                        damage, typeMultiplier = calculator(i[2],recipient,moveData[i[2].moves[int(i[1][6])]][2],moveData[i[2].moves[int(i[1][6])]][1],weather,lightScreen[oppositeIndex])
                                        i[2].hp -= damage / 4
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' took recoil damage!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                elif moveData[i[2].moves[int(i[1][6])]][3] == 'FELL_STINGER':
                                    if not protecting:
                                        if recipient.hp == 0:
                                            i[2].attack += 2
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack sharply rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        else:



                            # Status Moves
                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            protecting = False
                            if recipient.protect[0] == 1 and random.randint(0,recipient.protect[1]) == 0 and not moveData[i[2].moves[int(i[1][6])]][2] == 'HEAL' and not moveData[i[2].moves[int(i[1][6])]][2] == 'REST':
                                protecting = True
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it was blocked by ' + recipient.name + "'s Protect!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            if moveData[i[2].moves[int(i[1][6])]][2] == 'PAR' or moveData[i[2].moves[int(i[1][6])]][2] == 'PSN' or moveData[i[2].moves[int(i[1][6])]][2] == 'BRN' or moveData[i[2].moves[int(i[1][6])]][2] == 'FRZ':
                                if not protecting:



                                    # Main Status
                                    if moveData[i[2].moves[int(i[1][6])]][2] == 'PAR':
                                        if 'Electric' in recipient.elements:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it had no effect!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        else:
                                            recipient.status[0], recipient.status[1] = moveData[i[2].moves[int(i[1][6])]][2],-1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' is paralyzed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    if moveData[i[2].moves[int(i[1][6])]][2] == 'PSN':
                                        if 'Poison' in recipient.elements:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it had no effect!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        else:
                                            recipient.status[0], recipient.status[1] = moveData[i[2].moves[int(i[1][6])]][2],-1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' is poisoned!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    if moveData[i[2].moves[int(i[1][6])]][2] == 'BRN':
                                        if 'Fire' in recipient.elements:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it had no effect!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        else:
                                            recipient.status[0], recipient.status[1] = moveData[i[2].moves[int(i[1][6])]][2],-1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' is burnt!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    if moveData[i[2].moves[int(i[1][6])]][2] == 'FRZ':
                                        if 'Ice' in recipient.elements:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it had no effect!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        else:
                                            recipient.status[0], recipient.status[1] = moveData[i[2].moves[int(i[1][6])]][2],-1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' is frozen!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'BPS':
                                if not protecting:
                                    if 'Poison' in recipient.elements:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it had no effect!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        recipient.status[0], recipient.status[1] = 'BPS', 0
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The opposing ' + recipient.name + ' is badly poisoned!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SLP':
                                if not protecting:
                                    if 'Grass' in recipient.elements:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it had no effect!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        recipient.status[0], recipient.status[1] = 'SLP',random.randint(2,4)
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The opposing ' + recipient.name + ' is put to sleep!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')



                                # Secondary Status
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'BIND':
                                if not protecting:
                                    if safeguard[oppositeIndex] <= 0:
                                        if moveData[i[2].moves[int(i[1][6])]][1] in recipient.elements:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it had no effect!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        else:
                                            recipient.status[2], recipient.status[3], recipient.status[4] = 'BIND', random.randint(5,6), i[2].moves[int(i[1][6])]
                                    else:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it was blocked by ' + recipient.name + "'s Safeguard!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'TRAP':
                                if not protecting:
                                    if safeguard[oppositeIndex] <= 0:
                                        recipient.status[2], recipient.status[3], recipient.status[4] = 'TRAP', random.randint(3,6), i[2].moves[int(i[1][6])]
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The opposing ' + recipient.name + ' is trapped by ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it was blocked by ' + recipient.name + "'s Safeguard!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'CONFUSE':
                                if not protecting:
                                    if safeguard[oppositeIndex] <= 0:
                                        recipient.status[2], recipient.status[3] = 'CONFUSE', random.randint(2,5)
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The opposing ' + recipient.name + ' becomes confused!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it was blocked by ' + recipient.name + "'s Safeguard!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'LEECH_SEED':
                                if not protecting:
                                    if safeguard[oppositeIndex] <= 0:
                                        if 'Grass' in recipient.elements:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it had no effect!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        else:
                                            recipient.status[2], recipient.status[3] = 'LEECH_SEED', -1
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The opposing ' + recipient.name + ' is implanted by Leech Seed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it was blocked by ' + recipient.name + "'s Safeguard!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'FLINCH':
                                if not protecting:
                                    recipient.status[5] = 1



                                # Buffs/Debuffs
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'ATTACK_DOWN_1':
                                if not protecting:
                                    recipient.attack -= 1
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Attack fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'ATTACK_DOWN_2':
                                if not protecting:
                                    recipient.attack -= 2
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Attack harshly fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'ATTACK_UP_1':
                                i[2].attack += 1
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'ATTACK_UP_2':
                                i[2].attack += 2
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack sharply rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'DEFENSE_DOWN_1':
                                if not protecting:
                                    recipient.defense -= 1
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Defense fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'DEFENSE_UP_1':
                                i[2].defense += 1
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Defense rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'DEFENSE_UP_2':
                                i[2].defense += 2
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Defense sharply rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'DEFENSE_DOWN_2':
                                if not protecting:
                                    recipient.defense -= 2
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Defense harshly fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SPEED_DOWN_1':
                                if protecting:
                                    recipient.speed *= 1.2
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Speed fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SPEED_UP_1':
                                i[2].speed *= .8
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Speed rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SPEED_UP_2':
                                i[2].speed *= .64
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Speed sharply rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SPEED_DOWN_2':
                                if not protecting:
                                    recipient.speed *= 1.44
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Speed sharply fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SHELL_SMASH':
                                i[2].attack += 2
                                i[2].defense -= 1
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Defense fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Defense fell!\n     " + i[2].name + "'s Attack sharply rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SUPERPOWER':
                                i[2].attack -= 1
                                i[2].defense -= 1
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack fell!\n     " + i[2].name + "'s Defense fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'CLOSE_COMBAT':
                                i[2].defense -= 2
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack fell!\n     " + i[2].name + "'s Defense fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'LEAF_STORM':
                                i[2].attack -= 2
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack fell!\n     " + i[2].name + "'s Defense fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'QUIVER_DANCE':
                                i[2].attack += 1
                                i[2].defense += 1
                                i[2].speed *= .8
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack rose!\n     " + i[2].name + "'s Defense rose!",currentPkmn,name1,name2)  + 'Press "Enter" to continue. ')
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + "'s Attack rose!\n     " + i[2].name + "'s Defense rose!\n     " + i[2].name + "'s Speed rose!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'ACCURACY_DOWN':
                                if not protecting:
                                    recipient.accuracy -= .1
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + "'s Accuracy fell!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')



                                # Other
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SPIKES':
                                spikes[oppositeIndex] = 1
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     Spikes were spread around the ' + recipient.name + "'s side!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'TOXIC_SPIKES':
                                spikes[oppositeIndex] = 2
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     Toxic Spikes were spread around the ' + recipient.name + "'s side!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'HEAL':
                                recovery = int(i[2].maxHP / 2)
                                recoveryPrint = recovery
                                if (i[2].hp + recovery) > i[2].maxHP:
                                    recoveryPrint = i[2].maxHP - i[2].hp 
                                i[2].hp += recovery
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + ' heals ' + str(recoveryPrint) + ' HP!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'WAKE_UP_SLAP':
                                if recipient.status[0] == 'SLP':
                                    recipient.status[0], recipient.status[1] = '', -1
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + recipient.name + ' woke up!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'REST':
                                recovery = int(i[2].maxHP)
                                recoveryPrint = i[2].maxHP - i[2].hp 
                                i[2].hp += recovery
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + ' heals ' + str(recoveryPrint) + ' HP!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                i[2].status[0], i[2].status[1] = 'SLP',random.randint(2,4)
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     ' + i[2].name + ' heals ' + str(recoveryPrint) + ' HP!\n\n     ' + i[2].name + ' is put to sleep!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'PROTECT':
                                i[2].protect[0] = 1
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'RAIN':
                                weather = ["Rain",6]
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It begins raining!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SANDSTORM':
                                weather = ["Sandstorm",6]
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     A sandstorm brewed!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SAFEGUARD':
                                safeguard[indexNumber] = 6
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     Safeguard was set up on the ' + i[2].name + "'s side!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'LIGHT_SCREEN':
                                if currentPkmn[0] == i[2]:
                                    lightScreen[0] = 6
                                else:
                                    lightScreen[1] = 6
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     Light Screen was set up on the ' + i[2].name + "'s side!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'ELECTRO_BALL':
                                if currentPkmn[0] == i[2]:
                                    damage, typeMultiplier = calculator(i[2],recipient,electroBall,'Electric',weather,lightScreen[0])
                                else:
                                    damage, typeMultiplier = calculator(i[2],recipient,electroBall,'Electric',weather,lightScreen[1])
                                multiplier = 1
                                if i[2].status[0] == 'BRN':
                                    multiplier = .5
                                if weather[0] == 'Rain' and moveData[i[2].moves[int(i[1][6])]][1] == "Fire":
                                    multiplier *= .5
                                if weather[0] == 'Rain' and moveData[i[2].moves[int(i[1][6])]][1] == "Water":
                                    multiplier *= 2
                                if lightScreen[oppositeIndex] > -1:
                                    multiplier *= (2 / 3)
                                if i[2].attack / 2 < 1:
                                    multiplier *= 2 / (2 + (2 - i[2].attack))
                                else:
                                    multiplier *= i[2].attack / 2
                                if recipient.defense / 2 < 1:
                                    multiplier *= 2 / (2 + (2 - recipient.defense))
                                else:
                                    multiplier *= recipient.defense / 2
                                damage = math.ceil(damage * multiplier)
                                if recipient.protect[0] == 1:
                                    if random.randint(0,recipient.protect[1]) == 0:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it was blocked by ' + recipient.name + "'s Protect!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        recipient.hp -= damage
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        if typeMultiplier == 0:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But the opposing ' + recipient.name + ' is immune!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        elif typeMultiplier < 1:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It's not very effective...",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        elif typeMultiplier > 1:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It's super effective!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                else:
                                    recipient.hp -= damage
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    if typeMultiplier == 0:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But the opposing ' + recipient.name + ' is immune!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif typeMultiplier < 1:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It's not very effective...",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    elif typeMultiplier > 1:
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + "!\n\n     It's super effective!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'HAZE':
                                i[2].attack, i[2].defense, i[2].speed = 2, 2, 1
                                recipient.attack, recipient.defense, recipient.speed = 2, 2, 1
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The stats of all Pokemon on the field were reset!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'TAILWIND':
                                if currentPkmn[0] == i[2]:
                                    tailwind[0] = 6
                                else:
                                    tailwind[1] = 6
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     The tailwind blew from behind ' + i[2].name + "'s team!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'ENDEAVOR':
                                if i[2].hp >= recipient.hp:
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it failed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                else:
                                    recipient.hp = i[2].hp
                                    input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'SUPER_FANG':
                                recipient.hp = recipient.hp / 2
                                input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                            elif moveData[i[2].moves[int(i[1][6])]][2] == 'WHIRLWIND':
                                if not protecting:
                                    fainted = 0
                                    flag3 = False
                                    if currentPkmn[0] == i[2]:
                                        recipientOrder = order[1]
                                        currentOrder = order[0]
                                        number1 = 0
                                        number2 = 1
                                        for pkmn in recipientOrder[3]:
                                            if pkmn.hp == 0:
                                                fainted += 1
                                        if fainted != 5:
                                            if order.index(i) == 0:
                                                newList = []
                                                flagA = False
                                                flagB = False
                                                while not flagA:
                                                    for pkmn in recipientOrder[3]:
                                                        if len(newList) != 5:
                                                            if pkmn == recipientOrder[2]:
                                                                if not flagB:
                                                                    flagB = True
                                                            elif flagB:
                                                                newList.append(pkmn)
                                                        else:
                                                            flagA = True
                                                flagA = False
                                                for pkmn in newList:
                                                    if not flagA and pkmn.hp != 0:
                                                        currentPkmn[number2] = pkmn
                                                        flagA = True
                                            else:
                                                newList = []
                                                flagA = False
                                                flagB = False
                                                while not flagA:
                                                    for pkmn in currentOrder[3]:
                                                        if len(newList) != 5:
                                                            if pkmn == currentOrder[2]:
                                                                if not flagB:
                                                                    flagB = True
                                                            elif flagB:
                                                                newList.append(pkmn)
                                                        else:
                                                            flagA = True
                                                flagA = False
                                                for pkmn in newList:
                                                    if not flagA and pkmn.hp != 0:
                                                        currentPkmn[number2] = pkmn
                                                        flagA = True
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses Whirlwind!\n\n     ' + recipient.name + " was switched out!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                            if order.index(i) == 0:
                                                order[0][2] = currentPkmn[0]
                                                order[1][2] = currentPkmn[1]
                                            else:
                                                order[0][2] = currentPkmn[1]
                                                order[1][2] = currentPkmn[0]
                                            whirlwind = True
                                        else:
                                            input(display('     ' + i[0] + "'s " + i[2].name + ' uses Whirlwind!\n\n     But it failed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                    else:
                                        recipientOrder = order[0]
                                        currentOrder = order[1]
                                        number1 = 1
                                        number2 = 0
                                        for pkmn in currentOrder[3]:
                                            if pkmn.hp == 0:
                                                fainted += 1
                                        if fainted != 5:
                                            if order.index(i) == 0:
                                                newList = []
                                                flagA = False
                                                flagB = False
                                                while not flagA:
                                                    for pkmn in currentOrder[3]:
                                                        if len(newList) != 5:
                                                            if pkmn == currentOrder[2]:
                                                                if not flagB:
                                                                    flagB = True
                                                            elif flagB:
                                                                newList.append(pkmn)
                                                        else:
                                                            flagA = True
                                                flagA = False
                                                for pkmn in newList:
                                                    if not flagA and pkmn.hp != 0:
                                                        currentPkmn[number2] = pkmn
                                                        flagA = True
                                            else:
                                                newList = []
                                                flagA = False
                                                flagB = False
                                                while not flagA:
                                                    for pkmn in recipientOrder[3]:
                                                        if len(newList) != 5:
                                                            if pkmn == recipientOrder[2]:
                                                                if not flagB:
                                                                    flagB = True
                                                            elif flagB:
                                                                newList.append(pkmn)
                                                        else:
                                                            flagA = True
                                                flagA = False
                                                for pkmn in newList:
                                                    if not flagA and pkmn.hp != 0:
                                                        currentPkmn[number2] = pkmn
                                                        flagA = True
                                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses Whirlwind!\n\n     ' + recipient.name + " was switched out!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                        if order.index(i) == 0:
                                            order[0][2] = currentPkmn[1]
                                            order[1][2] = currentPkmn[0]
                                        else:
                                            order[0][2] = currentPkmn[0]
                                            order[1][2] = currentPkmn[1]
                    else:
                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                        input(display('     ' + i[0] + "'s " + i[2].name + ' uses ' + i[2].moves[int(i[1][6])] + '!\n\n     But it missed!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')



        # Status Damage
        for i in order:
            if i[2] == currentPkmn[0]:
                number = 0
            else:
                number = 1
            if order.index(i) == 0:
                recipient = order[1][2]
            else:
                recipient = order[0][2]
            if i[2].hp != 0:
                if i[2].status[0] == 'BRN':
                    i[2].hp -= i[2].maxHP * (1 / 8)
                    input(display('     ' + i[0] + "'s " + i[2].name + ' is hurt by its burn!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                elif i[2].status[0] == 'PSN':
                    i[2].hp -= i[2].maxHP * (1 / 8)
                    input(display('     ' + i[0] + "'s " + i[2].name + ' is hurt by poison!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                elif i[2].status[0] == 'BPS':
                    i[2].hp -= i[2].maxHP * ((1 + (-1 * i[2].status[1])) / 16)
                    input(display('     ' + i[0] + "'s " + i[2].name + ' is hurt by poison!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                if i[2].status[2] == 'BIND':
                    i[2].hp -= i[2].maxHP * (1 / 8)
                    input(display('     ' + i[0] + "'s " + i[2].name + ' is hurt by ' + i[2].status[4] + '!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                elif i[2].status[2] == 'LEECH_SEED':
                    i[2].hp -= (i[2].maxHP * (1 / 8))
                    if recipient.hp != 0:
                        if recipient.hp + (i[2].maxHP * (1 / 8)) <= recipient.maxHP:
                            recipient.hp += (i[2].maxHP * (1 / 8))
                    input(display('     ' + i[2].name + "'s health is sapped by Leech Seed!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                i[2].status[1] -= 1
                i[2].status[3] -= 1



            # Update Board Data
            safeguard[number] -= 1
            lightScreen[number] -= 1
            tailwind[number] -= 1
            if i[2].protect[0] == 1:
                i[2].protect[1] += 1
            else:
                i[2].protect[1] = 0
            if i[2].status[2] == 'BIND' and i[2].status[3] == 0 or i[2].status[2] == 'CONFUSE' and i[2].status[3] == 0 or i[2].status[2] == 'TRAP' and i[2].status[3] == 0:
                i[2].status[2] = ''
            i[2].status[5] = 0
            if safeguard[number] == 1:
                safeguard = 0
                input(display('     The ' + i[2].name + "'s Safeguard was lowered!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
            if tailwind[number] == 0:
                input(display('     The ' + i[2].name + "'s Tailwind subsided!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
            if lightScreen[number] == 0:
                input(display('     The ' + i[2].name + "'s Light Screen ended!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
            if weather[0] == 'Sandstorm' and 'Ground' not in i[2].elements and 'Rock' not in i[2].elements and 'Steel' not in i[2].elements and i[2].hp > 0:
                i[2].hp -= i[2].maxHP * (1 / 16)
                input(display('     ' + i[0] + "'s " + i[2].name + ' is buffeted by the sandstorm!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
        weather[1] -= 1
        if weather[1] == 0:
            if weather[0] == "Rain":
                input(display('     It stopped raining.',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
            elif weather[0] == 'Sandstorm':
                input(display('     The sandstorm subsided.',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
            weather[0] = ""



        # Fainted Pokemon
        for i in order:
            if i[2].hp == 0:
                fainted = 0
                names = []
                for pkmn in i[3]:
                    if pkmn.hp == 0:
                        fainted += 1
                    names.append(pkmn.name.lower())
                input(display('     ' + i[0] + "'s " + i[2].name + " fainted!",currentPkmn,name1,name2) + 'Press "Enter" to continue. ')



                # Display Team
                if fainted != 6:
                    msg = ''
                    accumulator = 0
                    for pkmn in i[3]:
                        accumulator += 1
                        pkmnStatus = ' ' + pkmn.status[0]
                        if pkmn.hp > 0:
                            if len(pkmn.elements) == 2:
                                msg += '     ' + str(accumulator) + '  -  "' + pkmn.name + '"  (' + str(pkmn.hp) + '/' + str(pkmn.maxHP) + 'HP,  ' + pkmn.elements[0] + ' / ' + pkmn.elements[1] + ')' + pkmnStatus + '\n'
                            else:
                                msg += '     ' + str(accumulator) + '  -  "' + pkmn.name + '"  (' + str(pkmn.hp) + '/' + str(pkmn.maxHP) + 'HP,  ' + pkmn.elements + ')' + pkmnStatus + '\n'
                        else:
                            if len(pkmn.elements) == 2:
                                msg += '     X  -  "' + pkmn.name + '"  (0/' + str(pkmn.maxHP) + 'HP,  ' + pkmn.elements[0] + ' / ' + pkmn.elements[1] + ')' + pkmnStatus + '\n'
                            else:
                                msg += '     X  -  "' + pkmn.name + '"  (0/' + str(pkmn.maxHP) + 'HP,  ' + pkmn.elements + ')' + pkmnStatus + '\n'
                    msg += '\n     Return  "Info"  &  Number/Name  for  more  details\n\n     ' + i[0] + ', input a command:'
                    flag1 = False
                    while not flag1:
                        choice = input(display(msg,currentPkmn,name1,name2)).lower()



                        # Info [Pokemon]
                        if 'info' in choice:
                            chosenPkmn = None
                            for pkmn in pokemonList:
                                if pkmn.name.lower() in choice:
                                    chosenPkmn = pkmn()
                            if chosenPkmn == None:
                                for pkmn in range(len(i[3])):
                                    if str(pkmn + 1) in choice:
                                        chosenPkmn = i[3][pkmn]
                            if chosenPkmn != None:
                                print('\n' * DISPLAY)
                                print(chosenPkmn)
                                input('     >> Press "Enter" to continue')
                            else:
                                input(display("     Please provide the number or name of the Pokemon you\n     would like to learn more about.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()



                        # Switch Pokemon
                        elif '1' == choice or '2' == choice or '3' == choice or '4' == choice or '5' == choice or '6' == choice:
                            if i[3][int(choice) - 1].hp < 1:
                                input(display("     You cannot switch to a fainted Pokemon.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()
                            else:
                                finalize = input(display('     Switch to ' + names[int(choice) - 1].capitalize() + '?',currentPkmn,name1,name2)).lower()
                                if finalize == 'yes':
                                    flag2 = False
                                    for pkmn in i[3]:
                                        if not flag2:
                                            if pkmn.name.lower() == names[int(choice) - 1] and pkmn.hp > 0:
                                                i[2] = pkmn
                                                flag2 = True
                                    flag1 = True
                        elif choice in names:
                            flag2 = False
                            for pkmn in i[3]:
                                if not flag2:
                                    if pkmn.name.lower() in choice and pkmn.hp > 0:
                                        flag2 = True
                            if not flag2:
                                input(display("     You cannot switch to a fainted Pokemon.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()
                            else:
                                finalize = input(display('     Switch to ' + choice.capitalize() + '?',currentPkmn,name1,name2)).lower()
                                if finalize == 'yes':
                                    flag2 = False
                                    for pkmn in i[3]:
                                        if not flag2:
                                            if pkmn.name.lower() in choice and pkmn.hp > 0:
                                                i[2] = pkmn
                                                if spikes[1] == 1:
                                                    i[2].hp -= 10
                                                    input(display('     ' + i[0] + ' switches to ' + i[2].name + '!\n\n     ' + i[2].name + ' takes damage from spikes!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                                elif spikes[1] == 2 and "Poison" not in i[2].elements:
                                                    i[2].status[0], i[2].status[1] = "PSN", -1
                                                    input(display('     ' + i[0] + ' switches to ' + i[2].name + '!\n\n     ' + i[2].name + ' is poisoned by Toxic Spikes!',currentPkmn,name1,name2) + 'Press "Enter" to continue. ')
                                                flag2 = True
                                    flag1 = True
                        else:
                            input(display("     Your input could not be understood. Please try again.",currentPkmn,name1,name2) + 'Press "Enter" to continue. ').lower()
                else:



                    # Battle End
                    if i[0] == name1:
                        input(('\n' * DISPLAY) + (' ' * 35) + name2.upper() + " WON!" + ('\n' * 12))
                        return name2
                    else:
                        input(('\n' * DISPLAY) + (' ' * 35) + name1.upper() + " WON!" + ('\n' * 12))
                        return name1
        if order[0][0] == name1:
            currentPkmn = [order[0][2],order[1][2]]
        else:
            currentPkmn = [order[1][2],order[0][2]]



def debug(text):
    debugfile = open(os.path.join(__location__, "debug.txt"),'a')
    debugfile.write(text)
    debugfile.close()



DISPLAY = 50 # Adjusts Display to fit IDLE (5) or Terminal (50)

# Type Chart and List
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
elementChart = open(os.path.join(__location__, "typechart.txt"),'r')
elementData = elementChart.read()
elementList = ('Normal','Fire','Water','Electric','Grass','Ice','Fighting','Poison','Ground','Flying','Psychic','Bug','Rock','Ghost','Dragon','Dark','Steel','Fairy')
elementChart.close()
debugfile = open(os.path.join(__location__, "debug.txt"),'w')
debugfile.write('')
debugfile.close()

# Name: Accuracy, Type, Damage/Effect, Effect, Chance
moveData = {"Tackle":(100,'Normal',10),\
            "Scratch":(100,'Normal',10),\
            "Pound":(100,'Normal',15),\
            "Double Slap":(100,'Normal',15),\
            "Rapid Spin":(100,'Normal',15,"SPIN",100),\
            "Round":(100,'Normal',20),\
            "Swift":(100,'Normal',20,"SWIFT",100),\
            "Horn Attack":(100,'Normal',20),\
            "Body Slam":(100,'Normal',25,'PAR',50),\
            "Headbutt":(100,'Normal',25),\
            "Slash":(100,'Normal',30),\
            "Slam":(100,'Normal',30),\
            "Hyper Fang":(100,'Normal',30),\
            "Hyper Voice":(100,'Normal',30),\
            "Mega Kick":(75,'Normal',40),\
            "Take Down":(100,'Normal',30,"RECOIL",100),\
            "Double Edge":(100, 'Normal',40,"RECOIL",100),\
            "Skull Bash":(100,'Normal',40,"RECOIL",100),\
            "Thrash":(100,'Normal',40,"RECOIL",100),\
            "Giga Impact":(100,'Normal',60,"CHARGE",100),\
            "Extreme Speed":(100,'Normal',25,"PRIORITY",100),\
            "Fake Out":(100,'Normal',15,"FLINCH",100),\
            "Hyper Beam":(100,'Normal',60,"CHARGE",100),\

            "Ember":(100,'Fire',10,"BRN",50),\
            "Fire Fang":(100,'Fire',20,"BRN",50),\
            "Fire Punch":(100,'Fire',25,"BRN",50),\
            "Flame Burst":(100,'Fire',20,"BRN",25),\
            "Flamethrower":(100,'Fire',30,"BRN",50),\
            "Fire Blast":(100,'Fire',30),\
            "Flare Blitz":(100,'Fire',40,"RECOIL",100),\
            "Inferno":(50,'Fire',40),\
            "Overheat":(100,'Fire',40,"LEAF_STORM",100),\
            
            "Water Gun":(100,'Water',10),\
            "Water Pulse":(100,'Water',20,"CONFUSE",25),\
            "Aqua Tail":(100,'Water',30),\
            "Hydro Pump":(75,'Water',40),\
            "Dive":(100,'Water',25),\
            
            "Nuzzle":(100,'Electric',10,"PAR",100),\
            "Thunder Shock":(100,'Electric',10,"PAR",50),\
            "Electroweb":(100,'Electric',15,"SPEED_DOWN_1",100),\
            "Thunder Fang":(100,'Electric',20,"PAR",50),\
            "Spark":(100,'Electric',20,"PAR",25),\
            "Discharge":(100,'Electric',25,"PAR",50),\
            "Thunder Punch":(100,'Electric',25,"PAR",50),\
            "Thunderbolt":(100,'Electric',30,"PAR",50),\
            "Thunder":(75,'Electric',40,"PAR",50),\
            
            "Vine Whip":(100,'Grass',10),\
            "Razor Leaf":(100,'Grass',20),\
            "Seed Bomb":(100,'Grass',25),\
            "Petal Blizzard":(100,'Grass',30),\
            "Solar Beam":(100,'Grass',60,"CHARGE",100),\
            "Leaf Blade":(100,'Grass',30),\
            "Leaf Storm":(100,'Grass',40,"LEAF_STORM",100),\
            "Wood Hammer":(100,'Grass',40,"RECOIL",100),\

            "Ice Fang":(100,'Ice',20,"FRZ",50),\
            "Blizzard":(75,'Ice',60,"FRZ",50),\

            "Wake-Up Slap":(100,'Fighting',15,"WAKE_UP_SLAP",100),\
            "Double Kick":(100,'Fighting',20),\
            "Superpower":(100,'Fighting',40,"SUPERPOWER",100),\
            "High Jump Kick":(75,'Fighting',60,"RECOIL",100),\
            "Hammer Arm":(75,'Fighting',35),\
            "Cross Chop":(75,'Fighting',30),\
            "Close Combat":(100,'Fighting',40,"CLOSE_COMBAT",100),\
            
            "Poison Sting":(100,'Poison',10,"PSN",50),\
            "Acid Spray":(100,'Poison',20,"DEFENSE_DOWN_2",100),\
            "Poison Fang":(100,'Poison',20,"FLINCH",50),\
            "Venoshock":(100,'Poison',25,"VENOSHOCK",100),\
            "Acid":(100,'Poison',25),\
            "Poison Jab":(100,'Poison',30,"PSN",50),\
            "Gunk Shot":(50,'Poison',40),\
            "Cross Poison":(100,'Poison',25,"PSN",50),\
            
            "Magnitude":(100,'Ground',15),\
            "Mud Bomb":(100,'Ground',20),\
            "Drill Run":(100,'Ground',25),\
            "Earth Power":(100,'Ground',30),\
            "Earthquake":(100,'Ground',35),\
            "Dig":(100,'Ground',25),\
            "Bone Rush":(100,'Ground',25),\
            
            "Peck":(100,'Flying',10),\
            "Gust":(100,'Flying',10),\
            "Air Slash":(100,'Flying',25,"FLINCH",50),\
            "Drill Peck":(100,'Flying',25),\
            "Wing Attack":(100,'Flying',30),\
            "Hurricane":(50,'Flying',40),\
            "Bounce":(75,'Flying',30),\
            "Brave Bird":(100,'Flying',40,'RECOIL',100),\
            
            "Confusion":(100,'Psychic',15,"CONFUSE",50),\
            "Psybeam":(100,'Psychic',20),\
            "Extrasensory":(100,'Psychic',25,"FLINCH",50),\
            "Zen Headbutt":(100,'Psychic',25,"FLINCH",50),\
            "Psychic":(100,'Psychic',30,'CONFUSE',50),\

            "Fell Stinger":(100,'Bug',15,"FELL_STINGER",100),\
            "Fury Cutter":(100,'Bug',15),\
            "Bug Bite":(100,'Bug',20),\
            "Silver Wind":(100,'Bug',30),\
            "Bug Buzz":(100,'Bug',30,"DEFENSE_DOWN_1",25),\
            "Megahorn":(75,'Bug',40),\
            "X-Scissor":(100,'Bug',25),\

            "Rollout":(100,'Rock',10),\
            "Power Gem":(100,'Rock',25),\
            "Ancient Power":(100,'Rock',20),\
            "Stone Edge":(75,'Rock',35),\
            "Rock Slide":(100,'Rock',25,"FLINCH",50),\
            "Rock Wrecker":(100,'Rock',60,"CHARGE",100),\
            "Head Smash":(75,'Rock',60,"RECOIL",100),\

            "Twister":(100,'Dragon',10,"FLINCH",50),\
            "Dragon Breath":(100,'Dragon',20,"PAR",50),\
            "Dragon Claw":(100,'Dragon',30),\
            
            "Pursuit":(100,'Dark',15,"PURSUIT",100),\
            "Bite":(100,'Dark',20,"FLINCH",50),\
            "Assurance":(100,'Dark',25),\
            "Crunch":(100,'Dark',25,"DEFENSE_DOWN_1",100),\
            "Darkest Lariat":(100,'Dark',30),\
            "Night Slash":(100,'Dark',25),\
            "Dark Pulse":(100,'Dark',25,"FLINCH",50),\

            "Spirit Shackle":(100,'Ghost',25,"TRAP",100),\
            "Shadow Ball":(100,'Ghost',30),\
            "Phantom Force":(100,'Ghost',30),\
            "Shadow Sneak":(100,'Ghost',25),\

            "Meteor Mash":(100,'Steel',30),\
            "Flash Cannon":(100,'Steel',25,"DEFENSE_DOWN_1",100),\
            "Iron Tail":(100,'Steel',35),\
            "Iron Head":(100,'Steel',25,"FLINCH",50),\
            "Double Iron Bash":(100,'Steel',35),\
            "Bullet Punch":(100,'Steel',20,"PRIORITY",100),\
            "Metal Claw":(100,'Steel',25),\

            "Disarming Voice":(100,'Fairy',10),\
            "Moonblast":(100,'Fairy',30),\
            "Play Rough":(100,'Fairy',30),\
            
            "Quick Attack":(100,'Normal',15,"PRIORITY",100),\
            "Aerial Ace":(100,'Flying',20,"PRIORITY",100),\
            "Sucker Punch":(100,'Dark',30,"SUCKER_PUNCH",100),\
            
            "Glare":(100,'Normal',"PAR"),\
            "Thunder Wave":(100,'Electric',"PAR"),\
            "Stun Spore":(100,'Grass',"PAR"),\
            "Sleep Powder":(50,'Grass',"SLP"),\
            "Sing":(50,'Normal',"SLP"),\
            "Hypnosis":(50,'Psychic',"SLP"),\
            "Yawn":(50,'Normal',"SLP"),\
            "Poison Powder":(100,'Poison',"PSN"),\
            "Toxic":(100,'Poison',"BPS"),\
            "Will-O-Wisp":(100,'Fire',"BRN"),\
            
            "Supersonic":(100,'Normal',"CONFUSE"),\
            "Sweet Kiss":(100,'Fairy',"CONFUSE"),\
            "Confuse Ray":(100,'Ghost',"CONFUSE"),\
            "Leech Seed":(100,'Grass',"LEECH_SEED"),\
            "Wrap":(100,'Normal',10,"TRAP",100),\
            "Fire Spin":(100,'Fire',10,"TRAP",100),\
            
            "Nasty Plot":(100,'Dark',"ATTACK_UP_2"),\
            "Swords Dance":(100,'Normal',"ATTACK_UP_2"),\
            "Calm Mind":(100,'Psychic',"ATTACK_UP_2"),\
            "Growl":(100,'Normal',"ATTACK_DOWN_1"),\
            "Play Nice":(100,'Normal',"ATTACK_DOWN_1"),\
            "Charm":(100,'Fairy',"ATTACK_DOWN_2"),\
            "Feather Dance":(100,'Flying',"ATTACK_DOWN_2"),\
            "Iron Defense":(100,'Steel',"DEFENSE_UP_2"),\
            "Cosmic Power":(100,'Psychic',"DEFENSE_UP_2"),\
            "Amnesia":(100,'Psychic',"DEFENSE_UP_2"),\
            "Defense Curl":(100,'Normal',"DEFENSE_UP_1"),\
            "Harden":(100,'Normal',"DEFENSE_UP_1"),\
            "Withdraw":(100,'Water',"DEFENSE_UP_1"),\
            "Leer":(100,'Normal',"DEFENSE_DOWN_1"),\
            "Tail Whip":(100,'Normal',"DEFENSE_DOWN_1"),\
            "Screech":(100,'Normal',"DEFENSE_DOWN_2"),\
            "Agility":(100,'Psychic',"SPEED_UP_2"),\
            "String Shot":(100,'Bug',"SPEED_DOWN_1"),\
            "Scary Face":(100,'Normal',"SPEED_DOWN_2"),\
            "Smokescreen":(100,'Normal',"ACCURACY_DOWN"),\
            "Sand Attack":(100,'Ground',"ACCURACY_DOWN"),\
            "Shell Smash":(100,'Normal',"SHELL_SMASH"),\
            "Quiver Dance":(100,'Bug',"QUIVER_DANCE"),\
            "Dragon Dance":(100,'Dragon',"QUIVER_DANCE"),\
            "Haze":(100,'Ice',"HAZE"),\
            
            "Protect":(100,'Normal',"PROTECT"),\
            "Rain Dance":(100,'Water',"RAIN"),\
            "Sandstorm":(100,'Rock',"SANDSTORM"),\
            "Super Fang":(100,'Normal',"SUPER_FANG"),\
            "Electro Ball":(100,'Electric',"ELECTRO_BALL"),\
            "Endeavor":(100,'Normal',"ENDEAVOR"),\
            "Synthesis":(100,'Grass','HEAL'),\
            "Roost":(100,'Flying',"HEAL"),\
            "Moonlight":(100,'Fairy',"HEAL"),\
            "Recover":(100,'Normal',"HEAL"),\
            "Rest":(100,'Psychic',"REST"),\
            "Light Screen":(100,'Psychic',"LIGHT_SCREEN"),\
            "Tailwind":(100,'Flying',"TAILWIND"),\
            "Whirlwind":(100,'Normal',"WHIRLWIND"),\
            "Safeguard":(100,'Normal',"SAFEGUARD"),\
            "Spikes":(100,'Ground',"SPIKES"),\
            "Toxic Spikes":(100,'Poison',"TOXIC_SPIKES")}





# Species Information
class Stoutland(Template):
    name = "Stoutland"
    elements = ('Normal')
    moves = ('Take Down','Fire Fang','Ice Fang','Thunder Fang')
    maxHP = 85
    
class Snorlax(Template):
    name = "Snorlax"
    elements = ('Normal')
    moves = ('Giga Impact','Body Slam','Hammer Arm',"Yawn")
    maxHP = 160

class Lopunny(Template):
    name = "Lopunny"
    elements = ('Normal')
    moves = ('Headbutt','High Jump Kick','Bounce','Charm')
    maxHP = 65

class Arcanine(Template):
    name = "Arcanine"
    elements = ('Fire')
    moves = ("Flare Blitz","Flamethrower","Crunch","Extreme Speed")
    maxHP = 90

class Charizard(Template):
    name = "Charizard"
    elements = ('Fire','Flying')
    moves = ("Flamethrower","Fire Spin","Air Slash","Dragon Breath")
    maxHP = 78

class Incineroar(Template):
    name = "Incineroar"
    elements = ('Fire','Dark')
    moves = ("Flare Blitz","Flamethrower","Darkest Lariat","Cross Chop")
    maxHP = 95

class Blastoise(Template):
    name = "Blastoise"
    elements = ('Water')
    moves = ("Aqua Tail","Skull Bash","Rain Dance","Rapid Spin")
    maxHP = 79

class Gyarados(Template):
    name = "Gyarados"
    elements = ('Water','Flying')
    moves = ("Aqua Tail","Hurricane","Ice Fang","Rain Dance")
    maxHP = 95

class Greninja(Template):
    name = "Greninja"
    elements = ('Water','Dark')
    moves = ("Hydro Pump","Night Slash","Extrasensory","Spikes")
    maxHP = 72

class Ampharos(Template):
    name = "Ampharos"
    elements = ('Electric')
    moves = ("Thunderbolt","Fire Punch","Power Gem","Light Screen")
    maxHP = 90

class Zapdos(Template):
    name = "Zapdos"
    elements = ('Electric','Flying')
    moves = ("Thunder","Drill Peck","Light Screen","Rain Dance")
    maxHP = 90

class Toxtricity(Template):
    name = "Toxtricity"
    elements = ('Electric','Poison')
    moves = ("Discharge","Poison Jab","Nuzzle","Toxic")
    maxHP = 75

class Sceptile(Template):
    name = "Sceptile"
    elements = ('Grass')
    moves = ("Leaf Blade","X-Scissor","Night Slash","Screech")
    maxHP = 70

class Venusaur(Template):
    name = "Venusaur"
    elements = ('Grass','Poison')
    moves = ("Double Edge","Petal Blizzard","Leech Seed","Synthesis")
    maxHP = 80

class Decidueye(Template):
    name = "Decidueye"
    elements = ('Grass','Ghost')
    moves = ("Leaf Blade","Spirit Shackle","Nasty Plot","Feather Dance")
    maxHP = 78

class Avalugg(Template):
    name = "Avalugg"
    elements = ("Ice")
    moves = ("Blizzard","Skull Bash","Iron Defense","Recover")
    maxHP = 95

class Mamoswine(Template):
    name = "Mamoswine"
    elements = ("Ice","Ground")
    moves = ("Blizzard","Ice Fang","Earthquake","Amnesia")
    maxHP = 110

class Froslass(Template):
    name = "Froslass"
    elements = ("Ice","Ghost")
    moves = ("Blizzard","Shadow Ball","Will-O-Wisp","Confuse Ray")
    maxHP = 70

class Conkeldurr(Template):
    name = "Conkeldurr"
    elements = ('Fighting')
    moves = ("Superpower","Hammer Arm","Stone Edge","Scary Face")
    maxHP = 105

class Lucario(Template):
    name = "Lucario"
    elements = ('Fighting','Steel')
    moves = ("Close Combat","Meteor Mash","Bone Rush","Swords Dance")
    maxHP = 70

class Medicham(Template):
    name = "Medicham"
    elements = ('Fighting','Psychic')
    moves = ("High Jump Kick","Zen Headbutt","Thunder Punch","Fire Punch")
    maxHP = 60

class Seviper(Template):
    name = "Seviper"
    elements = ('Poison')
    moves = ("Poison Jab","Crunch","Glare","Haze")
    maxHP = 73

class Crobat(Template):
    name = "Crobat"
    elements = ('Poison','Flying')
    moves = ("Cross Poison","Wing Attack","Confuse Ray","Haze")
    maxHP = 85

class Drapion(Template):
    name = "Drapion"
    elements = ('Poison','Dark')
    moves = ("Poison Jab","Crunch","Ice Fang","Toxic Spikes")
    maxHP = 70

class Mudsdale(Template):
    name = "Mudsdale"
    elements = ('Ground')
    moves = ("Earthquake","Superpower","Mega Kick","Iron Defense")
    maxHP = 100

class Flygon(Template):
    name = "Flygon"
    elements = ('Ground','Dragon')
    moves = ("Earthquake","Dragon Claw","Bug Buzz","Superpower")
    maxHP = 80

class Excadrill(Template):
    name = "Excadrill"
    elements = ('Ground','Steel')
    moves = ("Earthquake","Rock Slide","Metal Claw","Sandstorm")
    maxHP = 110

class Staraptor(Template):
    name = "Staraptor"
    elements = ('Normal','Flying')
    moves = ("Brave Bird","Aerial Ace","Close Combat","Whirlwind")
    maxHP = 85

class Tropius(Template):
    name = "Tropius"
    elements = ('Grass','Flying')
    moves = ('Leaf Storm','Air Slash','Synthesis','Whirlwind')
    maxHP = 99

class Cramorant(Template):
    name = "Cramorant"
    elements = ('Flying','Water')
    moves = ('Drill Peck','Hydro Pump','Dive','Amnesia')
    maxHP = 70

class Meowstic(Template):
    name = "Meowstic"
    elements = ('Psychic')
    moves = ('Psychic','Fake Out','Light Screen','Charm')
    maxHP = 74

class Gardevoir(Template):
    name = "Gardevoir"
    elements = ('Psychic','Fairy')
    moves = ('Psychic','Moonblast','Hypnosis','Calm Mind')
    maxHP = 68

class Exeggutor(Template):
    name = "Exeggutor"
    elements = ('Grass','Psychic')
    moves = ('Leaf Storm','Extrasensory','Light Screen','Leech Seed')
    maxHP = 95

class Accelgor(Template):
    name = "Accelgor"
    elements = ('Bug')
    moves = ('Bug Buzz','Toxic','Yawn','Quick Attack')
    maxHP = 80

class Scizor(Template):
    name = "Scizor"
    elements = ('Bug','Steel')
    moves = ('X-Scissor','Iron Head','Wing Attack','Swords Dance')
    maxHP = 70

class Crustle(Template):
    name = "Crustle"
    elements = ('Bug','Rock')
    moves = ('X-Scissor','Rock Wrecker','Rock Slide','Spikes')
    maxHP = 70

class Gigalith(Template):
    name = "Gigalith"
    elements = ('Rock')
    moves = ('Stone Edge','Iron Defense','Spikes','Sandstorm')
    maxHP = 85

class Tyranitar(Template):
    name = "Tyranitar"
    elements = ('Rock','Dark')
    moves = ('Stone Edge','Crunch','Earthquake','Sandstorm')
    maxHP = 100

class Aerodactyl(Template):
    name = "Aerodactyl"
    elements = ('Rock','Flying')
    moves = ('Rock Slide','Wing Attack','Giga Impact','Thunder Fang')
    maxHP = 80

class Cofagrigus(Template):
    name = "Cofagrigus"
    elements = ('Ghost')
    moves = ('Shadow Ball','Dark Pulse','Will-O-Wisp','Haze')
    maxHP = 58

class Trevenant(Template):
    name = "Trevenant"
    elements = ('Ghost','Grass')
    moves = ('Phantom Force','Wood Hammer','Leech Seed','Will-O-Wisp')
    maxHP = 85

class Chandelure(Template):
    name = "Chandelure"
    elements = ('Ghost','Fire')
    moves = ('Shadow Ball','Overheat','Fire Spin','Will-O-Wisp')
    maxHP = 60

class Haxorus(Template):
    name = "Haxorus"
    elements = ('Dragon')
    moves = ('Dragon Claw','Giga Impact','Crunch','Dragon Dance')
    maxHP = 76

class Salamence(Template):
    name = "Salamence"
    elements = ('Dragon','Flying')
    moves = ('Dragon Claw','Flamethrower','Zen Headbutt','Thunder Fang')
    maxHP = 95

class Garchomp(Template):
    name = "Garchomp"
    elements = ('Dragon','Ground')
    moves = ('Dragon Claw','Dig','Fire Fang','Sandstorm')
    maxHP = 108

class Darkrai(Template):
    name = "Darkrai"
    elements = ('Dark')
    moves = ('Dark Pulse','Hypnosis','Nasty Plot','Haze')
    maxHP = 70

class Grimmsnarl(Template):
    name = "Grimmsnarl"
    elements = ('Dark','Fairy')
    moves = ('Dark Pulse','Play Rough','Hammer Arm','Nasty Plot')
    maxHP = 95

class Hydreigon(Template):
    name = "Hydreigon"
    elements = ('Dark','Dragon')
    moves = ('Dragon Breath','Crunch','Hyper Beam','Nasty Plot')
    maxHP = 92

class Melmetal(Template):
    name = "Melmetal"
    elements = ('Steel')
    moves = ('Double Iron Bash','Superpower','Hyper Beam','Discharge')
    maxHP = 135

class Metagross(Template):
    name = "Metagross"
    elements = ('Steel','Psychic')
    moves = ('Meteor Mash','Psychic','Hammer Arm','Bullet Punch')
    maxHP = 80

class Aegislash(Template):
    name = "Aegislash"
    elements = ('Steel','Ghost')
    moves = ('Iron Head','Shadow Sneak','Head Smash','Swords Dance')
    maxHP = 60

class Clefable(Template):
    name = "Clefable"
    elements = ('Fairy')
    moves = ('Moonblast','Meteor Mash','Charm','Moonlight')
    maxHP = 95

class Wigglytuff(Template):
    name = "Wigglytuff"
    elements = ('Normal','Fairy')
    moves = ('Double Edge','Play Rough','Sing','Defense Curl')
    maxHP = 140

class Azumarill(Template):
    name = "Azumarill"
    elements = ('Water','Fairy')
    moves = ('Aqua Tail','Play Rough','Charm','Rain Dance')
    maxHP = 100

    




# List of Species
pokemonList = [Stoutland, \
               Snorlax, \
               Lopunny, \
               Arcanine, \
               Charizard, \
               Incineroar, \
               Blastoise, \
               Gyarados, \
               Greninja, \
               Ampharos, \
               Zapdos, \
               Toxtricity, \
               Sceptile, \
               Venusaur, \
               Decidueye, \
               Avalugg, \
               Mamoswine, \
               Froslass, \
               Conkeldurr, \
               Lucario, \
               Medicham, \
               Seviper, \
               Crobat, \
               Drapion, \
               Mudsdale, \
               Flygon, \
               Excadrill, \
               Staraptor, \
               Tropius, \
               Cramorant, \
               Meowstic, \
               Gardevoir, \
               Exeggutor, \
               Accelgor, \
               Scizor, \
               Crustle, \
               Gigalith, \
               Tyranitar, \
               Aerodactyl, \
               Cofagrigus, \
               Trevenant, \
               Chandelure, \
               Haxorus, \
               Salamence, \
               Garchomp, \
               Darkrai, \
               Grimmsnarl, \
               Hydreigon, \
               Melmetal, \
               Metagross, \
               Aegislash, \
               Clefable, \
               Wigglytuff, \
               Azumarill]





main() # Run Program
