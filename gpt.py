import flet as ft


class Message:
    def __init__(self, user_name: str, text: str, message_type: str) -> None:
        self.user_name = user_name
        self.text = text
        self.message_type = message_type


class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = "center"
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color="white",
                bgcolor=self.get_avatar_color(message.user_name),
            ),
            ft.Column(
                controls=[
                    ft.Text(
                        message.user_name,
                        width="bold",
                        font_family="RoosterPersonalUse",
                    ),
                    ft.Text(message.text, selectable=True, width=500),
                ]
            ),
        ]

    def get_initials(self, username: str):
        return username[0].upper()

    def get_avatar_color(self, message):
        return ft.colors.random_color()


def main(page: ft.Page):
    page.fonts = {"RoosterPersonalUse": "RoosterPersonalUse-3z8d8"}
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window.width = 500
    page.window.height = 500
    page.theme_mode = ft.ThemeMode.LIGHT
    # message = Message("kolade", "testing", "msg")
    # chat = ChatMessage(message)

    def closeAlert(e):
        print(user_join)
        print(e)
        if user_join.value:
            page.session.set("user_name", user_join.value)
            page.overlay[0].open = False
            ask.prefix_text = f"{user_join.value}:"
            page.pubsub.send_all(
                Message(
                    user_name=f"{user_join.value}",
                    text=f"{user_join.value} just joined the chat",
                    message_type="login",
                )
            )
        else:
            user_join.border_color = ft.colors.RED
            error_text.value = "Please Enter Your name"
        page.update()

    def send_message(e):
        page.pubsub.send_all(
            Message(
                user_name=f"{page.session.get("user_name")}",
                text=f"{ask.value}",
                message_type="chat",
            )
        )
        ask.value = ""
        page.pubsub.send_all(
            Message(
                user_name="bot",
                text="Gettting Message",
                message_type="chat",
            )
        )
        page.update()

    def on_message(message: Message):
        if message.message_type == "chat":
            m = ChatMessage(message)
        else:
            m = ft.Text(message.text)

        chats.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    user_join = ft.TextField(label="Enter Your name")
    error_text = ft.Text(color=ft.colors.RED, size=10)
    page.overlay.append(
        ft.AlertDialog(
            title=ft.Text("ENTER YOUR USER NAME"),
            content=ft.Column(
                controls=[user_join, error_text], width=20, height=50, tight=True
            ),
            open=True,
            actions=[
                ft.ElevatedButton("shoe", on_click=closeAlert),
                ft.TextButton("ss"),
            ],
            modal=True,
        )
    )

    chats = ft.ListView(expand=True, spacing=50, auto_scroll=True, divider_thickness=10)

    ask = ft.TextField(
        hint_text="Enter your question.....",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=10,
        expand=True,
        filled=True,
        on_submit=send_message,
    )

    icon_send = ft.IconButton(
        ft.icons.SEND_ROUNDED,
        tooltip="click to send",
        icon_color=ft.colors.GREEN,
        on_click=send_message,
    )
    page.add(
        ft.Container(
            content=chats,
            border=ft.border.all(2, ft.colors.GREEN),
            padding=10,
            border_radius=20,
            expand=True,
        ),
        ft.Row([ask, icon_send]),
    )


ft.app(target=main, assets_dir="speedTest/assets")
