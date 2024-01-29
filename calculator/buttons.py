from customtkinter import CTkButton
from calc_settings import *

class Button(CTkButton):
    def __init__(Self, parent, func, text,  col, row, font,span=1, color='dark-grey'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            corner_radius=  STYLING['corner-radius'],
            font=font,
            fg_color=COLORS[color]['fg'],
            hover_color=COLORS[color]['hover'],
            text_color=COLORS[color]['text'])
        Self.grid(column=col, columnspan=span, row=row, sticky='NSEW', padx=STYLING['gap'], pady=STYLING['gap'])

class numbutton(Button):
    def __init__(self, parent, func, text, col, row, font, span , color='light-grey'):
        super().__init__(
            parent=parent, 
            func=lambda: func(text), 
            text=text, 
            col=col, 
            row=row, 
            font=font, 
            color=color,
            span=span)

class mathbutton(Button):
    def __init__(self, parent, func, text, operator, col, row, font, color='orange'):
        super().__init__(
            parent=parent,
            text=text,
            func=lambda: func(operator),
            col=col, 
            row=row, 
            font=font, 
            color=color)