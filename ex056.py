soma = 0
med = 0
maior = 0
velho = ''
mn = 0
for c in range(1, 5):
    print(f'========== Pessoa {c} ============')
    nome = input('Digite o seu nome: ').strip()
    idade = int(input('Digite a sua idade: ')).strip()
    sexo = input('Digite o seu sexo M/F: ').strip()
    if sexo in 'Mm':
        if idade > maior:
            maior = idade
            velho = nome
    elif sexo in 'Ff':
        if idade < 20:
            mn += 1
    soma += idade
med = soma / 4
print(f'''\nA média de idade do grupo é {med}
      \nO homem mais velho é {velho}
      \nTêm {mn} mulheres com menos de 20 anos''')