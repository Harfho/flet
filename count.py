import flet as ft 

# def main(page:ft.Page):
#     page.title='counter'
#     page.theme_mode=ft.ThemeMode.LIGHT
#     page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
#     row = ft.Row(
#         alignment=ft.MainAxisAlignment.CENTER
#     )
#     txt_counter = ft.TextField(value="0",width=100,text_align=ft.TextAlign.CENTER)
#     def add(e):
#         print(e)
#         txt_counter.value=str(int(txt_counter.value)+1) # type: ignore
#         page.update()
        
#     def sub(e):
#         print(e)
#         if(int(txt_counter.value)>=1) :# type: ignore
#             txt_counter.value=str(int(txt_counter.value)-1) # type: ignore
#         page.update()
    
#     plus = ft.IconButton(icon=ft.icons.ADD,on_click=add)
#     minus=ft.IconButton(icon=ft.icons.REMOVE,on_click=sub)
    
#     row.controls.append(plus)
#     row.controls.append(txt_counter)
#     row.controls.append(minus)
    
#     page.add(
#         row
#     )

import flet as ft

class Counter(ft.Column):
    instances = []
    counter_value = 0

    def __init__(self):
        super().__init__()
        self.txt_counter = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER)
        self.plus = ft.IconButton(icon=ft.icons.ADD, on_click=self.add)
        self.minus = ft.IconButton(icon=ft.icons.REMOVE, on_click=self.sub)
        
        self.row = ft.Row(
            controls=[
                self.plus,
                self.txt_counter,
                self.minus
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.alignment = ft.MainAxisAlignment.CENTER
        self.controls.append(self.row)
        
        Counter.instances.append(self)

    
    def add(self, e):
        self.counter_value += 1
        self.update_all()

    
    def sub(self, e):
        if self.counter_value > 0:
            self.counter_value -= 1
        self.update_all()
    
    def update_all(self):
        for instance in self.instances:
            instance.txt_counter.value = str(self.counter_value)
            instance.update()

def main(page: ft.Page):
    page.title = 'counter'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    count = Counter()
    count1 = Counter()
    
    page.add(count, count1)

ft.app(target=main)