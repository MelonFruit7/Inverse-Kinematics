#pragma once
#include "RealVector.hpp"

class Segment {
    public:
        RealVector a, b;
        float len, angle, thickness;

        Segment();
        Segment(float x, float y, float len, float angle, float thickness);

        RealVector follow(float tx, float ty);
        void calculateB();
        void update(); 
        void show();
};