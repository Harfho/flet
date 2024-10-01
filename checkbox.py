from flet import *
import flet as ft


class mycheck(Checkbox):
    def __init__(self,label,value):
        super().__init__()
        self.label=label
        self.value=value
        self.on_change=self.change
        self.page=Page
    
    def change(self,e):
        print(e)
        text = ft.Text(value=f"{self.label} is {e.data}")
        print(text)
        self.page.add(text)
        
    

def main(page:Page):    
        
    # check=ft.Checkbox(label='text',value=False,on_change=change)
    # check1=ft.Checkbox(label='text1',value=False,on_change=change)
    # check2=ft.Checkbox(label='text2',value=False,on_change=change)
    check=mycheck('text',False,)
    check1=mycheck('text1',False,)
    check2=mycheck('tex2t',False,)

    
    print(text)
    page.add(
        check,
        check1,
        check2,

    )

ft.app(target=main)