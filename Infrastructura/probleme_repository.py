from Erori.exceptii import RepoError


class RepositoryProbleme(object):
    """
    Stocheaza problemele in memorie
    """

    def __init__(self):
        """
        Initializeaza lista in care vor fi stocate problemele si lista de clona pentru undo
        """
        self.__elems = []
        self.__clona = []

    def size(self):
        """
        Returneaza numarul de probleme
        :return: integer (numar probleme)
        """
        return len(self.__elems)

    def adauga(self, problema):
        """
        Adauga o problema in memorie
        :param: problema - Problema
        :exception: RepoError: O problema cu acelasi ID exista deja
        """
        if problema in self.__elems:
            raise RepoError("Problema existenta!\n")
        self.__elems.append(problema)

    def cauta(self, key_pb):
        """
        Cauta un element in functie de o cheie specificata
        :param: key_pb - string
        :exception: RepoError: Nu exista niciun element cu cheia data
        :return: list (elementul cautat)
        """
        if key_pb not in self.__elems:
            raise RepoError("Element inexistent!\n")
        for elem in self.__elems:
            if elem == key_pb:
                return elem

    def modifica(self, pb_noua):
        """
        Modifica o pb
        :param pb_noua - Problema
        :exception: RepoError: Nu exista niciun element cu nrLab_nrPb-ul dat
        """
        if pb_noua not in self.__elems:
            raise RepoError("Element inexistent!\n")
        for i in range(len(self.__elems)):
            if self.__elems[i] == pb_noua:
                self.__elems[i] = pb_noua
                return


    def sterge(self, key_pb):
        """
        Sterge o pb
        :param: key_pb - string
        :exception: RepoError: Nu exista niciun element cu ID-ul dat
        """
        if key_pb not in self.__elems:
            raise RepoError("Element inexistent!\n")
        for i in range(len(self.__elems)):
            if self.__elems[i] == key_pb:
                del self.__elems[i]
                return


    def get_all(self):
        """
        Returneaza lista cu toate problemele
        :return: list (lista probleme)
        """
        return self.__elems[:]
