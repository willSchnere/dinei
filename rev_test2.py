from atv_revisão2 import *

def test_acordada_cedo():
    assert acordar_cedo(7) == 'Tente novamente amanhã'
    assert acordar_cedo(5) == 'Você é um guerreiro'
def test_temp_exer():
    assert tempo_exercicio (5,4) ==  4
    assert tempo_exercicio (4,0) == None
def test_exer():
    assert tem_exercicio ('Descanso') == False
    assert tem_exercicio ('Futebol') == True
       
