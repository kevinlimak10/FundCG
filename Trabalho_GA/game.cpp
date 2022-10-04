#include "game.h"
#include "resource_manager.h"
#include "sprite_renderer.h"
#include <GLFW/glfw3.h>
#include "obstacle_object.h";
#include "game_object.h";
#include <stdio.h>
#include<iostream>


SpriteRenderer* Renderer;
GameObject* Player;
ObstacleObject* Obstacle;

Game::Game(unsigned int width, unsigned int height)
    : Keys(), Width(width), Height(height)
{

}

Game::~Game()
{
    delete Renderer;
    delete Player;
    delete Obstacle;
}

void Game::Init()
{
    // Carrega shaders.
    ResourceManager::LoadShader("shaders/sprite.vs", "shaders/sprite.frag", nullptr, "sprite");
    // configura shaders.
    glm::mat4 projection = glm::ortho(0.0f, static_cast<float>(this->Width),
        static_cast<float>(this->Height), 0.0f, -1.0f, 1.0f);
    ResourceManager::GetShader("sprite").Use().SetInteger("image", 0);
    ResourceManager::GetShader("sprite").SetMatrix4("projection", projection);
    // set render-specific controls
    Shader myShader;
    myShader = ResourceManager::GetShader("sprite");
    Renderer = new SpriteRenderer(myShader);
    // Carrega texturas.
    ResourceManager::LoadTexture("textures/fundo_mar.png", false, "background");
    ResourceManager::LoadTexture("textures/torpedo.png", true, "bomber");
    ResourceManager::LoadTexture("textures/iceberg.png", true, "iceberg");
    ResourceManager::LoadTexture("textures/submarine.png", true, "player");
    ResourceManager::LoadTexture("textures/life.png", true, "life");

    //Criacao dos objetos.
    glm::vec2 playerPos = glm::vec2(10.0f, this->Height / 2.0f);
    Player = new GameObject(playerPos, PLAYER_SIZE, ResourceManager::GetTexture("player"));
    glm::vec2 obsPos = glm::vec2(this->Width - (2.0f * ICE_RADIUS), this->Height/2.0f);
    Obstacle = new ObstacleObject(obsPos, ICE_RADIUS, INITIAL_ICE_VELOCITY, ResourceManager::GetTexture("iceberg"));
    ROUND_NEXT_LIFE = 10;
    std::cout << "PROXIMA VIDA EM: " << ROUND_NEXT_LIFE << "\n";
}

void Game::Update(float dt)
{
    //Move a bola
    Obstacle->Move(dt, this->Width);
    //Checagem de colisoes.
    this->DoCollisions();
    
    if (ROUND_NEXT_LIFE == ROUND) {
        Obstacle->IsLife = true;
        //DEFINE A PROXIMA VIDA DENTRO DE 20 ROUNDS
        ROUND_NEXT_LIFE = (rand() % 20) + ROUND;
        
    }else if (LIFE > 1) {
        //Se tem 2 colisões fica com torpedos
        Obstacle->IsBomb = false;
    }
    else {
        Obstacle->IsBomb = true;
    }
    //Se o gelo bater 3 vezes game over
    if (LIFE == 0)
    {
        printf("Entrou no NUM_NO_COLLISION == 3");
        this->ResetPlayer();
    }

    //Se bater na borda voltar ao inicio
    if (Obstacle->Position.x <= 0) {
        int randomHeigth = (rand() % (this->Height / 2 + 1)) + this->Height / 2;
        glm::vec2 icePos = glm::vec2(this->Width, randomHeigth);
        Obstacle->Teleport(icePos);
        Obstacle->IsBomb = false;
        Obstacle->IsLife = false;
        POINTS++;
        std::cout << "Pontuação do jogador: " << POINTS << "\n";
        Obstacle->IncreaseVelocity(5);
        std::cout << "Status obstaculos: " << Obstacle->Velocity.y << "\n";
        std::cout << "Status vidas: " << LIFE << "\n";
        std::cout << "PROXIMA VIDA EM: " <<  ROUND_NEXT_LIFE - ROUND << "\n";
        ROUND++;
    }
}

void Game::updateLife() {
    LIFE++;
}

//Recebe a velocidade por parametro
void Game::ProcessInput(float dt)
{
    float velocity = PLAYER_VELOCITY * dt;
        // Movimento do player.
    if (this->Keys[GLFW_KEY_UP])
    {
        if (Player->Position.y >= (this->Height / 2))
        {//Movimento para cima.
            Player->Position.y -= velocity;
        }
    }
    if (this->Keys[GLFW_KEY_DOWN])
    {
        if (Player->Position.y <= this->Height-50)
        {//Movimento para baixo.
            Player->Position.y += velocity;
        }
    }//Barra de espaco comeca o jogo.
    if (this->Keys[GLFW_KEY_SPACE])
        Obstacle->IsStopped = false;
}

void Game::Render()
{
    //Renderizando o background
    Texture2D background;
    background = ResourceManager::GetTexture("background");
    Renderer->DrawSprite(background, glm::vec2(0.0f, 0.0f), glm::vec2(this->Width, this->Height));


    if (Obstacle->IsBomb) {
        //SE for uma bomba
        Obstacle->Sprite = ResourceManager::GetTexture("bomber");
    }
    else if (Obstacle->IsLife) {
        //SE for uma vida
        Obstacle->Sprite = ResourceManager::GetTexture("life");
    } else {
        //Se nao for apenas gelo
        Obstacle->Sprite = ResourceManager::GetTexture("iceberg");
    }
    Obstacle->Draw(*Renderer);
    Player->Draw(*Renderer);
    //Renderizando player e o obstaculo.
}


void Game::ResetPlayer()
{
    // Reseta o player, bola e numero de colisoes.
    Player->Size = PLAYER_SIZE;
    Player->Position = glm::vec2(10.0f, this->Height / 2.0f);
    glm::vec2 ballPos = glm::vec2(this->Width - (2.0f * ICE_RADIUS), this->Height / 2.0f);
    Obstacle->Reset(ballPos, INITIAL_ICE_VELOCITY);
    LIFE = 3;
    std::cout << "Pontuação final do jogador: " << POINTS <<"\n";
    ROUND = 0;
}


bool CheckCollision(GameObject& one, GameObject& two)
{
    // Colisao no x
    bool collisionX = one.Position.x + one.Size.x >= two.Position.x &&
        two.Position.x + two.Size.x >= one.Position.x;
    // Colisao no y
    bool collisionY = one.Position.y + one.Size.y >= two.Position.y &&
        two.Position.y + two.Size.y >= one.Position.y;

    return collisionX && collisionY;
}

void Game::DoCollisions()
{
    int randomHeigth = (rand() % (this->Height/2 + 1))+ this->Height/2;
    glm::vec2 obsPos = glm::vec2(this->Width, randomHeigth);

    if (CheckCollision(*Obstacle, *Player) && Obstacle->IsLife) {
        updateLife();
        Obstacle->IsLife = false;
        Obstacle->Teleport(obsPos);
    }
    if (CheckCollision(*Obstacle, *Player) && Obstacle->IsBomb) {
        //Se tiver colisao e for a bomba, reinicia o jogo.
        printf("Entrou no DoCollisions");
        ResetPlayer();
    }
    if (CheckCollision(*Obstacle, *Player) ) {
        //Com a colisão joga o gelo para outra altura na agua.
        Obstacle->IncreaseVelocity(NUM_NO_COLLISION);
        POINTS -= 10;
        LIFE--;
        Obstacle->Teleport(obsPos);
    }
}