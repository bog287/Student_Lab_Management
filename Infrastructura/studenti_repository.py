from Erori.exceptii import RepoError


class RepositoryStudenti(object):
    """
    Stocheaza studentii in memorie
    """

    def __init__(self):
        """
        Initializeaza lista in care vor fi stocati studentii si lista de clone pentru undo
        """
        self.__elems = []
        self.__clona = []

    def size(self):
        """
        Returneaza numarul de studenti
        :return: integer (numar studenti)
        """
        return len(self.__elems)

    def adauga(self, student):
        """
        Adauga un student in memorie
        :param: student - Student
        :exception: RepoError: un student cu acelasi ID exista deja
        """
        if student in self.__elems:
            raise RepoError("Element existent!\n")
        self.__elems.append(student)

    def get_all(self):
        """
        Returneaza lista cu toti studentii
        :return: list (lista studenti)
        """
        return self.__elems[:]

    def cauta(self, key_persoana):
        """
        Cauta un element in functie de o cheie specificata
        :param: key_persoana - string
        :exception: RepoError: Nu exista niciun element cu cheia data
        :return: list (elementul cautat)
        """
        if key_persoana not in self.__elems:
            raise RepoError("Element inexistent!\n")
        for elem in self.__elems:
            if elem == key_persoana:
                return elem

    def modifica(self, student_nou):
        """
        Modifica un student
        :param student_nou - Student
        :exception: RepoError: Nu exista niciun element cu ID-ul dat
        """
        if student_nou not in self.__elems:
            raise RepoError("Element inexistent!\n")
        for i in range(len(self.__elems)):
            if self.__elems[i] == student_nou:
                self.__elems[i] = student_nou
                return

    def sterge(self, key_persoana):
        """
        Sterge un student
        :param: key_student - string
        :exception: RepoError: Nu exista niciun element cu ID-ul dat
        """
        if key_persoana not in self.__elems:
            raise RepoError("Element inexistent!\n")
        for i in range(len(self.__elems)):
            if self.__elems[i] == key_persoana:
                del self.__elems[i]
                return

    def adauga_clona(self, lista_stud):
        """
        Adauga o clona a unei liste in memorie
        :param: lista_stud - lista de studenti curenta
        """
        self.__clona.append(lista_stud)

    def size_clona(self):
        """
        Returneaza numarul de liste clonate in clona
        :return: integer (numar liste clonate)
        """
        return len(self.__clona)

    def get_clona(self):
        """
        Modifica lista de studenti aducand-o la forma anterioara ultimei modificari si o returneaza
        :return: list (lista studenti)
        """
        self.__elems = self.__clona.pop()
        return self.__elems
