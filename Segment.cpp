#include "raylib.h"
#include "Segment.hpp"
#include <cmath>

Segment::Segment() {};
Segment::Segment(float x, float y, float len_, float angle_, float thickness_) {
    a = RealVector(x, y);
    len = len_;
    angle = angle_;
    thickness = thickness_;
    update();
}

RealVector Segment::follow(float tx, float ty) {
    RealVector t(tx, ty);
    RealVector dir = t.sub(a);
    angle = dir.angleOf();

    a.x = t.x - len*cos(angle);
    a.y = t.y - len*sin(angle);
    return RealVector(a.x, a.y);
}  

void Segment::calculateB() {
    b.x = a.x + len*cos(angle);
    b.y = a.y + len*sin(angle);
}
void Segment::update() {calculateB();}

void Segment::show() {
    DrawLineEx((Vector2){a.x, a.y}, (Vector2){b.x, b.y}, thickness, BLACK);
}