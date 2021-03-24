from Erori.exceptii import ValidError


class Validare_Asignare(object):

    def __init__(self):
        pass

    def valideaza(self, asignare):
        """
        Valideaza Asignarea
        :param: asign - object
        """
        erori = ""
        # Asignare ID
        if asignare.get_asignare_ID() == "":
            erori += "ID-ul asign nu poate fi gol!\n"
        try:
            if asignare.get_asignare_ID() < 0:
                erori += "ID-ul asign nu poate fi un numar negativ!\n"
        except Exception:
            erori += "ID-ul asign trebuie sa fie un numar natural!\n"
        # Person ID
        if asignare.get_stud_ID() == "":
            erori += "ID-ul unei persoane nu poate fi gol!\n"
        try:
            if asignare.get_stud_ID() < 0:
                erori += "ID-ul unei persoane nu poate fi un numar negativ!\n"
        except Exception:
            erori += "ID-ul unei persoane trebuie sa fie un numar natural!\n"
        # nrLab_nrPb
        if asignare.get_nrLab_nrPb() == "":
            erori += "ID-ul unei probleme nu poate fi gol!\n"
        # nota
        if asignare.get_nota() < 0 or asignare.get_nota() > 10:
            erori += "nota nu poate fi un numar negativ si nu poate fi mai mare ca 10!\n"

        if len(erori) > 0:
            raise ValidError(erori)
