import flet as ft
import time

# This is my first tryout with Flet!


def main(page: ft.Page):  # Some experimentation with flet structures.
    t = ft.Text()
    page.add(t)

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(
        ft.Row(
            [
                ft.Text("A"),
                ft.Text("B"),
                ft.Text("C"),
            ]
        )
    )
    page.add(
        ft.Row(
            [
                ft.TextField(label="Your name..."),
                ft.ElevatedButton(text="See my name!"),
            ]
        )
    )

    page.add(
        ft.ElevatedButton(
            text="Click me!",
            on_click=button_clicked,
        )
    )

    for i in range(10):
        # page.controls.append(ft.Text(f"Line {i}"))
        # if i > 4:
        #     page.controls.pop(0)
        # page.update()
        # time.sleep(0.3)
        t.value = f"Step: {i}."
        page.update()
        time.sleep(1)


def todo(page: ft.Page):  # A simple ToDo list.
    def add_clicked(e):
        page.add(
            ft.Checkbox(
                label=new_task.value,
            ),
        )
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(
        hint_text="What needs to be done?",
        width=300,
    )
    page.add(
        ft.Row(
            [
                new_task,
                ft.ElevatedButton("Add", on_click=add_clicked, key="Enter"),
            ]
        )
    )


def disabled(page: ft.Page):  # Experimentations with the `disabled` attribute.
    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(
        [
            first_name,
            last_name,
        ]
    )
    c.disabled = True
    page.add(c)


def controlrefs(page: ft.Page):  # Experimentation with control references.
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.TextField]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="First name", autofocus=True),
        ft.TextField(ref=last_name, label="Last name"),
        ft.ElevatedButton("Say Hello!", on_click=btn_click),
        ft.Column(ref=greetings),
    )


# Possible targets: main, todo, disabled, controlrefs
ft.app(target=controlrefs)
