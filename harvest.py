############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(
                self,
                code,
                first_harvest,
                color,
                is_seedless,
                is_bestseller, 
                name,
                ):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
                                'yw',
                                2013,
                                'yellow',
                                False,
                                True,
                                'Yellow Watermelon'
                                )
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')

        for pair in melon.pairings:
            print(f'- {pair}')

        print()

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code.

        Takes in return of make_melon_types as the argument."""

    # melon_dict = {}

    # for melon in melon_types:
    #     melon_dict[melon.code] = melon

    # return melon_dict

    return {melon.code: melon 
            for melon in melon_types}

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(
                self,
                melon_type, 
                shape_rating, 
                color_rating, 
                field, 
                harvested_by,
                ):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by


    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else: 
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects.

        Takes in the return value of make_melon_type_lookup as the argument"""

    melons_picked = []

    melon_1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    melons_picked.append(melon_1)

    melon_2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    melons_picked.append(melon_2)

    melon_3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    melons_picked.append(melon_3)

    melon_4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila')
    melons_picked.append(melon_4)

    melon_5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael')
    melons_picked.append(melon_5)

    melon_6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael')
    melons_picked.append(melon_6)

    melon_7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael')
    melons_picked.append(melon_7)

    melon_8 = Melon(melon_types['musk'], 6, 7, 4, 'Michael')
    melons_picked.append(melon_8)

    melon_9 = Melon(melon_types['yw'], 7, 10, 3, 'Sheila')
    melons_picked.append(melon_9)

    return melons_picked

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable.

        Takes return value of make_melons as the argument. """

    for melon in melons:
        sellable = melon.is_sellable()

        if sellable == True:
            sell_phrase = 'CAN BE SOLD'
        else:
            sell_phrase = 'NOT SELLABLE'

        print(f'Harvested by {melon.harvested_by} from Field {melon.field} ({sell_phrase})')

def create_melon_obj(melon_types):
    """ Takes a harvest log and creates a list of Melon objects.

        Takes in the return value of make_melon_type_lookup as the argument"""

    fname = open('harvest_log.txt')

    melons_picked = []

    for line in fname:
        words = line.rstrip().split()

        melon_code = words[5]
        shape_rating = words[1]
        color_rating = words[3]
        field = words[11]
        harvested_by = words[8]

        melon = Melon(
                    melon_types[melon_code], 
                    shape_rating, 
                    color_rating, 
                    field, 
                    harvested_by,
                    )

        melons_picked.append(melon)

    for melon in melons_picked:
        
        if melon.melon_type.is_seedless:
            seeds = "no seeds"

        else:
            seeds = "seeds"

        print(f'The melon picked by {melon.harvested_by} is {melon.melon_type.color} and has {seeds}.')

    return melons_picked




