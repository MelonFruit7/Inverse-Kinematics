#pragma once
#include "Segment.hpp"

class SegCollection {
public:
    Segment *root;
    Segment *rootCopy;
    SegCollection(float x, float y, int amount, float width, float len);
    void gotoPosition(float tx, float ty);
    void changeStartPoint(float x, float y);
    void freeSeg();
};