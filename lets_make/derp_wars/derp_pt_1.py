import random

def still_playing():
    """check for end conditions"""
    return True  # TODO add win/lose conditions

day = 0  # starting day

def start_day():
    """a banner that signals a new round and lists remaining days"""
    global day
    day += 1
    print(f"\n===================================")
    print(f"|                                 |")
    print(f"|             Day {day}               |")
    print(f"|                                 |")
    print(f"===================================")

derps = [
    'laptop stickers',
    'deepfake cat pics',
    'conference swag',
    'hand sanitizer',
    'iced espresso americano',
    "floppy disk (8\" SSSD)",
]

def gen_inventory(derps):
    """generates an empty starter inventory for the influencer"""
    inventory = {}
    for derp in derps:
        inventory[derp] = 0
    return inventory

# generate starting inventory for player (empty)
inventory = gen_inventory(derps)
clout = 20  # starting funds
currency = 'c (Clout)'

def list_currency():
    print(f"You have {clout}{currency} in your fanny pack.\n")

locations = [
    "ruddit.com/ragrets",
    '7chin',
    'the dork web',
    'an coffee shop',
    "some hacker's basement"
]

def get_locations(places):
    """returns a list of 3 random locations"""
    random.shuffle(places)  # shuffle in place
    return places[:3] # return the first 3

def list_locations(places):
    """print a list of locations the player can move this turn"""
    print("======== L O C A T I O N S ========")
    for num,place in enumerate(places):
        print(f"{num+1}) {place}")
    print('')

def list_inventory():
    """print inventory & clout prettily™ on screen"""
    print('\n======== I N V E N T O R Y ========')
    # if inventory is empty, say so explicitely
    if all(val == 0 for val in inventory.values()):
        print("\nYour inventory is currently empty. feelsbadman.jpg.")
    # otherwise, print the inventory
    else:
        print('QTY | DERP')
        print('----+------------------------------')
        # only list items that have inventory
        for item,qty in inventory.items():
            if qty > 0:
                print(f"{qty}   | {item}")
    print('')  # extra line at the end looks kleeeeen 👌

def prompt():
    """get input from the player"""
    try:
        return int(input(f"[ DAY {day} | {clout}{currency[0]} ] >>> "))
    except ValueError:  # in case they send an empty string or a weird char
        return False


def get_move():
    """ask the player where they want to go"""
    # keep asking whre they want to go until they give a valid input
    while True:
        print('Where to, Dude? ')
        move = prompt()
        if 1 <= move <= 3:
            break
        else:
            print("\nThat location doesn't exist. Try again! :D")
    return move

def display_location(location):
    """print where the player chose to move on screen"""
    print(f"\nYou've arrived at {location}.\n")

def get_rates():
    """returns derps at random rates"""
    derp_rates = {}
    for derp in derps:
        derp_rates[derp] = random.randint(1,10)
    return derp_rates

def display_rates(rates):
    """show the rates of everything that's for sale"""
    print(' # |  C  | DERP')
    print('---+-----+-------------------------')
    index = 1
    for derp,rate in rates.items():
        print(f"{index:>2} | {rate:>2}{currency[0]} | {derp}")
        index += 1
    print('')

def prompt_buyer():
    """ask the player what they want to buy and return an int"""
    # keep asking until they return a valid input
    print("What do you want to buy, cool guy?")
    while True:
        purchase = prompt()
        # check to see if their input is valid
        if 1 <= purchase <= len(derps):
            break
        else:
            print("\nThat's not something you can *technically* buy here... Try again.")
    return purchase - 1

def can_buy(rate):
    """make a purchase."""
    # check to see if they have enough money first
    if rate > clout:
        return False
    return True # let 'em know the buy was successful

def report_purchase(derp, rate):
    """prints what the player purchased and for how much"""
    print(f"\nAiight. You just bought some {derps[derp]} for {rate}{currency[0]}")

def make_purchase(derp, rate):
    global clout
    inventory[derps[derp]] += 1  # adjust their inventory
    clout -= rate  # remove the clout from their fanny pack (US)
    report_purchase(derp, rate)

def splash_screen():
    print('')
    print("|￣￣￣￣￣￣ |")
    print("|   WELCOM   |")
    print("|    TO      |")
    print("|     DERP   |")
    print("|   WARS     |")
    print("| ＿＿＿＿＿__|")
    print("(\__/) ||")
    print("(•ㅅ•) ||")
    print("/ 　 づ")

splash_screen()

while still_playing():

    # show how many days are left
    start_day()

    # show the player their inventory
    list_inventory()
    list_currency()

    # show the player some locations & ask them where they want to go
    move_options = get_locations(locations)
    list_locations(move_options)
    location = move_options[get_move()-1]

    # move the player
    display_location(location)

    # show the player what's for sale and ask what they want to buy
    rates = get_rates()
    display_rates(rates)
    while True:
        purchase = prompt_buyer()
        if can_buy(rates[derps[purchase]]):
            # report/track/log the purchase & update their inventory
            make_purchase(purchase, rates[derps[purchase]])
            break
        else:
            print("\nDude! You don't have enough money! Buy something else..\n")