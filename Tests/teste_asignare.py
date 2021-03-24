from Business.asignare_servicii import ServiceAsignare
from Domeniu.asignare_entitati import Asignare
from Domeniu.problema_entitati import Problema
from Domeniu.student_entitati import Student
from Erori.exceptii import ValidError, RepoError
from Infrastructura.asignare_repository import RepositoryAsignare
from Infrastructura.probleme_repository import RepositoryProbleme
from Infrastructura.studenti_repository import RepositoryStudenti
from Validare.asignare_validare import Validare_Asignare


class Teste_Asignare(object):

    def __ruleaza_teste_domeniu(self):
        asignare_ID = 1
        stud_ID = 2
        nrLab_nrPb = "3_21"
        nota = 8
        asignare = Asignare(asignare_ID, stud_ID, nrLab_nrPb, nota)
        assert asignare.get_asignare_ID() == asignare_ID
        assert asignare.get_stud_ID() == stud_ID
        assert asignare.get_nrLab_nrPb() == nrLab_nrPb
        assert asignare.get_nota() == nota
        assert str(asignare) == "          1          2          3_21          8"
        alt_asign = Asignare(asignare_ID, None, None, None)
        assert asignare == alt_asign

    def __ruleaza_teste_validare(self):
        asignare_ID = ""
        stud_ID = -1
        nrLab_nrPb = ""
        nota = 11
        asign = Asignare(asignare_ID, stud_ID, nrLab_nrPb,nota)
        valid = Validare_Asignare()
        try:
            valid.valideaza(asign)
            assert False
        except ValidError as ve:
            assert str(
                ve) == "ID-ul asign nu poate fi gol!\nID-ul asign trebuie sa fie un numar natural!\nID-ul unei persoane nu poate fi un numar negativ!\nID-ul unei probleme nu poate fi gol!\nnota nu poate fi un numar negativ si nu poate fi mai mare ca 10!\n"


    def __ruleaza_teste_repo(self):
        #adauga
        repo = RepositoryAsignare()
        assert repo.size() == 0
        asignare_ID = 1
        stud_ID = 2
        nrLab_nrPb = "2_23"
        nota = 9
        asignare = Asignare(asignare_ID, stud_ID, nrLab_nrPb,nota)
        repo.adauga(asignare)
        assert repo.size() == 1

        # get all
        all = repo.get_all()
        assert len(all) == 1
        assert all[0].get_nrLab_nrPb() == "2_23"


    def __ruleaza_teste_serviciu_adaugare(self):
        repo_asignare = RepositoryAsignare()
        repo_stud = RepositoryStudenti()
        repo_prob = RepositoryProbleme()
        valid = Validare_Asignare()
        srv = ServiceAsignare(repo_asignare, repo_stud, repo_prob, valid)
        student = Student(5, "Alina", "236")
        repo_stud.adauga(student)
        prob = Problema("4_18", "cam urata problema", 8)
        repo_prob.adauga(prob)
        asign_ID = 28
        stud_ID = 5
        nrLab_nrPb = "4_18"
        nota = 7
        srv.adauga_asignare(asign_ID, stud_ID, nrLab_nrPb, nota)
        assert srv.numar_asignare() == 1
        try:
            srv.adauga_asignare(-asign_ID, stud_ID, nrLab_nrPb,nota)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID-ul asign nu poate fi un numar negativ!\n"
        try:
            srv.adauga_asignare(asign_ID, 5, "4_18", 8)
            assert False
        except RepoError as re:
            assert str(re) == "Element existent!\n"
        assert len(srv.get_asignare()) == 1
        try:
            srv.adauga_asignare(4, 5, "9_12", 8)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"
        try:
            srv.adauga_asignare(4, 3, "9_12", 7)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"


    def ruleaza_teste(self):
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_repo()
        self.__ruleaza_teste_serviciu_adaugare()
