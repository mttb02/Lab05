import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_corso = None
        self.btn_cerca_iscritti = None
        self.tf_matricola = None
        self.tf_nome = None
        self.tf_cognome = None
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None
        self.btn_iscrivi = None
        self.txt_result = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)     #MODIFICATA DA self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(self._title)

        #Row1
        self.dd_corso = ft.Dropdown(label="corso", expand=True, hint_text="Selezionare un corso", options=[], autofocus=True)
        self._controller.populate_dd_corso()
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_cerca_iscritti, tooltip="cerca gli iscritti al corso selezionato")
        row1 = ft.Row([self.dd_corso, self.btn_cerca_iscritti], alignment=ft.MainAxisAlignment.CENTER)

        #Row2
        self.tf_matricola = ft.TextField(label="matricola", width=150, hint_text="Inserire matricola")
        self.tf_nome = ft.TextField(label="nome", read_only=True)
        self.tf_cognome = ft.TextField(label="cognome", read_only=True)
        row2 = ft.Row([self.tf_matricola, self.tf_nome, self.tf_cognome], alignment=ft.MainAxisAlignment.CENTER)

        #Row3
        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_cerca_studente, tooltip="Verifica se c'è uno studente con la matricola specificata")
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_cerca_corsi, tooltip="cerca i corsi a cui è iscritto lo studente con la matricola specificata")
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_cerca_studente, tooltip="iscritto al corso selezionato lo studente con la matricola specificata")
        row3 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi], alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._page.update()

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
