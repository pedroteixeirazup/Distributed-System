# Projeto-Sistemas-Distribuidos
Projeto feito com o objetivo de aprender mais sobre a criação e implementação de um sistema distribuído.

## Jogo da velha (tic-tac-toe)
![Erro, Gif indisponível!](https://thumbs.gfycat.com/PoisedGrippingFox-small.gif)


### Ideia inicial
A ideia é criar um jogo da velha para que a turma inteira possa jogar em um servidor, cada um em sua thread

O servidor suportará até 30 pessoas conectadas, sendo que a cada duas conexõe, uma thread diferente será separada para aqueles jogadores jogarem um contra o outro.

As regras do jogo sao simples e estão claramente explicadas no link abaixo:
[LINK PARA AS REGRAS](https://www.bigmae.com/regras-jogo-da-velha/)

### Funcionamento
* Ao abrir o servidor, dois usuários devem se conectar. Quando eles entrarem, será criada uma thread para rodar a função principal do jogo. Isso pode ser feito para até 30 usuários, ou seja, 15 threads serão criadas. 
* Após os dois jogadores se conectarem, o administrador do servidor deverá perguntar se eles querem começar um novo jogo ou recuperar um estado de jogo anterior (caso tenha havido algum erro no servidor ou se alguem precisou sair). 
* Com a resposta dos usuários, o administrador irá dar um comando para o servidor, que irá realizar uma dessas duas opções.
* Caso recupere um estado anterior, serão recuperados do ultimo jogo: o tabuleiro, a pontuação do circulo, pontuação do xis e o numero da jogada (a vez de quem iria jogar).
* Caso escolha para iniciar um novo jogo, tudo será iniciado do zero.
* A cada jogada de cada jogador o jogo é salvo em um arquivo com o endereço IP dos dois jogadores. Para recuperar, o servidor utiliza o endereço dos jogadores conectados.

### Linguagem de implementação
O jogo será implementado em Python.

### Componentes
30 Clients (jogadores), 1 interface para rodar o jogo (terminal), 1 servidor para as pessoas acessarem.

### Lista de testes a serem implementados
* Teste de ponta a ponta: para mostrar que todas as jogadas que um jogador faz podem ser vistas pelo outro.<br>
* Teste de concorrência: demonstrando que múltiplos clientes podem acessar o serviço ao mesmo tempo, sem comportamentos estranhos.<br>
* Teste de recuperação de falhas: quando um componente falha é possivel recuperar um estado anterior do jogo<br>
* Demonstração de funcionalidades: Mostrar que as funcionalidades estão implementadas, ou seja, que é realmente possível jogar o jogo sem falhas.<br>

### Como executar?
1. Clone o projeto
2. Entre na pasta
3. Abra o terminal e execute o servidor: > python server.py
4. Abra mais dois terminais e execute os clients: > python client.py
5. Nos clients, será pedido o ip do servidor, basta colocar o ip
6. Pronto, tudo certo para jogar, basta escolher uma opção no servidor (Jogar ou recuperar jogo anterior)
