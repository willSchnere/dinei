from atv_revisão import *

def test_ver_email():
    assert email_valido("email@verdadeiro.com") == True
    assert email_valido("email@falsidade") == False
def test_num_par():
    assert eh_par (4) == True
    assert eh_par (3) == False    
def test_fatorial():
    assert fatorial (5) == 120
    assert fatorial (0) == 1
def test_quadrado():
    assert quadrado (2) == 4
    assert quadrado (3) == 9
def test_eh_positivo():
    assert eh_positivo (1) == True
    assert eh_positivo (-5) == False
def test_verifica_idade():
    assert verificar_maioridade (25) == 'maior de idade'
    assert verificar_maioridade (10) == 'menor de idade'
def test_verifica_temp():
    assert classificar_temperatura (-50) == 'frio'
    assert classificar_temperatura (20) == 'moderado'
    assert classificar_temperatura (40) == 'quente'
def test_nota():
    assert avaliar_nota (8) == 'aprovado'
    assert avaliar_nota (6) == 'recuperacao'
    assert avaliar_nota (2) == 'reprovado'
def test_votar():
    assert pode_votar (19) == 'voto obrigatório'
    assert pode_votar (16) == 'voto facultativo'
    assert pode_votar (14) == 'não pode votar'
def test_avaliar_produto():
    assert avaliar_produto (5) == 'excelente'
    assert avaliar_produto (4) == 'bom'
    assert avaliar_produto (3) == 'regular'
    assert avaliar_produto (2) == 'ruim'
    assert avaliar_produto (1) == 'péssimo'
    assert avaliar_produto (0) == 'valor inválido'    

