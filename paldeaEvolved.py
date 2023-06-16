import random

#Arrays with all cards of each rarity

#It is worth noting that all common and uncommon cards have a reverse hollow variant with the exact same item number

#4 common cards guaranteed in each pack
common = [
    "#001 - Hoppip","#004 - Pineco","#007 - Tropius","#008 - Combee","#010 - Snover","#012 - Sprigatito",
    "#013 - Sprigatito","#016 - Tarountula","#017 - Tarountula","#019 - Nymble","#020 - Nymble","#022 - Bramblin","#023 - Bramblin",
    "#025 - Rellor","#026 - Rellor","#031 - Litleo","#034 - Fuecoco","#035 - Fuecoco","#038 - Charcadet","#039 - Charcadet","#042 - Magikarp",
    "#044 - Marill","#046 - Delibird","#047 - Luvdisc","#049 - Quaxly","#050 - Quaxly","#053 - Cetoddle","#054 - Cetoddle","#057 - Frigibax",
    "#058 - Frigibax","#062 - Pikachu","#065 - Magnemite","#066 - Voltorb", "#068 - Shinx","#069 - Shinx","#072 - Pincurchin","#074 - Pawmi",
    "#077 - Tadbulb", "#078 - Tadbulb","#080 - Wattrel","#081 - Wattrel","#083 - Jigglypuff", "#085 - Slowpoke","#087 - Misdreavus","#090 - Gothita",
    "#095 - Sandygast","#100 - Tinkatink","#101 - Tinkatink", "#102 - Tinkatink", "#106 - Mankey","#110 - Larvitar","#112 - Makuhita","#114 - Croagunk",
    "#116 - Rockruff","#119 - Falinks","#120 - Nacli","#121 - Nacli","#124 - Glimmet","#125 - Glimmet","#128 - Paldean Wooper","#129 - Paldean Wooper", "#131 - Murkrow",
    "#133 - Sneasel","#138 - Deino","#141 - Maschiff","#142 - Maschiff","#144 - Shroodle","#145 - Shroodle", "#149 - Cufant", "#152 - Noibat", "#154 - Girafarig",
    "#156 - Dunsparce","#158 - Wingull","#160 - Slakoth","#163 - Fletchling","#164 - Rookidee","#166 - Tandemaus","#167 - Tandemaus","#177 - Clavell",
    "#183 - Great Ball", "#188 - Super Rod"
]

#3 uncommon cards guranteed in each pack
uncommon = [
    "#002 - Skiploom", "#006 - Heracross", "#009 - Vespiquen", "#014 - Floragato", "#018 - Spidops", "#024 - Brambleghast", "#028 - Paldean Tauros",
    "#029 - Fletchinder", "#030 - Talonflame", "#032 - Pyroar", "#036 - Crocalor", "#041 - Paldean Tauros", "#045 - Azumarill", "#048 - Eiscue",
    "#051 - Quaxwell", "#055 - Cetitan", "#059 - Arctibax", "#064 - Raichu", "#067 - Electrode", "#070 - Luxio", "#073 - Pincurchin", "#075 - Pawmo",
    "#082 - Kilowattrel", "#088 - Mismagius", "#091 - Gothorita", "#092 - Gothitelle", "#094 - Oranguru", "#096 - Palossand", "#103 - Tinkatuff",
    "#104 - Tinkatuff", "#107 - Primeape", "#108 - Paldean Tauros", "#109 - Sudowoodo", "#111 - Pupitar", "#115 - Toxicroak", "#118 - Passimian",
    "#122 - Naclstack", "#132 - Honchkrow", "#137 - Seviper", "#139 - Zweilous", "#143 - Mabosstiff", "#146 - Grafaiai", "#147 - Bombirdier",
    "#148 - Corviknight", "#155 - Farigiraf", "#157 - Dudunsparce", "#159 - Pelipper", "#161 - Vigoroth", "#165 - Corvisquire", "#168 - Maushold",
    "#170 - Flamigo", "#171 - Artazon", "#173 - Bravery Charm", "#174 - Calamitous Snowy Mountain", "#175 - Calamitous Wasteland", "#176 - Choice Belt",
    "#178 - Delivery Drone", "#179 - Dendra", "#180 - Falkner", "#181 - Fighting Au Lait", "#182 - Giacomo", "#184 - Grusha", "#185 - Iono",
    "#186 - Practice Studio", "#187 - Saguaro", "#189 - Superior Energy Retrieval", "#190 - Jet Energy", "#191 - Luminous Energy", "#192 - Reversal Energy",
    "#193 - Therapeutic Energy"
]

