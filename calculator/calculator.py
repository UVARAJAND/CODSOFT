import customtkinter as ctk
from buttons import Button,  numbutton, mathbutton
import darkdetect
from calc_settings import *
try:
     from ctypes import windll, byref, sizeof, c_int
except:
     pass
class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        #setup
        super().__init__(fg_color=(WHITE, BLACK))
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)
        self.title('CALCULATOR')
        self.rowconfigure(list(range(MAIN_ROWS)), weight=1, uniform='a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1, uniform='a')
        self.result_string=ctk.StringVar(value='0')
        self.formula_string=ctk.StringVar(value='')
        self.display_nums=[]
        self.full_operation=[]
        self.create_widgets()
        self.mainloop()
    def create_widgets(self):
         main_font=ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
         result_font=ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

         OutputLabel(self, 0, 'SE', main_font, self.formula_string)
         OutputLabel(self, 1, 'E', result_font, self.result_string)
    
         Button(
              parent=self,
              func=self.clear, 
              text=OPERATOR['clear']['text'], 
              col=OPERATOR['clear']['col'], 
              row=OPERATOR['clear']['row'],
              font=main_font)
         Button(
              parent=self,
              func=self.percent, 
              text=OPERATOR['percent']['text'], 
              col=OPERATOR['percent']['col'], 
              row=OPERATOR['percent']['row'],
              font=main_font)
         Button(
              parent=self,
              func=self.invert, 
              text=OPERATOR['invert']['text'], 
              col=OPERATOR['invert']['col'], 
              row=OPERATOR['invert']['row'],
              font=main_font)
         
         for num,data in NUM_POSITIONS.items():
              numbutton(parent=self,
                        text=num,
                        func=self.num_press,
                        col=data['col'],
                        row=data['row'],
                        font=main_font,
                        span=data['span'])
         for operator,data in MATH_POSITIONS.items():
              mathbutton(
                   parent=self,
                   text=data['character'],
                   func=self.math_press,
                   operator=operator,
                   col=data['col'],
                   row=data['row'],
                   font=main_font
              )
    def num_press(self,value):
          self.display_nums.append(str(value))
          full_number=''.join(self.display_nums)
          self.result_string.set(full_number)
    def math_press(self,value):
          current_number=''.join(self.display_nums)
          if current_number:
               self.full_operation.append(current_number)
               if value != '=':
                    self.full_operation.append(value)
                    self.display_nums.clear()
                    self.result_string.set('')
                    self.formula_string.set(' '.join(self.full_operation))
               else:
                    formula=' '.join(self.full_operation)
                    result=eval(formula)
                    if isinstance(result, float):
                         if result.is_integer():
                              result=int(result)
                         else:
                              result=round(result, 3)
                    self.full_operation.clear()
                    self.display_nums=[str(result)]
                    self.result_string.set(result)
                    self.formula_string.set(formula)
    def clear(self):
          self.result_string.set(0)
          self.formula_string.set('')
          self.display_nums.clear()
          self.full_operation.clear()
    def percent(self):
          if self.display_nums:
               current_number=float(''.join(self.display_nums))
               percent_number=round(current_number/100,4)
               self.display_nums=list(str(percent_number))
               self.result_string.set(''.join(self.display_nums))
    def invert(self):
          current_number=''.join(self.display_nums)
          if current_number:
               if float(current_number)>0:
                    self.display_nums.insert(0,'-')
               else:
                    del self.display_nums[0]
               self.result_string.set(''.join(self.display_nums))
    def title_bar_color(self, is_dark):
        try:
            HWD=windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE=35
            COLOR = TITLE_BAR_HEX_COLORS['dark']if is_dark else TITLE_BAR_HEX_COLORS['light']
            windll.dwmapi.DwmSetWindowAttribute(HWD, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass
class OutputLabel(ctk.CTkLabel):
     def __init__(self, parent, row, anchor, font, string_var):
          super().__init__(master=parent, font=font, textvariable=string_var)
          self.grid(column=0, columnspan=4, row=row, sticky=anchor, padx=10)
          
if __name__=="__main__":
        Calculator(darkdetect.isDark())