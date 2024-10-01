import flet as ft

def main(page: ft.Page):
    page.title = "Final Autoclaim - Access Profile"
    # page.vertical_alignment='center'
    page.horizontal_alignment='center'
    # Text for header
    header = ft.Text(
        "Access Your Profile",
        size=30,
        weight="bold",
        color="blue",
        text_align=ft.TextAlign.CENTER
    )
    
    # Text for email label
    email_label = ft.Text(
        "Unique Email Address:",
        size=15,
        color="black",
    )
    
    # Email input TextField
    email_input = ft.TextField(
        label="Enter your given unique Email",
        width=400,
    )
    
    # Load Profile button
    load_button = ft.ElevatedButton(
        text="LOAD PROFILE",
        width=200,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.GREEN,
        on_click=lambda e: print("Load Profile clicked")
    )
    
    # Join WhatsApp group button
    whatsapp_button = ft.TextButton(
        text="Join our WhatsApp group to stay updated!",
        icon=ft.icons.WECHAT_SHARP,
        icon_color=ft.colors.GREEN,
        style=ft.ButtonStyle(bgcolor='green',color='#ffffff'),
        on_click=lambda e: page.launch_url("https://chat.whatsapp.com/join")
    )
    
    # Layout: Add everything to a Column
    page.add(
        ft.Container(
        content=ft.Column(
            [
                header,
                email_label,
                email_input,
                load_button,
                whatsapp_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
                    
        ),
        bgcolor='#f4ebebff',
        
        )
    )

# Run the Flet app
ft.app(target=main)
