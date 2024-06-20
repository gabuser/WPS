# WPS simples
WPS(word per second) era para ser um WPM, entretanto, o WPM utiliza um temporizador que calcula sua precisão com base em um tempo em que você
consegue digitar. eu fiz algo parecido, porém, eu não utilizei um temporaziador, ao invés, foi utilizado apenas a precisão que
vai calcular com base na quantidade de erros em que o usuário conseguiu digitar toda a sentença proposta, quanto maior os erros, menor será sua precisão, quanto menor o erro, maior será sua precisão.

### objetivos do projeto
````
aprender como funciona algoritmo de busca sequencial

por mais que não tenha sido usado, multhreading e seus conceitos(eventos, I/o bound e concorrência)

aprender a lib curses do python

aumentar o repertório na base computacional
````

### instalação
>git clone esse repostório

#### versão recomendada
`python3 e suas versões mais novas(recomendado)`

#### dependências necessárias
>unix-like é instalado por padrão.

>caso não seja instalado:

##### ubuntu/debian/derivados

> sudo apt-get update

>sudo apt-get install libncurses5-dev libncursesw5-dev

##### fedora
> sudo dnf install ncurses-devel

##### arch linux
>sudo pacman -S ncurses

##### openSUSE
>sudo zypper install ncurses-devel
-----
##### windows
> pip install windows-curses

#### rodando o script
para rodar o script em sua máquina, é necessário ser pelo terminal.

>python3 main.py

> cd local onde você copiou o repositório
---
# avisos importantes
>você pode colocar qualquer frase dentro do arquivo.txt(sentenca.txt), mas, siga o mesmo formato de quebra de linha no exemplo de sentenca.txt. caso não coloque, a busca resposável pela correção pode sofrer atrasos :(

>escolha se você irá executar o arquivo em tela grande ou tela mínima em seu terminal ou pormpt de comando, caso contrário, ele bulga o programa.

> se você errar alguma frase, continue escrevendo, não tente apagar, pois, eu não implementei essa função.

> para pular de linha é so apertar enter

>mantenha esses arquivos tudo junto(main.py e sentenca.txt)

>para interromper o programa, voce pode finalizar a sentença ou apertar ctrl+c

##### referências:
[algoritmos busca sequencial](https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/BuscaSequencial.html)

[curses](https://youtu.be/Db4oc8qc9RU?si=8mf0lE2KZ11FLUMi)

[curses pt2](https://docs.python.org/3/library/curses.html)

obrigado por ler até aqui e tirar tempo para testar. esse projeto pode sofrer mudanças no futuro ao decorrer do tempo de aprendizado adquirido. 