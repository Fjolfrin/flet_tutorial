import flet as ft
from typing import Dict


def main(page: ft.Page):
    def on_dialog_result(e: ft.FilePickerResultEvent):
        print(f"Selected files: {e.files}")
        print(f"Selected file or directory: {e.path}")

    def upload_files(e: ft.FilePickerUploadEvent):
        upload_list = []
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                upload_list.append(
                    ft.FilePickerUploadFile(
                        name=f.name,
                        upload_url=page.get_upload_url(file_name=f.name, expires=600),
                    )
                )
            file_picker.upload(upload_list)

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    page.add(
        ft.ElevatedButton(
            text="Choose files...",
            on_click=lambda _: file_picker.pick_files(allow_multiple=True),
        ),
        ft.ElevatedButton(
            text="Upload",
            on_click=upload_files,
        ),
    )
    page.update()


def upload_with_progress(page: ft.Page):
    pbars: Dict[str, ft.ProgressRing] = {}
    files = ft.Ref[ft.Column]()
    upload_button = ft.Ref[ft.ElevatedButton]()

    def file_picker_result(e: ft.FilePickerResultEvent):
        upload_button.current.disabled = True if e.files is None else False
        pbars.clear()
        files.current.controls.clear()

        if e.files is not None:
            for f in e.files:
                prog = ft.ProgressRing(
                    value=0,
                    bgcolor="#eeeeee",
                    width=20,
                    height=20,
                )
                pbars[f.name] = prog
                files.current.controls.append(
                    ft.Row(
                        controls=[
                            prog,
                            ft.Text(value=f.name),
                        ],
                    ),
                )
        page.update()

    def on_upload_progress(e: ft.FilePickerUploadEvent):
        pbars[e.file_name].value = e.progress
        pbars[e.file_name].update()

    file_picker = ft.FilePicker(
        on_result=file_picker_result,
        on_upload=on_upload_progress,
    )

    def upload_files(e: ft.FilePickerUploadEvent):
        to_upload = []
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                to_upload.append(
                    ft.FilePickerUploadFile(
                        name=f.name,
                        upload_url=page.get_upload_url(
                            file_name=f.name,
                            expires=600,
                        ),
                    )
                )
            file_picker.upload(to_upload)

    page.overlay.append(file_picker)

    page.add(
        ft.ElevatedButton(
            text="Select Files...",
            icon=ft.icons.FOLDER_OPEN_ROUNDED,
            on_click=lambda _: file_picker.pick_files(allow_multiple=True),
        ),
        ft.Column(ref=files),
        ft.ElevatedButton(
            text="Upload",
            ref=upload_button,
            icon=ft.icons.UPLOAD_FILE_ROUNDED,
            on_click=upload_files,
            disabled=True,
        ),
    )


ft.app(
    target=upload_with_progress,
    view=ft.AppView.WEB_BROWSER,
    upload_dir="uploads",
    assets_dir="assets",
)
