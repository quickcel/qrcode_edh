#Mana Symbols
MANA_SYMBOL = {
    'w':'static/img/white.svg',
    'u':'static/img/blue.svg',
    'b':'static/img/black.svg',
    'r':'static/img/red.svg',
    'g':'static/img/green.svg',
}

#Mono Color
TRUE_WHITE = {'r':255, 'g':255, 'b':255} #ffffff
GRAY = {'r':50, 'g':50, 'b':50}

WHITE = {'r':248, 'g':231, 'b':185, 'mana_svg': MANA_SYMBOL['w']} #f8e7b9
BLUE = {'r':14, 'g':104, 'b':171, 'mana_svg': MANA_SYMBOL['u']} #0e68ab
BLACK = {'r':21, 'g':11, 'b':0, 'mana_svg': MANA_SYMBOL['b']} #150b00
RED = {'r':211, 'g':32, 'b':42, 'mana_svg': MANA_SYMBOL['r']} #d3202a
GREEN = {'r':0, 'g':115, 'b':62, 'mana_svg': MANA_SYMBOL['g']} #00733e

#Dual Color
AZORIUS = {'r':131, 'g':168, 'b':178}
DIMIR  = {'r':18, 'g':58, 'b':86}
RAKDOS = {'r':116, 'g':22, 'b':21}
GRUUL = {'r':106, 'g':74, 'b':52}
SELESNYA = {'r':124, 'g':173, 'b':124}
ORZHOV = {'r':135, 'g':121, 'b':93}
IZZET = {'r':113, 'g':68, 'b':107}
GOLGARI = {'r':11, 'g':63, 'b':31}
BOROS = {'r':230, 'g':132, 'b':114}
SIMIC = {'r':7, 'g':110, 'b':117}

#Tri Color
ESPER = {'r':94, 'g':115, 'b':119}
GRIXIS = {'r':82, 'g':49, 'b':71}
JUND = {'r':77, 'g':53, 'b':35}
NAYA = {'r':153, 'g':126, 'b':96}
BANT = {'r':87, 'g':150, 'b':139}
ABZAN = {'r':90, 'g':119, 'b':82}
JESKAI = {'r':158, 'g':122, 'b':133}
SULTAI = {'r':12, 'g':77, 'b':78}
MARDU = {'r':160, 'g':91, 'b':76}
TEMUR = {'r':75, 'g':84, 'b':92}

#Color of commander text underneath the code
TEXT_COLOR = {
    'r':BLACK['r'],
    'g':BLACK['g'],
    'b':BLACK['b']
}

#QR Code Color: Used for 3+ color commanders
QR_CODE_COLOR = {
    'r':BLACK['r'],
    'g':BLACK['g'],
    'b':BLACK['b']   
}


#Paper
#All unit measurements are in points (72 points = 1 inch)
DOC_W = 612
DOC_H = 792
DOC_COLS = 3
DOC_ROWS = 4

MARGIN_T = 46.44
MARGIN_R = 45
MARGIN_B = 46.44
MARGIN_L = 45

MARGIN_HORIZ = 45
MARGIN_VERT = 41.04

CELL_W = 144
CELL_H = 144
CELL_BLEED = 9
