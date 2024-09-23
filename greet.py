import flet as ft

def main(page:ft.Page):    
    page.title='Test'
    page.theme_mode=ft.ThemeMode.LIGHT
    page.window.always_on_top=True
    page.window.width=300
    page.window.height=300

    info = ft.Column(adaptive=True)
    def submit(e):
        first_name = first.value
        second_name= second.value
        if first_name and second_name:
            print(first.value)
            info.controls.append(ft.Text(value=f'Hello {first_name} {second_name}')) # type: ignore
            first.value=''
            second.value=''
            # page.add(info)
            page.update()
        first.autofocus=True
        

    text = ft.Text(value='Hello')
    first=ft.TextField(label='first',autofocus=True)
    second=ft.TextField(label='second name')
    button = ft.ElevatedButton(text='click me',on_click=submit)

    page.add(
        first,
        second,
        button,
        info
    )






ft.app(target=main)# type: ignore
