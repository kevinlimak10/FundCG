# Submarine
## Kevin Lima, Vítor Mello e Carolina Prates

### Jogo

### objetivo:
- O jogo consiste em navegar sem colidir com os obstaculos.
- Pegar vidas garante mais chances de sobrevivencia em caso de colisão.
- Se ver o missel, significa que está em sua ultima vida.
- Para cada vez que desvia do obstaculo, você irá passar de turno e ganhar +1 ponto.
- Colidir com Obstaculos faz você perder pontos.

### Logica aplicada:

- Ao clicar Espaço irá iniciar a partida, com a vida em 3, e a proxima vida extra irá receber em 10 turnos
- Ao obstaculo colidir com a parede ele é teletransportado para o inicio em um eixo Y aleatorio.
- Caso colidir com o jogador, é usado um decremento de vida, diminuição da pontuação, teleporte do objeto para o inicio e validará se for a ultima vida, fazer o decremento da vida.
- Todos as interações do submarino e obstaculo, ocorrem "abaixo da Água", no caso obtemos o eixo y e deixamos uma barreira para não ultrapassar a borda e a agua.