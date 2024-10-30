from flet import *  # type: ignore


def main(page: Page):
    navbar = Row(
        [
            Image(src="logo.jpg", width=200, height=200),
            Text("App Name"),
            TextButton("Login"),
        ]
    )

    sidebar = Column(
        [
            Text("Dashboard"),
            Text("Users"),
            Text("Settings"),
        ]
    )

    main_area = Container(
        Text("Main Area"),
        padding=padding.all(10),
        border=border.all(2, "black"),
    )

    card = Stack([Image(src="kids.jpg", width=200, height=200), Text("Description")])
    page.add(Column([navbar, Row([sidebar, main_area, card])]))


app(target=main)
