import flet as ft
import flet_easy as fs

app = fs.FletEasy(route_init="/greeting")

# We add a page
@app.page(route="/flet-easy", title="Flet-Easy")
def index_page(data: fs.Datasy):
    return ft.View(
        controls=[
            ft.Text("Home page"),
            ft.FilledButton("Go to Counter", on_click=data.go("/counter")),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )
    
# We add a second page
@app.page(route="/greeting", title="greet")
def greet(data:fs.Datasy):
    page=data.page
    return ft.View(
        controls=[
            ft.Text(value='GREETING'),
            ft.FilledButton("Go to Home", on_click=data.go("/flet-easy")),
            ft.FilledButton("Go to Counter", on_click=data.go("/counter")),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )
    
# We add a second page
@app.page(route="/counter", title="Counter")
def counter_page(data: fs.Datasy):
    page = data.page

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    return ft.View(
        controls=[
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),
            ft.FilledButton("Go to Home", on_click=data.go("/flet-easy")),
            ft.FilledButton("Go to greeting", on_click=data.go("/greeting")),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )

# We run the application
app.run()