from flet import *
import flet as ft


def main(page:ft.Page):
    page.horizontal_alignment='center'
    page.theme_mode=ThemeMode.LIGHT
    logo=Image(src='logo.jpg',            
               fit=ImageFit.CONTAIN
               )
    logoCon=Container(
        content=logo,
        width=500,
        height=200,
        border_radius=BorderRadius(top_left=500,top_right=100,bottom_left=100,bottom_right=500)
        
        
    )
    
    def update_text(e):
        text.content.value=e.data
        text.update()
        
    search = TextField(label='ENTER THE SENTENCE',text_style=TextStyle(weight=FontWeight.BOLD),
                       prefix_icon=icons.ABC,
                       on_change=update_text)
    

        
    text =Container(
        content=Text(value='SOME SENTENCE',size=30,style=TextThemeStyle.LABEL_SMALL),
        bgcolor="#b3ff00a",
        border_radius=20,
        padding=padding.symmetric(20)
    )
    page.add(
        logoCon,
        search,
        text,
        Container(content=Image(src='kids.jpg',fit=ImageFit.CONTAIN,height=300))
    )
app(target=main)