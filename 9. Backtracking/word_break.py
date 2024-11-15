elements = {
    'h': 'Hydrogen',
    'he': 'Helium',
    'li': 'Lithium',
    'be': 'Beryllium',
    'b': 'Boron',
    'c': 'Carbon',
    'n': 'Nitrogen',
    'o': 'Oxygen',
    'f': 'Fluorine',
    'ne': 'Neon',
    'na': 'Sodium',
    'mg': 'Magnesium',
    'al': 'Aluminum',
    'si': 'Silicon',
    'p': 'Phosphorus',
    's': 'Sulfur',
    'cl': 'Chlorine',
    'ar': 'Argon',
    'k': 'Potassium',
    'ca': 'Calcium',
    'sc': 'Scandium',
    'ti': 'Titanium',
    'v': 'Vanadium',
    'cr': 'Chromium',
    'mn': 'Manganese',
    'fe': 'Iron',
    'co': 'Cobalt',
    'ni': 'Nickel',
    'cu': 'Copper',
    'zn': 'Zinc',
    'ga': 'Gallium',
    'ge': 'Germanium',
    'as': 'Arsenic',
    'se': 'Selenium',
    'br': 'Bromine',
    'kr': 'Krypton',
    'rb': 'Rubidium',
    'sr': 'Strontium',
    'y': 'Yttrium',
    'zr': 'Zirconium',
    'nb': 'Niobium',
    'mo': 'Molybdenum',
    'tc': 'Technetium',
    'ru': 'Ruthenium',
    'rh': 'Rhodium',
    'pd': 'Palladium',
    'ag': 'Silver',
    'cd': 'Cadmium',
    'in': 'Indium',
    'sn': 'Tin',
    'sb': 'Antimony',
    'te': 'Tellurium',
    'i': 'Iodine',
    'xe': 'Xenon',
    'cs': 'Cesium',
    'ba': 'Barium',
    'la': 'Lanthanum',
    'ce': 'Cerium',
    'pr': 'Praseodymium',
    'nd': 'Neodymium',
    'pm': 'Promethium',
    'sm': 'Samarium',
    'eu': 'Europium',
    'gd': 'Gadolinium',
    'tb': 'Terbium',
    'dy': 'Dysprosium',
    'ho': 'Holmium',
    'er': 'Erbium',
    'tm': 'Thulium',
    'yb': 'Ytterbium',
    'lu': 'Lutetium',
    'hf': 'Hafnium',
    'ta': 'Tantalum',
    'w': 'Tungsten',
    're': 'Rhenium',
    'os': 'Osmium',
    'ir': 'Iridium',
    'pt': 'Platinum',
    'au': 'Gold',
    'hg': 'Mercury',
    'tl': 'Thallium',
    'pb': 'Lead',
    'bi': 'Bismuth',
    'po': 'Polonium',
    'at': 'Astatine',
    'rn': 'Radon',
    'fr': 'Francium',
    'ra': 'Radium',
    'ac': 'Actinium',
    'th': 'Thorium',
    'pa': 'Protactinium',
    'u': 'Uranium',
    'np': 'Neptunium',
    'pu': 'Plutonium',
    'am': 'Americium',
    'cm': 'Curium',
    'bk': 'Berkelium',
    'cf': 'Californium',
    'es': 'Einsteinium',
    'fm': 'Fermium',
    'md': 'Mendelevium',
    'no': 'Nobelium',
    'lr': 'Lawrencium',
    'rf': 'Rutherfordium',
    'db': 'Dubnium',
    'sg': 'Seaborgium',
    'bh': 'Bohrium',
    'hs': 'Hassium',
    'mt': 'Meitnerium',
    'ds': 'Darmstadtium',
    'rg': 'Roentgenium',
    'cn': 'Copernicium',
    'nh': 'Nihonium',
    'fl': 'Flerovium',
    'mc': 'Moscovium',
    'lv': 'Livermorium',
    'ts': 'Tennessine',
    'og': 'Oganesson'
}

def periodic_table_words(s: str) -> tuple[str, list[str]] | None:
    result: list[str] = []
    names: list[str] = []
    word: str
    for word in s.split():
        r: list[str] | None = find(word, set(elements.keys()))
        if r is not None:
            result.append('-'.join([c.capitalize() for c in r]))
            e: str
            for e in r:
                names.append(elements[e])
        else:
            return None
    return ('  '.join(result), names)


def find(s: str, words: set[str], answer: list[str] = []) -> list[str] | None:
    if s == '':
        return answer
    index: int = 0
    word: str = ''
    while index < len(s):
        word += s[index]
        if word in words:
            new_answer: list[str] | None = find(s[index + 1:], words, answer + [word])
            if new_answer is not None:
                return new_answer
        index += 1
    return None


if __name__ == '__main__':
    from pprint import pprint
    words: set[str] = {
        'the', 'a', 'an', 'boy', 'girl',
        'dog', 'ran', 'ate', 'homework',
        'table', 'them', 'my', 'kissed'
    }
    # print(find('thedog', words))
    # print(find('thedogatemyhomework', words))
    # print(find('thegirlkissedtheboy', words))
    # print(len(elements))
    pprint(periodic_table_words('white chocolate sucks'))
    pprint(periodic_table_words('this fat boy thinks you watch black hats'))
    pprint(periodic_table_words('yes i think you scare python babies in argentina'))
    pprint(periodic_table_words('un taco bebe'))
