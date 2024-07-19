#include "RealVector.hpp"
#include <cmath>

RealVector::RealVector() {}
RealVector::RealVector(float x_, float y_) {
    x = x_;
    y = y_;
}

RealVector RealVector::add(RealVector &vec) {
    return RealVector(x+vec.x, y+vec.y);
}

RealVector RealVector::sub(RealVector &vec) {
    return RealVector(x-vec.x, y-vec.y);
}

float RealVector::getMag() {
    return sqrt(pow(x, 2) + pow(y, 2));
}

float RealVector::angleOf() {
    if (x == 0) return 0;
    float angle = atan(y/x);
    
    if (y < 0 && x < 0) angle += M_PI;
    else if (x < 0) angle += M_PI;
    return angle; 
}