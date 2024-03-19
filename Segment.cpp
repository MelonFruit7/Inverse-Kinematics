#include "Segment.hpp"
#include <cmath>
#include "raylib.h"
#include <iostream>

Segment::Segment() {}
Segment::Segment(float x, float y, float len_, float angle_, float thickness_) {
    a.x = x;
    a.y = y;
    len = len_;
    angle = angle_*(M_PI/180); //Assumes angles was inputted as degrees, converting to radians 
    thickness = thickness_;
    update();
}
Segment::Segment(Segment *parent_, float len_, float angle_, float thickness_) {
    parent = parent_;
    a.x = parent_->b.x;
    a.y = parent_->b.y;
    len = len_;
    angle = angle_;
    thickness = thickness_;
    update();
}

RealVector Segment::follow(float tx, float ty) {
    RealVector t(tx, ty);
    RealVector dir = t.sub(a);
    angle = dir.angleOf();

    a.x = t.x + len*cos(angle+M_PI);
    a.y = t.y - len*sin(angle+M_PI);
    return RealVector(t.x + len*cos(angle+M_PI), t.y - len*sin(angle+M_PI));
}

void Segment::calculateB() {
    b.x = a.x + len*cos(angle);
    b.y = a.y - len*sin(angle);
}
void Segment::update() {calculateB();}

void Segment::show() {
    DrawLineEx((Vector2){a.x,a.y}, (Vector2){b.x, b.y}, thickness, BLACK);
}