import flet as ft


def btns(page: ft.Page):  # Experimenting with buttons.
    page.title = "Flet Counter Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_num = ft.TextField(
        value="0",
        text_align="right",
        width=120,
    )
    step_num = ft.TextField(
        value="1",
        text_align="center",
        width=100,
        label="Step size",
    )

    def minus_click(e):
        txt_num.value = str(int(txt_num.value) - int(step_num.value))
        page.update()

    def plus_click(e):
        txt_num.value = str(int(txt_num.value) + int(step_num.value))
        page.update()

    page.add(ft.Row([step_num], alignment=ft.MainAxisAlignment.CENTER))
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_num,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


def txtbox(page: ft.Page):  # Experimenting with text boxes.
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")
    page.add(
        txt_name,
        ft.ElevatedButton(
            "Say hello!",
            on_click=btn_click,
        ),
    )


def chkbox(page: ft.Page):  # Experimenting with text boxes.
    def checkbox_changed(e):
        output_text.value = f"You have learned how to ski: {todo_check.value}."
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(
        label="ToDo: Learn how to ski",
        value=False,
        on_change=checkbox_changed,
    )
    page.add(todo_check, output_text)


def dropdown(page: ft.Page):  # Experimenting with dropdown menus.
    def button_clicked(e):
        output_text.value = f"Dropdown value is: {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)


# Possible targets: btns, txtbox, chkbox, dropdown
ft.app(target=dropdown)
