import flet as ft
from math import pi
import time

def opacity(page: ft.Page):
    c = ft.Container(
        height=300,
        width=300,
        bgcolor="blue",
        border_radius=10,
        animate_opacity=ft.Animation(
            duration=1000,
            curve=ft.AnimationCurve.EASE_IN_OUT_EXPO,
        ),
    )

    def animate_opacity(e):
        c.opacity = 0 if c.opacity == 1 else 1
        c.update()

    page.add(
        c,
        ft.ElevatedButton(
            text="Animate Opacity",
            on_click=animate_opacity,
        ),
    )


def roation(page: ft.Page):
    c = ft.Container(
        height=300,
        width=300,
        bgcolor="blue",
        border_radius=10,
        rotate=ft.transform.Rotate(
            angle=0,
            alignment=ft.alignment.center,
        ),
        animate_rotation=ft.Animation(
            duration=1000,
            curve=ft.AnimationCurve.EASE_IN_OUT_EXPO,
        ),
    )

    def animate_rotation(e):
        c.rotate.angle += pi / 2
        c.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(
        c,
        ft.ElevatedButton(
            text="Animate!",
            on_click=animate_rotation,
        ),
    )


def scale(page: ft.Page):
    c = ft.Container(
        height=300,
        width=300,
        bgcolor="blue",
        border_radius=10,
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.Animation(
            duration=1000,
            curve=ft.AnimationCurve.EASE_IN_OUT_EXPO,
        ),
    )

    def animate_scale(e):
        c.scale = 2 if c.scale == 1 else 1
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(
        c,
        ft.ElevatedButton(
            text="Animate!",
            on_click=animate_scale,
        ),
    )


def offset(page: ft.Page):
    c = ft.Container(
        height=300,
        width=300,
        bgcolor="blue",
        border_radius=10,
        offset=ft.transform.Offset(
            x=-2,
            y=0,
        ),
        animate_offset=ft.Animation(
            duration=1000,
            curve=ft.AnimationCurve.EASE_IN_OUT_EXPO,
        ),
    )

    def aniamte_offset(e):
        c.offset.x = 0 if c.offset.x == -2 else -2
        c.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30
    page.add(
        c,
        ft.ElevatedButton(
            text="Reveal!",
            on_click=aniamte_offset,
        ),
    )


def position(page: ft.Page):
    c1 = ft.Container(
        width=50,
        height=50,
        bgcolor="red",
        animate_position=ft.Animation(
            duration=1000,
            curve=ft.AnimationCurve.EASE_IN,
        ),
    )

    c2 = ft.Container(
        width=50,
        height=50,
        bgcolor="green",
        top=60,
        left=0,
        animate_position=ft.Animation(
            duration=500,
            curve=ft.AnimationCurve.ELASTIC_IN_OUT,
        ),
    )

    c3 = ft.Container(
        width=50,
        height=50,
        bgcolor="blue",
        top=120,
        left=0,
        animate_position=ft.Animation(
            duration=1500,
            curve=ft.AnimationCurve.BOUNCE_IN_OUT,
        ),
    )

    def animate_container(e):
        c1.top = 20
        c1.left = 200
        c2.top = 100
        c2.left = 40
        c3.top = 180
        c3.left = 100
        page.update()

    page.add(
        ft.Stack([c1, c2, c3], height=250),
        ft.ElevatedButton("Animate!", on_click=animate_container),
    )

def animate_container(page: ft.Page):

    c = ft.Container(
        width=150,
        height=150,
        bgcolor="red",
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
    )

    def animate(e):
        c.width = 100 if c.width == 150 else 150
        c.height = 50 if c.height == 150 else 150
        c.bgcolor = "blue" if c.bgcolor == "red" else "red"
        c.update()

    page.add(c, ft.ElevatedButton("Animate container", on_click=animate))


def switch(page: ft.Page):

    i = ft.Image(src="https://picsum.photos/150/150", width=150, height=150)

    def animate(e):
        sw.content = ft.Image(
            src=f"https://picsum.photos/150/150?{time.time()}", width=150, height=150
        )
        page.update()

    sw = ft.AnimatedSwitcher(
        i,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=500,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    page.add(
        sw,
        ft.ElevatedButton("Animate!", on_click=animate),
    )


ft.app(target=switch)
