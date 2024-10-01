from flet import *



def main(page:Page):
    
    drop_list=Dropdown(
        label='testi',
        options=[dropdown.Option('green')]
    )
    
    page.add(
        drop_list
    )


app(target=main)