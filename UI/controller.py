import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view

        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_cerca_iscritti(self, e):
        if self._view.dd_corso.value is None:
            self._view.create_alert("Selezionare un corso")
        else:
            stud = self._model.get_studenti_corso(self._view.dd_corso.value)
            self._view.txt_result.controls.append(ft.Text(f'Ci sono {len(stud)} iscritti al corso:'))
            for s in stud:
                self._view.txt_result.controls.append(ft.Text(s))
            self._view.update_page()

    def handle_cerca_studente(self, e):
        s = self._model.get_studente(self._view.tf_matricola.value)
        if s is None:
            self._view.create_alert("Inserire una matricola presente")
        else:
            self._view.tf_nome.value = s.nome
            self._view.tf_cognome.value = s.cognome
        self._view.update_page()
        return s

    def handle_cerca_corsi(self, e):
        if self.handle_cerca_studente(e) is not None:
            cors = self._model.get_corsi_studente(self._view.tf_matricola.value)
            self._view.txt_result.controls.append(ft.Text(f'Risultano {len(cors)} corsi:'))
            for c in cors:
                self._view.txt_result.controls.append(ft.Text(c))
            self._view.update_page()

    def handle_iscrivi(self, e):
        codcorso = self._view.dd_corso.value
        matricola = self._view.tf_matricola.value
        if (self.handle_cerca_studente(e) is not None) and (self._view.dd_corso.value is not None):
            self._model.iscrivi_studente_corso(matricola, codcorso)

    def populate_dd_corso(self):
        for c in self._model.get_corsi():
            self._view.dd_corso.options.append(ft.dropdown.Option(key=c.codins, text=c))
