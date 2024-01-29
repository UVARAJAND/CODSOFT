WHITE="#EEEEEE"
BLACK="#000000"
APP_SIZE=(400,700)
MAIN_COLUMNS=4
MAIN_ROWS=7

FONT="Century Gothic"
OUTPUT_FONT_SIZE=70
NORMAL_FONT_SIZE=32

STYLING={
    'gap':0.5,
    'corner-radius':0
}

NUM_POSITIONS={
    '.': {'col':2, 'row':6,'span':1},
    0 : {'col':0, 'row':6,'span':2},
    1 : {'col':0, 'row':5,'span':1},
    2 : {'col':1, 'row':5,'span':1},
    3 : {'col':2, 'row':5,'span':1},
    4 : {'col':0, 'row':4,'span':1},
    5 : {'col':1, 'row':4,'span':1},
    6 : {'col':2, 'row':4,'span':1},
    7 : {'col':0, 'row':3,'span':1},
    8 : {'col':1, 'row':3,'span':1},
    9 : {'col':2, 'row':3,'span':1}
}
MATH_POSITIONS={
    '/': {'col':3, 'row':2, 'character':'/', 'image path': None},
    '*': {'col':3, 'row':3, 'character':'x', 'image path': None},
    '-': {'col':3, 'row':4, 'character':'-', 'image path': None},
    '=': {'col':3, 'row':6, 'character':'=', 'image path': None},
    '+': {'col':3, 'row':5, 'character':'+', 'image path': None}
}
OPERATOR={
    'clear':{'col':0, 'row':2, 'text':'AC', 'image path':None},
    'invert':{'col':1, 'row':2, 'text':'+/-', 'image path':None},
    'percent':{'col':2, 'row':2, 'text':'%', 'image path':None}
}
COLORS={
    'light-grey': {'fg':('#505050','#D4D4D2'), 'hover':('#686868','#EFEFED'), 'text': ('white','black')},
    'dark-grey': {'fg':('#D4D4D2','#505050'), 'hover':('#EFEFED','#686868'), 'text': ('black','white')},
    'orange': {'fg':'#ff9500', 'hover':'#ffb143', 'text': ('white','black')},
    'orange-highlight': {'fg':'white', 'hover':'white', 'text': ('black','#ff9500')}
}
TITLE_BAR_HEX_COLORS={
    'dark': 0x00000000,
    'light': 0x00EEEEEE
}