#One rare card or better in each pack (Illusrator rare/special illustrator rare is not included in this)
rare = [
    "#003 - Jumpluff", "#011 - Abomasnow", "#021 - Lokix", "#033 - Oricorio", "#043 - Gyarados", "#056 - Veluza", "#060 - Baxcalibur",
    "#071 - Luxray", "#076 - Pawmot", "#084 - Wigglytuff", "#089 - Spiritomb", "#097 - Mimikyu", "#098 - Ceruledge", "#099 - Rabsca",
    "#105 - Tinkaton", "#113 - Hariyama", "#123 - Garganacl", "#126 - Glimmora", "#134 - Weavile", "#135 - Tyranitar", "#136 - Sableye",
    "#140 - Hydreigon", "#151 - Orthworm", "#162 - Slaking", "#172 - Boss's Orders"
]

# Hardest to get cards

#1 IN 15 PACKS OR ROUGHLY 6.64% PULL RATE
ultra_rare = [
    "#230 - Forretress EX", "#231 - Meowscarada EX", "#232 - Wo-Chien EX", "#233 - Skeledirge EX", "#234 - Chi-Yu EX", "#235 - Quaquaval EX",
    "#236 - Chien-Pao EX", "#237 - Bellibolt EX", "#238 - Slowking EX", "#239 - Dedenne EX", "#240 - Tinkaton EX", "#241 - Lycanroc EX",
    "#242 - Annihilape EX", "#243 - Ting-Lu EX", "#244 - Paldean Clodsire EX", "#245 - Copperajah EX", "#246 - Noivern EX", "#247 - Squawkabilly EX",
    "#248 - Boss's Orders", "#249 - Clavell", "#250 - Dendra", "#251 - Falkner", "#252 - Giacomo", "#253 - Grusha", "#254 - Iono", "#255 - Saguaro"
]

#1 IN 7 PACKS OR ROUGHLY A 13.72% PULL RATE
double_rare = [
    "#005 - Forretress EX", "#015 - Meowscarada EX", "#027 - Wo-Chien EX", "#037 - Skeledirge EX", "#040 - Chi-Yu EX", "#052 - Quaquaval EX",
    "#061 - Chien-Pao EX", "#063 - Pikachu EX", "#079 - Bellibolt EX", "#086 - Slowking EX", "#093 - Dedenne EX", "#117 - Lycanroc EX",
    "#127 - Ting-Lu EX", "#130 - Paldean Clodsire EX", "#150 - Copperajah EX", "#153 - Noivern EX", "#169 - Squawkabilly EX"
]

#1 IN 13 PACKS OR ROUGHLY A 7.7% PULL RATE
illustration_rare = [
    "#194 - Heracross", "#195 - Tropius", "#196 - Sprigatito", "#197 - Floragato", "#198 - Bramblin", "#199 - Fletchinder",
    "#200 - Pyroar", "#201 - Fuecoco", "#202 - Crocalor", "#203 - Magikarp", "#204 - Marill", "#205 - Eiscue",
    "#206 - Quaxly", "#207 - Quaxwell", "#208 - Frigibax", "#209 - Arctibax", "#210 - Baxcalibur", "#211 - Raichu",
    "#212 - Mismagius", "#213 - Gothorita", "#214 - Sandygast", "#215 - Rabsca", "#216 - Tinkatink", "#217 - Tinkatuff",
    "#218 - Paldean Tauros", "#219 - Sudowoodo", "#220 - Nacli", "#221 - Paldean Wooper", "#222 - Tyranitar", "#223 - Grafaiai",
    "#224 - Orthworm", "#225 - Rookidee", "#226 - Maushold", "#227 - Flamigo", "#228 - Farigiraf", "#229 - Dudunsparce"
]

