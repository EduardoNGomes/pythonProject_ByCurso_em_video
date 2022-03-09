#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.


from itertools import count


times = ('Atletico-mg', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthias', 'Bragantino', 'Chapecoense', 'Fluminense', 'America-mg'
        , 'Altetico-go', 'Santos', 'Ceara Sc', 'Internacional', 'Sao paulo', 'Athletico-PR', 'Cuiaba', 'Juventude', 'Gremio', 'Bahia',
        'Sport Recife')

print(f'Os cinco primeiros times do campeonato sao {times[:5]}')
print('=='*20)
print(f'Os ultimos 4 colocados sao {times[-4:]}')
print('=='*20)
print(f'O nome dos times em ordem alfabetica: {sorted(times)}')
print('=='*20)
print('A posicao do Chapecoense {}'.format(times.index('Chapecoense')+1))

