#pragma once

class RealVector {
    public:
        float x, y;

        RealVector();
        RealVector(float x, float y);

        RealVector add(RealVector &vec);
        RealVector sub(RealVector &vec);
        float getMag();
        float angleOf();
};