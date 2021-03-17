m = 0
me = 0
for c in range(1, 6):
    p = float(input(f'Digite o seu peso nº {c}: '))
    if c == 1:
        m = p
        me = p
    else:
        if p > m:
            m = p
        if p < me:
            me = p
print(f'O maior peso foi de {m}\nO menor peso foi de {me}')