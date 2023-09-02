
from sqlalchemy import insert
from db.models import Creator, Spell, Item, Rule


def handleSelection(arr):
    sel = [str(i) for i in arr] + ['X', 'x']
    inp = 999

    while (inp not in sel):
        inp = input("\nMake Selection: ")

    return inp

def menuAndSelect(menu, sesh):

    options = menu[1]
    title = menu[0]

    print('\n' + title + '\n')

    for key in options.keys():
        print(f"\t{key}) {options[key][0]}")
    print("\tX) Exit")

    resp = handleSelection(options.keys())

    if resp in ['X','x']:
        return 
    else:
        options[resp][1](sesh)

def addCreator(session):
    print("\n")
    inp = input("Creator name: ")
    session.add(Creator(name = inp))
    session.commit()

def menuAndSelectView(sesh):
    menuAndSelect(viewMenu, sesh)

def menuAndSelectCreate(sesh):
    menuAndSelect(createMenu, sesh)

def menuAndSelectMain(sesh):
    menuAndSelect(mainMenu, sesh)


def assignCreator(sesh):
    creators = sesh.query(Creator).all()

    print("\nChoose Creator")
    for c in creators:
        print(f"\t{c.id}) {c.name}")
    print("\tX) New Creator")

    r = input("\nMake Selection: ")
    

    if r in ['x','X']:
        inp = input('\nCreator name: ')
        nc = Creator(name = inp)
        sesh.add(nc)
        sesh.commit()
        nc = sesh.query(Creator).filter(Creator.name == inp)[0]
        r = nc.id
    
    creator = sesh.query(Creator).filter(Creator.id == int(r))[0]
    creator.entries += 1
    sesh.commit()
    return int(r)

    

mainMenu = ["Homebrew Content Manager",
        {'1': ['Enter new creator.', addCreator],
         '2': ['View', menuAndSelectView],
         '3': ['Create.', menuAndSelectCreate]
         }]

def backOrExit(menu, sesh):
    print("\n\tb) Back")
    print("\tX) Exit\n")
    r = input("Make Selection: ")

    if r in ['x','X']:
        return
    elif r in ['b','B']:
        print('\n')
        menu(sesh)



def createItem(sesh):
    name = input('\nGive item a name: ')
    desc = input('\nGive a short description: ')
    creator = assignCreator(sesh)
    sesh.add(Item(name = name,description = desc, item_creator_id = creator))
    sesh.commit()
    menuAndSelectCreate(sesh)



def createSpell(sesh):
    name = input('\nGive spell a name: ')
    desc = input('\nGive a short description: ')
    creator = assignCreator(sesh)
    sesh.add(Spell(name = name,description = desc, spell_creator_id = creator))
    sesh.commit()
    menuAndSelectCreate(sesh)


def createRule(sesh):
    rule = input('\nEnter new rule: ')
    just = input('\nEnter Justification for new rule: ')
    creator = assignCreator(sesh)
    sesh.add(Rule(rule = rule, justification = just, rule_creator_id = creator))
    sesh.commit()
    menuAndSelectCreate(sesh)

createMenu = ['Create Homebrew Content',
            {'1': ['Create new Item.', createItem],
             '2': ['Create new Spell.', createSpell],
             '3': ['Create new Rule', createRule],
             '4': ['Back', menuAndSelectMain]}]

def displayList(resp, IDnumer = True):
   # print('\n')
    if IDnumer:
        for r in resp:
            print(f'\t{r.id}) {r}')
    else:
        i = 1
        for r in resp:
            print(f'\t{i}) {r}')
            i = i + 1
   # print('\n')


def viewItems(sesh):
    try:
        items = sesh.query(Item).all()
        displayList(items)
    except:
        print('\n\tNo Entries\n')
    backOrExit(menuAndSelectView, sesh)


def viewSpells(sesh):
    try:
        items = sesh.query(Spell).all()
        displayList(items)
    except:
        print('\n\tNo Entries\n')
    backOrExit(menuAndSelectView, sesh)

def viewRules(sesh):
    try:
        items = sesh.query(Rule).all()
        displayList(items)
    except:
        print('\n\tNo Entries\n')
    backOrExit(menuAndSelectView, sesh)

def viewCreators(sesh):
    try: 
        items = sesh.query(Creator).all()
        print('\n')
        displayList(items)
        print("\n\tb) Back")
        print("\tX) Exit\n")
        resp = input("\nSelect to view all creations: ")
        if resp in ['b','B']:
            menuAndSelectView(sesh)
            return
        elif resp in ['x','X']:
            return
        items = sesh.query(Item).filter(Item.item_creator_id == int(resp)).all()
        spells = sesh.query(Spell).filter(Spell.spell_creator_id == int(resp)).all()
        rules = sesh.query(Rule).filter(Rule.rule_creator_id == int(resp)).all()
        all = items + spells + rules
        displayList(all, False)
        backOrExit(viewCreators ,sesh)

    except:
        print('\n\tNo Entries\n')

viewMenu = ['View Homebrew Content',
            {'1': ['View Item.', viewItems],
             '2': ['View Spell.', viewSpells],
             '3': ['View Rules', viewRules],
             '4': ['View Creators', viewCreators],
             '5': ['Back', menuAndSelectMain]}]