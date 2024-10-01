from flet import *
import flet as ft

class Counter(Row):
    def __init__(self,text,count=0):
        super().__init__()
        self.count=count
        self.button=ElevatedButton(text,on_click=self.increment)
        self.text=Text(value=count,size=40)
        self.alignment=ft.MainAxisAlignment.SPACE_AROUND
        self.controls=[
            self.button,
            self.text,            
        ]
    def increment(self,e):
        self.count +=1
        self.text.value=self.count
        self.text.update()


def main(page:Page):
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.add(
        Counter('peopel'),
        Counter('animal'),
        Counter('human'),
        Counter('girl')
    )
    
    
ft.app(target=main)