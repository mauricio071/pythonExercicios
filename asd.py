class Arvore: #método construtor da árvore
    def _init_(self, chave = None, filho=[]):
        self.chave = chave
        self.filho  = filho

    def _repr_(self): #imprimir a arvore
        return '%s -> %s' %(self.chave, self.filho)

#raiz da Arvore
raiz = Arvore(9)

#filhos da Raiz
raiz.filho = [3,11,15]
print(f'Arvore: {raiz}')

#Filhos do 3
raiz.filho = Arvore(3)
raiz.filho.filho = [1,4,5]
print(f'Arvore: {raiz}')

#filhos do 4
raiz.filho.filho = Arvore(4)
raiz.filho.filho.filho = [20,22]
print(f'Arvore: {raiz}')

#Filhos do 22

raiz.filho.filho.filho = Arvore(22)
raiz.filho.filho.filho.filho = [30]
print(f'Arvore: {raiz}')