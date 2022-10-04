#include <glad/glad.h>
#include <glm/glm.hpp>

#include "game_object.h"
#include "sprite_renderer.h"
#include "resource_manager.h"


// Tamanho do player.
const glm::vec2 PLAYER_SIZE(60.0f, 60.0f);
// Velocidade do player.
const float PLAYER_VELOCITY(200.0f);

// Velocidade do obstaculo.
const glm::vec2 INITIAL_ICE_VELOCITY(0.0f, 300.0f);

// Raio do gelo.
const float ICE_RADIUS = 15.5f;

class Game
{
public:
    // game state
    bool         Keys[1024];
    unsigned int Width, Height;
    int NUM_NO_COLLISION = 0;
    int POINTS = 0;
    int ROUND = 1;
    int ROUND_NEXT_LIFE = 10;
    int LIFE = 3;
    // Construtor
    Game(unsigned int width, unsigned int height);
    ~Game();
    // Inicializacao (carrega shaders, texturas)
    void Init();
    // Loop de jogo
    void ProcessInput(float dt);
    void Update(float dt);
    void Render();
    void updateLife();
    //Checa as colisoes
    void DoCollisions();
    //Reseta o jogo quando a condicao de perda ocorre.
    void ResetPlayer();
};