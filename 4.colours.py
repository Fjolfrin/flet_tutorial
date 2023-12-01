import flet as ft


def main(page: ft.Page):
    container = ft.Container(
        width=200,
        height=200,
        border=ft.border.all(1, ft.colors.BLACK),
        content=ft.FilledButton("Primary color"),
        theme=ft.Theme(
            color_scheme=ft.ColorScheme(primary=ft.colors.GREEN_400),
        ),
    )

    page.add(container)


ft.app(target=main)
