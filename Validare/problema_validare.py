from Erori.exceptii import ValidError


class Validare_Problema(object):


    def __init__(self):
        pass

    def valideaza(self, problema):
        """
        Valideaza Problema
        :param: problema - object
        """
        erori = ""
        if problema.get_nrLab_nrPb() == "":
            erori += "ID-ul nu poate fi gol!\n"
        if problema.get_desc() == "":
            erori += "Descrierea nu poate fi goala!\n"
        if int(problema.get_deadline()) < 0:
            erori += "Deadline-ul nu poate fi un numar negativ!\n"
        if len(erori) > 0:
            raise ValidError(erori)





