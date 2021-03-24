from Business.studenti_servicii import ServiceStudenti
from Domeniu.student_entitati import Student
from Infrastructura.studenti_repository import RepositoryStudenti
from Validare.student_validare import Validare_Student
from Erori.exceptii import ValidError, RepoError


class Teste_Student(object):

    def __ruleaza_teste_domeniu(self):
        studID = 2
        nume = "Alin"
        grup = 222
        student = Student(studID, nume, grup)
        assert student.get_stud_id() == studID
        assert student.get_nume() == nume
        assert student.get_grup() == grup
        assert str(student) == "2 : Alin : 222"
        alt_student = Student(studID, None, None)
        assert student == alt_student

    def __ruleaza_teste_validare(self):
        studID = -2
        nume = ""
        grup = 223
        student = Student(studID, nume, grup)
        valid = Validare_Student()
        try:
            valid.valideaza(student)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID-ul nu poate fi un numar negativ!\nNumele nu poate fi gol!\n"

    def __ruleaza_teste_repo(self):
        # adauga
        repo = RepositoryStudenti()
        assert repo.size() == 0
        studID = 2
        nume = "Alina"
        grup = 13
        student = Student(studID, nume, grup)
        repo.adauga(student)
        assert repo.size() == 1

        # get all
        all_stud = repo.get_all()
        assert len(all_stud) == 1

        # cautare
        key_persoana = Student(studID, None, None)
        gasit = repo.cauta(key_persoana)
        try:
            repo.adauga(key_persoana)
            assert False
        except RepoError as re:
            assert str(re) == "Element existent!\n"
        assert gasit.get_nume() == nume
        key_persoana_nu = Student(24, None, None)
        try:
            repo.cauta(key_persoana_nu)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"

        # modificare
        student_nou = Student(2, "Mihai", "241")
        repo.modifica(student_nou)
        gasit = repo.cauta(key_persoana)
        assert gasit.get_grup() == "241"
        try:
            repo.modifica(key_persoana_nu)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"

            # stergere si size
            repo.sterge(key_persoana)
            assert repo.size() == 0
            try:
                repo.sterge(key_persoana)
                assert False
            except RepoError as re:
                assert str(re) == "Element inexistent!\n"

    def __ruleaza_teste_serviciu_gaseste_stud_by_ID(self):
        repo = RepositoryStudenti()
        valid = Validare_Student()
        srv = ServiceStudenti(repo, valid)
        studID = 2
        nume = "Alina"
        grup = "233"
        student = Student(studID, nume, grup)
        repo.adauga(student)
        assert repo.size() == 1
        gasit = srv.gaseste_stud_by_ID(studID)
        assert gasit.get_nume() == "Alina"
        assert gasit.get_grup() == "233"
        try:
            srv.gaseste_stud_by_ID(3)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"


    def __ruleaza_teste_serviciu_modificare(self):
        repo = RepositoryStudenti()
        valid = Validare_Student()
        srv = ServiceStudenti(repo, valid)
        studID = 2
        nume = "Alina"
        grup = "313"
        student = Student(studID, nume, grup)
        repo.adauga(student)
        assert repo.size() == 1
        nume_nou = "Catalina"
        grup_nou = "314"
        srv.modifica_stud(studID, nume_nou, grup_nou)
        key_persoana = Student(studID, None, None)
        gasit = repo.cauta(key_persoana)
        assert gasit.get_nume() == "Catalina"
        assert gasit.get_grup() == "314"
        try:
            srv.modifica_stud(3, nume_nou, grup_nou)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"


    def __ruleaza_teste_serviciu_sterge(self):
        repo = RepositoryStudenti()
        valid = Validare_Student()
        srv = ServiceStudenti(repo, valid)
        studID = 2
        nume = "Alina"
        grup = "313"
        srv.adauga_student(studID, nume, grup)
        assert srv.numar_studenti() == 1
        srv.adauga_student(3, "Raluca", "314")
        assert srv.numar_studenti() == 2
        srv.sterge_stud(studID)
        assert srv.numar_studenti() == 1
        try:
            srv.sterge_stud(2)
            assert False
        except RepoError as re:
            assert str(re) == "Element inexistent!\n"

    def ruleaza_teste(self):
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_validare()
        self.__ruleaza_teste_repo()
        self.__ruleaza_teste_serviciu_gaseste_stud_by_ID()
        self.__ruleaza_teste_serviciu_modificare()
        self.__ruleaza_teste_serviciu_sterge()
