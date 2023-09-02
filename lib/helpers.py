
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



def createItem(sesh):
    name = input('\nGive item a name: ')
    desc = input('\nGive a short description: ')
    creator = assignCreator(sesh)
    sesh.add(Item(name = name,description = desc, item_creator_id = creator))
    sesh.commit()


def createSpell(sesh):
    name = input('\nGive spell a name: ')
    desc = input('\nGive a short description: ')
    creator = assignCreator(sesh)
    sesh.add(Spell(name = name,description = desc, spell_creator_id = creator))
    sesh.commit()


def createRule(sesh):
    rule = input('\nEnter new rule: ')
    just = input('\nEnter Justification for new rule: ')
    creator = assignCreator(sesh)
    sesh.add(Rule(rule = rule, justification = just, rule_creator_id = creator))
    sesh.commit()

createMenu = ['Create Homebrew Content',
            {'1': ['Create new Item.', createItem],
             '2': ['Create new Spell.', createSpell],
             '3': ['Create new Rule', createRule],
             '4': ['Back', menuAndSelectMain]}]

def displayList(resp):
    print('\n')
    for r in resp:
        print(f'\t{r.id}) {r}')
    print('\n')


def viewItems(sesh):
    try:
        items = sesh.query(Item).all()
        displayList(items)
    except:
        print('\n\tNo Entries\n')


def viewSpells(sesh):
    try:
        items = sesh.query(Spell).all()
        displayList(items)
    except:
        print('\n\tNo Entries\n')


def viewRules(sesh):
    try:
        items = sesh.query(Rule).all()
        displayList(items)
    except:
        print('\n\tNo Entries\n')

def viewCreators(sesh):
    try: 
        items = sesh.query(Creator).all()
        displayList(items)
    except:
        print('\n\tNo Entries\n')

viewMenu = ['View Homebrew Content',
            {'1': ['View Item.', viewItems],
             '2': ['View Spell.', viewSpells],
             '3': ['View Rules', viewRules],
             '4': ['View Creators', viewCreators],
             '5': ['Back', menuAndSelectMain]}]