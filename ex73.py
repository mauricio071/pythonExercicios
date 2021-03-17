time = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'Os 5 primeiros colocados: {time[:6]}')
print(f'Os 4 últimos colocados: {time[-4:]}')
print(f'Lista dos times em ordem alfabética: {sorted(time)}')
print(f'O time Chapecoense está na posição {time.index("Chapecoense") + 1}')
