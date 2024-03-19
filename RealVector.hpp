#pragma once

class RealVector {
public:
    float x, y;

    RealVector();
    RealVector(float x_, float y_);

    RealVector add(RealVector &a);
    RealVector sub(RealVector &a);
    float getMag();
    float angleOf();
};