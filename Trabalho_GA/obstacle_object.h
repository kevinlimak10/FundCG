#ifndef BALLOBJECT_H
#define BALLOBJECT_H

#include <glad/glad.h>
#include <glm/glm.hpp>

#include "game_object.h"
#include "texture.h"



class ObstacleObject : public GameObject
{
public:
    float   Radius;
    bool    IsStopped;
    bool    IsBomb;
    bool    IsLife;
    // Construtores.
    ObstacleObject();
    ObstacleObject(glm::vec2 pos, float radius, glm::vec2 velocity, Texture2D sprite);
    // Movimenta o gelo.
    glm::vec2 Move(float dt, unsigned int window_width);
    // Reseta o gelo com a velocidade e posicao original.
    void      Reset(glm::vec2 position, glm::vec2 velocity);

    void      Teleport(glm::vec2 position);

    void      IncreaseVelocity(int numColl);
};

#endif