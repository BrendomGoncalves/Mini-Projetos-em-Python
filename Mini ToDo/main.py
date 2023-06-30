import flet as ft

class Task(ft.UserControl):
    def __init__(self, input_text, remove_task):
        super().__init__()
        self.input = input_text
        self.remove_task = remove_task

    def build(self):
        self.task_cb = ft.Checkbox(label=self.input, expand=True, fill_color=ft.colors.YELLOW_500)
        self.edit_tf = ft.TextField(value=self.input, expand=True, color=ft.colors.YELLOW_500, border_color=ft.colors.YELLOW_500)
        self.task_view = ft.Row(
            visible=True,
            controls=[
                self.task_cb,
                ft.IconButton(icon=ft.icons.CREATE_OUTLINED, on_click=self.edit_clicked, icon_color=ft.colors.YELLOW_500),
                ft.IconButton(icon=ft.icons.DELETE_OUTLINE, on_click=self.remove_clicked, icon_color=ft.colors.YELLOW_500)
            ]
        )
        self.edit_view = ft.Row(
            visible=False,
            controls=[
                self.edit_tf,
                ft.IconButton(icon=ft.icons.CHECK, on_click=self.save_clicked, icon_color=ft.colors.YELLOW_500)
            ]
        )
        return ft.Column(controls=[self.task_view, self.edit_view])
    
    def edit_clicked(self, e):
        self.task_view.visible = False
        self.edit_view.visible = True
        self.update()

    def remove_clicked(self, e):
        self.remove_task(self)

    def save_clicked(self, e):
        self.task_cb.label = self.edit_tf.value
        self.task_view.visible = True
        self.edit_view.visible = False
        self.update()

class ToDo(ft.UserControl):
    def build(self):
        self.input = ft.TextField(hint_text="O que deseja deixar de lembrete?", expand=True, color=ft.colors.WHITE)
        self.tasks = ft.Column()

        view = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='Seus ToDo\'s',
                        style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.colors.YELLOW_500),
                ft.Row(
                    controls=[
                        self.input,
                        ft.FloatingActionButton(icon=ft.icons.ADD_ROUNDED, on_click=self.add_clicker, bgcolor=ft.colors.YELLOW_500)
                    ]
                ),
                self.tasks
            ]
        )
        return view

    def add_clicker(self, e):
        if self.input.value != '':
            task = Task(self.input.value, self.remove_task)
            self.tasks.controls.append(task)
            self.input.value = ''
            self.update()
        else:
            pass
    
    def remove_task(self, task):
        self.tasks.controls.remove(task)
        self.update()

def main(page: ft.Page):
    page.window_height = 600
    page.window_width = 400
    page.bgcolor = ft.colors.SHADOW

    page.title = 'ToDo'

    todo = ToDo()
    page.add(todo)

ft.app(target=main)