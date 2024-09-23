import flet  as ft

# def main(page:ft.Page):
    
#     page.theme_mode=ft.ThemeMode.LIGHT
    
    
#     text1=ft.TextField(value="0",width=50)
    
#     text2=ft.TextField(value="100",width=50)
    
#     def add5(e):
#         text1.value = str(int(text1.value)+5)
#         page.update()
    
#     def sub5(e):
#         text2.value = str(int(text2.value)-5)
#         page.update()
        
#     first_button = ft.IconButton(icon=ft.icons.ADD,on_click=add5)
    
#     second_button = ft.IconButton(icon=ft.icons.REMOVE,on_click=sub5)
    
#     page.add(
#         ft.Row(
#         controls=[
#         first_button,
#         text1,
#         text2,
#         second_button
#         ],
#         alignment=ft.MainAxisAlignment.CENTER
#         ),
        
#     )


class new(ft.Column):
    def __init__(self) -> None:
        super().__init__()        
        self.text1=ft.TextField(value="0",width=50)
        
        self.text2=ft.TextField(value="100",width=50)
        
        self.first_button = ft.IconButton(icon=ft.icons.ADD,on_click=self.add5)
    
        self.second_button = ft.IconButton(icon=ft.icons.REMOVE,on_click=self.sub5)
        
        self.controls.append(
            ft.Row(
            controls=[
            self.first_button,
            self.text1,
            self.text2,
            self.second_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        )
        self.alignment=ft.MainAxisAlignment.CENTER
    def add5(self,e):
        self.text1.value = str(int(self.text1.value)+5)
        self.update()
    
    def sub5(self,e):
        self.text2.value = str(int(self.text2.value)-5)
        self.update()
            
       

def main(page:ft.Page):
    page.theme_mode=ft.ThemeMode.LIGHT
    t = new()
    page.add(
        t
    )
ft.app(target=main)    