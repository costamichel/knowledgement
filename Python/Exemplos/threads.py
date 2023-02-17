# Fonte: https://medeubranco.wordpress.com/2008/07/10/threads-em-python/
from threading import Thread
 
class minhaThread(Thread):
    # sobrescrevendo o método __init__()
    def __init__(self, meu_argumento):
        # o metodo __init__ da superclasse
        # deve ser chamado para proceder
        # com a inicialização
        Thread.__init__(self)
        self.atributo=meu_argumento
 
    # sobrescrevendo o metodo run()
    def run(self):
        #insira seu codigo aqui
        print(self.atributo)

thr = minhaThread( [1, 5, 9] )
thr.start()
