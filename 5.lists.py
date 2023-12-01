import os

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"
import flet as ft


def bad_idea_list(page: ft.Page):
    ##### This code is a bad idea #####
    for i in range(5000):
        page.controls.append(ft.Text(f"line {i}"))
    page.scroll = "always"
    page.update()
    ###################################


def list_view(page: ft.Page):
    lv = ft.ListView(
        expand=True,
        spacing=10,
    )
    for i in range(5000):
        lv.controls.append(
            ft.Text(f"Line {i}"),
        )
    page.add(lv)


def bad_idea_grid(page: ft.Page):
    r = ft.Row(
        wrap=True,
        scroll="always",
        expand=True,
    )
    page.add(r)

    for i in range(5000):
        r.controls.append(
            ft.Container(
                content=ft.Text(f"Item {i}", color=ft.colors.BLACK),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(color=ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()


def grid_view(page: ft.Page):
    gv = ft.GridView(
        expand=True,
        max_extent=150,
        child_aspect_ratio=1,
    )
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}", color=ft.colors.BLACK),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
        page.update()

def list_view_batch(page: ft.Page):
    lv = ft.ListView(
        expand=True,
        spacing=10,
    )
    page.add(lv)
    for i in range(5100):
        lv.controls.append(
            ft.Text(f"Line {i}"),
        )
        if i % 500 == 0:
            page.update()
    page.update()


ft.app(target=list_view_batch, view=ft.AppView.WEB_BROWSER)
