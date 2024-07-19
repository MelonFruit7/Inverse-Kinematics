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
    
    if (y < 0 && x < 0) angle += M_PI; //We're in the 3rd quadrant, our angle was outputted in the 1st
    else if (x < 0) angle += M_PI; //We're in the 2nd quadrant, our angle was outputted in the 4th
    return angle; 
}