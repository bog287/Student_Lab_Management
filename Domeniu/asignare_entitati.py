class Asignare(object):
    def __init__(self, asignare_ID, stud_ID, nrLab_nrPb, nota):
        """
        Creare Asignare
        :param asignare_ID: numar natural(identificatorul unic al unei inscrieri)
        :param stud_ID: numar natural (identificatorul unic al unui student)
        :param nrLab_nrPb: string (identificatorul unic al unei probleme)
        :param nota: numar natural (nota primita de un student la un laborator)
        """
        self.__asignare_ID = asignare_ID
        self.__stud_ID = stud_ID
        self.__nrLab_nrPb = nrLab_nrPb
        self.__nota = nota

    def get_asignare_ID(self):
        """
        Returneaza ID ul unei asignari
        :return: __asignare_ID - numar natural (identificatorul unic al unei asignari)
        """
        return self.__asignare_ID

    def get_stud_ID(self):
        """
        Returneaza ID ul unui student
        :return: __stud_ID - numar natural (identificatorul unic al unei persoane)
        """
        return self.__stud_ID

    def get_nrLab_nrPb(self):
        """
        Returneaza nrLab_nrPb ul unei probleme
        :return: __nrLab_nrPb - string (identificatorul unic al unei probleme)
        """
        return self.__nrLab_nrPb

    def get_nota(self):
        """
        Returneaza nota unui student
        :return: numar natural(mai mic sau egal cu 10)
        """
        return self.__nota

    def __eq__(self, asgn):
        """
        Verifica daca doua asignari au acelasi ID
        :param: asign - Asignare
        :return: bool (True daca asignarea curenta are acelasi ID cu asgn; False in caz contrar)
        """
        return self.__asignare_ID == asgn.__asignare_ID

    def __str__(self):
        """
        Converteste acest obiect in string
        :return: string (asignare_ID, stud_ID, nrLab_nrPb, nota)
        """
        return "          " + str(self.get_asignare_ID()) + "          " + str(self.get_stud_ID()) + "          " + str(
            self.get_nrLab_nrPb()) + "          " + str(self.get_nota())
