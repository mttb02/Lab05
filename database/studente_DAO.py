# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


def get_studenti() -> list[Studente] | None:
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente")
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def get_studenti_corso(codcorso) -> list[Studente] | None:
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT studente.matricola, nome, cognome, CDS FROM iscrizione JOIN studente on iscrizione.matricola = studente.matricola 
                WHERE codins = %s"""
        cursor.execute(query, (codcorso,))
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
            print(row)
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def get_studente(matricola) -> Studente | None:
    cnx = get_connection()
    print(matricola)
    result = None
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM studente WHERE matricola = %s"
        cursor.execute(query, (str(matricola),))
        for row in cursor:
            result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None