# criando variáveis para o jogo
jogador1 = int(input('informe um numero: '))
jogador2 = int(input('informe um numero: '))

# operadores matemáticos
# somar + ex: 1+1 = 2
# incrementar += ex: idade += 1
# subtração -  ex: 3-2 = 1
# decremento -=  ex: idade -= 1
# multiplicação *
# divisão /  ex: 3/2 = 1.5
# módulo %   ex: 3%2 = 1 (traz o resto)

numero = jogador1 + jogador2

# lógica - if e else

if numero % 2 != 0:
    print('impar ganhou')

else:
    print('par ganhou')