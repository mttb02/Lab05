import database.corso_DAO
from database import corso_DAO
from database import studente_DAO


class Model:

    def get_corsi(self):
        return corso_DAO.get_corsi()

    def get_studenti(self):
        return studente_DAO.get_studenti()

    def get_studenti_corso(self, codcorso):
        return studente_DAO.get_studenti_corso(codcorso)

    def get_studente(self, matricola):
        return studente_DAO.get_studente(matricola)

    def get_corsi_studente(self, matricola):
        return corso_DAO.get_corsi_studente(matricola)

    def iscrivi_studente_corso(self, matricola, codcorso):
        return corso_DAO.iscrivi_studente_corso(matricola, codcorso)
