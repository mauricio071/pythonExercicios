p = float(input('Digite o valor do produto: '))
op = input('Condição de pagamento: \n- À vista \033[1;34mdinheiro/cheque\033[m: 10% de desconto \n- À vista no \033[1;34mcartão\033[m: 5% de desconto '
           '\n- Em até \033[1;34m2x no cartão\033[m: preço normal \n- \033[1;34m3x ou mais\033[m no cartão: 20% de juros')

if op == 'dinheiro' or op == 'cheque':
    print(f'R$ {p * 0.90:.2f}')
elif op == 'cartão':
    print(f'R$ {p * 0.95:.2f}')
elif op == '2x no cartão':
    print(f'2x de R$ {p / 2:.2f}')
elif op == '3x ou mais':
    m = int(input('Em quantas vezes? '))
    print(f'3x ou mais de R$ {(p / m) * 1.20:.2f}')
else:
    print('Opção inválida')
