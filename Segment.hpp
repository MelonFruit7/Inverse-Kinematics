#pragma once
#include "RealVector.hpp"

class Segment {
public:
    RealVector a;
    RealVector b;
    float len, angle, thickness;
    Segment *parent = nullptr;
    Segment *child = nullptr;

    Segment();
    Segment(float x, float y, float len_, float angle_, float thickness_ = 10);
    Segment(Segment *parent_, float len_, float angle_, float thickness_ = 10);

    RealVector follow(float tx, float ty);
    void calculateB();
    void update(); 
    void show();
};