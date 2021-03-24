class Student(object):
    def __init__(self, studID, nume, grup):
        """
        Creare Student
        :param studID: nr natural pozitiv (identificatorul unic al unui student)
        :param nume: string (nume Student)
        :param grup: string (grup Student)
        """
        self.__studID = studID
        self.__nume = nume
        self.__grup = grup

    def get_stud_id(self):
        """
        Returneaza ID ul unui student
        :param: -
        :return: __studID - nr natural pozitiv (identificatorul unic al unui student)
        """
        return self.__studID

    def get_nume(self):
        """
        Returneaza numele unui student
        :param: -
        :return: __nume - string (nume Student)
        """
        return self.__nume

    def get_grup(self):
        """
        Returneaza grupul unui student
        :param: -
        :return: __grup - string (grup Student)
        """
        return self.__grup

    def set_nume(self, val):
        """
        Seteaza numele unui student
        :param: value - string (nume student)
        """
        self.__nume = val

    def set_grup(self, val):
        """
        Seteaza grupul unui student
        :param: val - string (grup student)
        """
        self.__grup = val

    def __str__(self):
        """
        Converteste acest obiect in string
        :return: string (studID, nume, grup)
        """
        return str(self.__studID) + " : " + self.__nume + " : " + str(self.__grup)

    def __eq__(self, stud):
        """
        Verifica daca doi studenti au acelasi ID
        :param: pers - Student
        :return: bool (True daca student curent are acelasi ID cu stud; False in caz contrar)
        """

        return self.__studID == stud.__studID
