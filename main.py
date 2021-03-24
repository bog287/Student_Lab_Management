from Business.asignare_servicii import ServiceAsignare
from Business.probleme_servicii import ServiceProbleme
from Business.statistici_servicii import ServiceStatistici
from Infrastructura.asignare_repository import RepositoryAsignare
from Infrastructura.studenti_repository import RepositoryStudenti
from Tests.teste_asignare import Teste_Asignare
from Tests.teste_probleme import Teste_Problema
from Tests.teste_statistici import Teste_Statistici
from Tests.teste_student import Teste_Student
from Validare.asignare_validare import Validare_Asignare
from Validare.problema_validare import Validare_Problema
from Validare.student_validare import Validare_Student
from UI.consola import *
from Business.studenti_servicii import ServiceStudenti
from Infrastructura.probleme_repository import RepositoryProbleme

# Tests
teste_student = Teste_Student()
teste_student.ruleaza_teste()
teste_problema = Teste_Problema()
teste_problema.ruleaza_teste()
teste_asignare = Teste_Asignare()
teste_asignare.ruleaza_teste()
teste_statistici = Teste_Statistici()
teste_statistici.ruleaza_teste()

# Validators
valid_stud = Validare_Student()
valid_pb = Validare_Problema()
valid_asign = Validare_Asignare()


# Repositories
repo_stud = RepositoryStudenti()
repo_problema = RepositoryProbleme()
repo_asignare = RepositoryAsignare()

# Controllers
srv_stud = ServiceStudenti(repo_stud, valid_stud)
srv_pb = ServiceProbleme(repo_problema, valid_pb)
srv_asign = ServiceAsignare(repo_asignare,repo_stud, repo_problema, valid_asign)
srv_statistici = ServiceStatistici(repo_asignare, repo_stud, repo_problema)




# User Interface
cons = UI(srv_stud, srv_pb, srv_asign,srv_statistici)

cons.run()

