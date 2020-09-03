from app.funcionarios.fixos.programador import Programador
from app.funcionarios.fixos import Analista
from app.funcionarios.fixos import Programador

if __name__ == '__main__':
    programador = Programador()
    analista = Analista()

    print(programador, analista)
    print(analista.info())
