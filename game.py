from bag_class import Bag
from equipment_class import Equipment
from hero_class import Hero
from item_class import Item
from mobs_class import Mobs
from quest_class import Quest
from race_class import Race
from stat_class import Stat


def game():
    ### RACES
    statElfe = Stat({'strength': 5, 'magic': 10, 'agility': 10, 'speed': 5, 'charisma': 5, 'chance': 5})
    elfe = Race('Elfe', statElfe)
    statHuman = Stat({'strength': 10, 'magic': 10, 'agility': 5, 'speed': 5, 'charisma': 5, 'chance': 5})
    human = Race('Human', statHuman)
    statDwarf = Stat({'strength': 10, 'magic': 0, 'agility': 10, 'speed': 5, 'charisma': 5, 'chance': 10})
    dwarf = Race('Dwarf', statDwarf)
    statOrc = Stat({'strength': 15, 'magic': 0, 'agility': 5, 'speed': 10, 'charisma': 5, 'chance': 5})
    orc = Race('Orc', statOrc)

    ### CLASSES
    statWizard = Stat({'strength': 0, 'magic': 10, 'agility': 0, 'speed': 0, 'charisma': 10, 'chance': 10})
    wizard = Race('Wizard', statWizard)
    statWarrior = Stat({'strength': 10, 'magic': 0, 'agility': 5, 'speed': 5, 'charisma': 5, 'chance': 5})
    warrior = Race('Warrior', statWarrior)

    ### ITEMS
    statSword = Stat({'strength': 5, 'magic': 0, 'agility': 5, 'speed': 5, 'charisma': 0, 'chance': 5})
    sword = Equipment({'classList': 'warrior', 'place': 'hand', 'name': 'dragon sword', 'type': 'sword', 'space': 2},
                      statSword)
    statBaton = Stat({'strength': 0, 'magic': 10, 'agility': 0, 'speed': 5, 'charisma': 0, 'chance': 5})
    baton = Equipment({'classList': 'wizard', 'place': 'hand', 'name': 'wizard baton', 'type': 'baton', 'space': 2},
                      statBaton)
    statPotion = Stat({'strength': 0, 'magic': 0, 'agility': 0, 'speed': 0, 'charisma': 0, 'chance': 0})
    Potion = Item({'name': 'life potion', 'type': 'potion', 'space': 2}, statPotion)

    ### BAG
    myBag = Bag({"sizeMax": 20, "items": [Potion, Potion]})

    ### MOBS
    mechant1 = Mobs(
        {'name': 'orc 1', 'race': orc, 'classe': warrior, 'bag': myBag, 'equipment': [sword], 'element': 'Fire',
         'type': 'soldier'})
    mechant2 = Mobs(
        {'name': 'orc 2', 'race': orc, 'classe': warrior, 'bag': myBag, 'equipment': [sword], 'element': 'Fire',
         'type': 'soldier'})

    ### HEROES
    hero1 = Hero({'name': 'Jean', 'race': elfe, 'classe': wizard, 'bag': myBag, 'equipment': [baton], 'element': 'Fire',
                  'profession': 'chomeur'})
    hero2 = Hero(
        {'name': 'Pierre', 'race': human, 'classe': warrior, 'bag': myBag, 'equipment': [sword], 'element': 'Fire',
         'profession': 'chomeur'})

    hero1.save()
    hero1.saveXML()

    ### QUEST
    firstQuest = Quest({'lAvatar': [mechant1, mechant2], 'lvl': 2, 'gift': sword})
    # firstQuest = Quest({'lAvatar':[hero2], 'lvl':2, 'gift':sword})
    print(firstQuest.run(hero1))

if __name__ == "__main__":
    game()