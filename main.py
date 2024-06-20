import curses
from curses import wrapper

class Wpm:
    # função que vai inicializar a frase para aparecer no terminal e os caracteres que o usuário vai digitar e o contador.
    def __init__(self,contador:int, sentenca:str, palavras:list) -> None:
        self.contador = contador
        self.sentenca = sentenca
        self.palavras = palavras
        
        #método with open para manipular arquivos em python, ele vai passar a frase para a variável sentença
        with open('sentenca.txt','r') as sentencas:
            self.sentenca = sentencas.read()

        #mesmo método, porém, ao invés de pegar a frase, vai dividir os caracteres e ordena-los em uma lista
        with open('sentenca.txt','r') as letra:
            self.palavras = letra.read().strip()
            
            self.palavras = list(self.palavras.replace('\n',''))
    
    #função que vai gerar os elementos no terminal(cores,frase e contador) e habilitar algumas funcionalidades
    def terminal(self,stdscr,cor= False,cor2=False)->str:
        self.cor = cor
        self.cor2 = cor2
        self.stdscr= stdscr
        
        #definindo as cores que usarei para corrigir, sendo identificada por um id como pode ver.
        curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.cor = curses.color_pair(1)

        curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
        self.cor2 = curses.color_pair(2)
        
        #adicionando uma string no terminal(sentença)
        self.stdscr.addstr(0,0,f'{self.sentenca}')

        self.main()
    
    def tempo(self) -> int:
            self.contador+=1
            self.stdscr.addstr(4,1, f'CHARS/MIN:{self.contador}')
    
    # função de busca utilizando o algoritmo de busca sequencial para verificar os elementos digitados e corriji-los
    def busca(self,erros:int,digitou:list, posicao:int,caracteres:list,escreveu:str,altura:int, largura:int) -> str:
        self.posicao = posicao
        self.caracteres = caracteres
        self.digitou=digitou
        self.erros=erros
        self.quebra_linha=0

        self.escreveu= escreveu
        self.altura= altura
        self.largura = largura
         
        while self.posicao < len(self.caracteres):
            self.botao = self.stdscr.getkey()
            
            if self.botao:
                   self.digitou.append(self.botao)
                   self.decidir_cor = self.cor if self.caracteres[self.posicao] == self.digitou[self.posicao] else self.cor2
                   
                   self.erros+=1 if self.digitou[self.posicao] != self.caracteres[self.posicao] else erros
            
                   self.escreveu = self.sentenca.replace(self.sentenca,self.botao)
                   self.stdscr.addstr(self.largura, self.altura, self.escreveu, self.decidir_cor)
                   self.altura+=1

                   self.tempo()
                   self.stdscr.refresh()
              
            if self.botao == '\n':
                   self.digitou.pop()
                   self.digitou.append(self.botao)
                   
                   self.largura+=1
                   self.altura=0
                   self.stdscr.refresh()

            self.posicao+=1
        self.quebra_linha=[c for c in self.digitou if "\n" in c]      
        
    #função que vai calcular a precisão apenas
    def media(self,verificar:int,total_digitado:int,resultado:int,acertos:list,tirar:int) -> int:
        self.verificar = verificar- tirar
        self.total_digitado = total_digitado
        self.acertos=acertos
        self.acertos=self.total_digitado-self.verificar

        self.resultado = resultado
        self.resultado=float(self.acertos/self.total_digitado)*100
        
        print(f'precisao:{(self.resultado):.2f}%')

    def main(self)-> None:
         if __name__ == "__main__":
            self.busca(erros=0,digitou=[], posicao=0, caracteres=self.palavras,escreveu='',altura=0,largura=0)

#tratamento de erro, caso o usuário queira interromper o programa com ctrl+c
try:
    words = Wpm(0,'',[])
    wrapper(words.terminal)
    words.media(verificar=words.erros, total_digitado=len(words.caracteres), resultado=0,acertos=0,tirar=len(words.quebra_linha))

except:
    print('programa interrompido')