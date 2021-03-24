from Erori.exceptii import ValidError

class Validare_Student(object):


    def __init__(self):
        pass

    def valideaza(self, stud):
        """
        Valideaza Student
        :param: stud - object
        """
        erori = ""
        if stud.get_stud_id() == "":
            erori += "ID-ul nu poate fi gol!\n"
        try:
            if stud.get_stud_id() < 0:
                erori += "ID-ul nu poate fi un numar negativ!\n"
        except Exception:
            erori += "ID-ul trebuie sa fie un numar natural!\n"
        if stud.get_nume() == "":
            erori += "Numele nu poate fi gol!\n"
        if stud.get_grup() == "":
            erori += "Grupul nu poate fi gol!\n"

        if len(erori) > 0:
            raise ValidError(erori)