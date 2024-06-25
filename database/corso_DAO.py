# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


def get_corsi() -> list[Corso] | None:
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM corso")
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def get_corsi_studente(matricola) -> list[Corso] | None:
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = ("SELECT corso.codins, crediti, nome, pd FROM iscrizione JOIN corso WHERE iscrizione.codins = corso.codins AND matricola = %s")
        cursor.execute(query, (str(matricola),))
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def iscrivi_studente_corso(matricola, codcorso) -> bool:
    cnx = get_connection()
    result = []
    query = """INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
        (`matricola`, `codins`) 
        VALUES(%s,%s)
        """
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute(query, (matricola, codcorso,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    else:
        print("Could not connect")
        return False
