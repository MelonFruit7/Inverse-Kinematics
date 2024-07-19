#pragma once
#include <iostream>
#include <vector>
#include "Segment.hpp"

class SegCollection {
    std::vector<Segment> segments;
    public:
        SegCollection();
        void gotoPosition(float tx, float ty);
        void showCollection();
        void changeStartPoint(Segment &seg, float x, float y);
        void addSeg(float x, float y, float len, float angle, float thickness);
};