#1 IN 32 PACKS OR ROUGHLY A 3.17% PULL RATE
special_illustration = [
    "#256 - Meowscarada EX", "#257 - Wo-Chien EX", "#258 - Skeledirge EX", "#259 - Chi-Yu EX", "#260 - Quaquaval EX",
    "#261 - Chien-Pao EX", "#262 - Tinkaton EX", "#263 - Ting-Lu EX", "#264 - Squawkabilly EX", "#265 - Boss's Orders",
    "#266 - Dendra", "#267 - Giacomo", "#268 - Grusha", "#269 - Iono", "#270 - Saguaro"
]

#1 IN 57 PACKS OR ROUGHLY A 1.76% PULL RATE
hyper_rare = [
    "#271 - Meowscarada EX", "#272 - Skeledirge EX", "#273 - Quaquaval EX", "#274 - Chien-Pao EX", "#275 - Ting-Lu EX",
    "#276 - Super Rod", "#277 - Superior Energy Retrieval", "#278 - Basic Grass Energy", "#279 - Basic Water Energy"
]

reverseHoloLst = common + uncommon



def common_pulls(): #4 of them
    common1 = random.choice(common)
    common2 = random.choice(common)
    common3 = random.choice(common)
    common4 = random.choice(common)

    return common1
    return common2
    return common3
    return common4
    #return common1,common2,common3,common4


def uncommon_pulls(): #3 of them
    uncommon1 = random.choice(uncommon)
    uncommon2 = random.choice(uncommon)
    uncommon3 = random.choice(uncommon)
    
    return uncommon1
    return uncommon2
    return uncommon3
    
    #return uncommon1,uncommon2,uncommon3

def reverse_holo():
    reverseHolo1 = random.choice(reverseHoloLst)
    return reverseHolo1
    
    #return reverseHolo1 + " -Reverse Holo"

def reverse_holo_plus():
    possibilities = [reverseHoloLst, illustration_rare, special_illustration]
    probabilities = [0.8913, 0.077, 0.0317]
    chosen_option = random.choices(possibilities, probabilities)[0]
    randomCard = random.choice(chosen_option)

    return randomCard

def rare_plus():
    possibilities = [rare, double_rare, ultra_rare, hyper_rare]
    probabilities = [0.7788,0.1372, 0.0664, 0.0176]
    chosen_option = random.choices(possibilities, probabilities)[0]
    randomCard = random.choice(chosen_option)

    return randomCard

def pull_all_cards():
    common_cards = common_pulls()
    uncommon_cards = uncommon_pulls()
    reverse_holo = reverse_holo()
    reverse_holo_plus = reverse_holo_plus()
    rare_card = rare_plus()
    
    return common_cards, uncommon_cards, reverse_holo_plus, rare_card

def pull_all_cards():
    
    common_cards = []
    uncommon_cards = []

    # Pull 4 common cards
    for _ in range(4):
        common_card = random.choice(common)
        common_cards.append(common_card)

    # Pull 3 uncommon cards
    for _ in range(3):
        uncommon_card = random.choice(uncommon)
        uncommon_cards.append(uncommon_card)

    reverse_holo_card = reverse_holo()
    reverse_holo_card_plus = reverse_holo_plus()
    rare_card = rare_plus()

    for card in common_cards:
        print("Common:", card)

    print("\n")
    for card in uncommon_cards:
        print("Uncommon:", card)
    
    print("\n")
    print("Reverse Holo:", reverse_holo_card)
    
    print("\n")
    if reverse_holo_card_plus in illustration_rare:
        print("Illustrator Rare:", reverse_holo_card_plus)
    elif reverse_holo_card_plus in special_illustration:
        print("Special Illustrator Rare:", reverse_holo_card_plus)
    else:
        print("Reverse Holo:", reverse_holo_card_plus)

    print("\n")
    if rare_card in double_rare:
        print("Double Rare:", rare_card)
    elif rare_card in hyper_rare:
        print("Hyper Rare:", rare_card)
    elif rare_card in ultra_rare:
        print("Ultra Rare:", rare_card)
    else:
        print("Rare:", rare_card)


    return common_cards, uncommon_cards, reverse_holo_card, reverse_holo_card_plus, rare_card


pull_all_cards()



    
    
    







