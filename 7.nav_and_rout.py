import flet as ft


def page_route(page: ft.Page):
    page.add(
        ft.Text(f"Initial route: {page.route}"),
    )

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    def go_store(e):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change
    page.add(
        ft.ElevatedButton(
            text="Go to store",
            on_click=go_store,
        )
    )


def views(page: ft.Page):
    page.title = "Routes Example"

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.AppBar(
                        title=ft.Text(
                            "Flet app",
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        )
                    ),
                    ft.ElevatedButton(
                        text="Visit Store", on_click=lambda _: page.go("/store")
                    ),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    route="/store",
                    controls=[
                        ft.AppBar(
                            title=ft.Text(
                                "Store",
                                bgcolor=ft.colors.SURFACE_VARIANT,
                            ),
                        ),
                        ft.ElevatedButton(
                            text="Go Home", on_click=lambda _: page.go("/")
                        ),
                    ],
                )
            )
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=views, view=ft.AppView.WEB_BROWSER)
