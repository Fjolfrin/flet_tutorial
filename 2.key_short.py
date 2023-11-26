import flet as ft


def main(page: ft.Page):  # Experimenting with keyboard shortcuts.
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Q" and e.shift and e.ctrl:
            page.window_destroy()
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Press any key with a combination of CTR, ALT, SHIFT and META keys...")
    )


ft.app(target=main)
