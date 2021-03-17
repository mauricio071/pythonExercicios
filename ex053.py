f = input('Digite uma frase: ').strip()
pa = f.split()
junto = ''.join(pa)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
   inverso += junto[letra]

if junto.upper() == inverso.upper():
   print(junto, inverso)
   print('Palíndromo')
else:
   print(junto, inverso)
   print('Não é palindromo')

