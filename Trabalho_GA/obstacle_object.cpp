#include "obstacle_object.h"


ObstacleObject::ObstacleObject()
    : GameObject(), Radius(12.5f), IsStopped(true), IsBomb(false) { }

ObstacleObject::ObstacleObject(glm::vec2 pos, float radius, glm::vec2 velocity, Texture2D sprite)
    : GameObject(pos, glm::vec2(radius * 2.0f, radius * 2.0f), sprite, glm::vec3(1.0f), velocity), Radius(radius), IsStopped(true), IsBomb(false), IsLife(false) { }

glm::vec2 ObstacleObject::Move(float dt, unsigned int window_width)
{
    // Se o jogo ja comecou
    if (!this->IsStopped)
    {
        // o iceberg se mexe.
        this->Position.x -= (dt * this->Velocity.y);

    }
    return this->Position;
}

// Reseta o gelo.
void ObstacleObject::Reset(glm::vec2 position, glm::vec2 velocity)
{
    this->Position = position;
    this->Velocity = velocity;
    this->IsStopped = true;
    this->IsBomb = false;
}

//Teleporta o gelo para uma posicao.
void ObstacleObject::Teleport(glm::vec2 position) {

    this->Position = position;
}

//Aumenta a velocidade do gelo.
void ObstacleObject::IncreaseVelocity(int numColl) {
    this->Velocity += glm::vec2(0.0f, numColl);
}