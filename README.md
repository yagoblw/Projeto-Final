## Projeto-Final
Projeto Final - Curso de Admissão - Módulo 2 - Jala University

## História:
-> Ao longo das etapas do processo seletivo para ganhar bolsa integral e online da Jala University, ao qual estou concorrendo, tive que realizar um projeto utilizando
a base do jogo DINO RUNNER, a partir da biblioteca PYGAME da Linguagem PYTHON e fazer adaptações e implementações de um jogo que, mesmo com a essência do DINO RUNNER, fosse mais diferente e dinâmico, ou seja, um jogo 2d tendo o propósito de ultrapassar todos obstáculos e alcançar a maior pontuação possível.

## Implementações:
-> As principais implementações que fiz no jogo, foram:
<ul>
	<li>A Pena : permite que possamos voar, apertando a tecla 'W' e parar de voar, a tecla 'Q', vale ressaltar que ao voar os obstáculos Cogumelo voador e Torpedo também seguem o Mário e para podermos voar mais alto, só apertar a tecla 'Space' e voar mais baixo, a tecla 'S';</li>
	<li>O Martelo : permite que possamos destruir os obstáculos dentro do tempo mostrado;</li>
	<li>As Vidas : permitem que ao colidirmos com os obstáculos, tenhamos novas chances ao decorrer do jogo;</li>
	<li>O Shield : permite que sejamos transformados no personagem Mecha Mario e ao colidirmos nos obstáculos não sejamos mortos pela poderosa armadura de metal do Mecha Mario;</li>
	<li>O Relógio : uma implementação rara dentro do jogo, que permite que a velocidade do jogo diminua e, consequentemente, a dificuldade do jogo também;</li>
</u>

## Controles

<p>
	SPACE  = Pular e voar mais alto
</p>
<p>
	S  = Agachar e voar mais baixo
</p>
<p>
	W  = Ativar o voo (com a pena)
</p>
<p>
	Q  = Desativar o voo (com a pena)
</p>


### Construído com:

- [ Python 3.11.3 ](https://www.python.org/downloads/release/python-3113/)
- [ Pygame 2.4.0](https://www.pygame.org/wiki/GettingStarted)
- [ OS ](https://python.readthedocs.io/en/stable/library/os.html)

#### Por que utilizei pygame como biblioteca:
- Maior quantidade de repositórios online, disponíveis para aprendizado.
- Facilidade na criação de molduras para a superfície do jogo, com posicionamento dos sprites através da função <i>rect</i> da biblioteca.
- Possui funções para colidir objetos do jogo.
- Facilidade de manipulação de eventos do jogo.

#### Por que utilizei OS path como biblioteca:
- Utilizei a biblioteca <b>OS</b> apenas para facilitar o acesso ao diretório de imagens e áudios com a função <i>path</i>.


<!-- ## Como rodar o jogo? -->
<h2 id="how-to-run">Como rodar o jogo?</h2>
<p>
	O jogo requer o Python e o Pygame instalados no teu sistema. Instruções sobre como instalar o Python e o Pygame podem ser encontradas nos seus respectivos sites. Abra o <strong>main.py</strong> em project no terminal e rode 
	
```sh
  python main.py
```

</p>

## Arquivos

/assets

> Nesse diretório temos todas as imagens separadas por categorias e os aúdios.

/obstacles

> Nesse diretório temos todos os obstáculos, poderes e itens duráveis do jogo e suas configurações de interações com o usuário (player), onde pode ser encontrados nos arquivos <i>_manager.py</i> 

/dinossaur.py

> Tudo que o player realiza e suas interações com outros objetos são controlados nesse script.

/game.py

> É o script principal do projeto, onde o loop do jogo roda, isto é, os eventos seguidos da atualização do status do jogo e em seguinte o desenho do jogo, além de interligar aos componentes principais do jogo.

/constants

> Nesse script encontra-se todas as constantes criadas para todos os aúdios e as spritesheets, isto é, o conjunto de sprites (imagens gráficas), que utilizei para a formação das ações do personagem.

/main.py

> Arquivo onde importamos a <i>classe Game</i> do arquivo <b>game.py</b> e rodamos o jogo.

## Sobre o Processo

<table>
  <td align="center"><b>Conhecimentos Aprendidos</b></td>
  <tr/>
  <td align="left">
  <ul>
  <li>Trabalho Assíncrono</li>
  <li>Importância do trabalho em equipe e da comunicação ativa</li>
  <li>Conhecimento Compartilhado</li>
  <li>Recursos de Python e Pygame</li>
  <li>Programação Orientada a Objetos (POO) voltada ao Pygame</li>
  </ul>
  </td>
 </tr>
 </table>
