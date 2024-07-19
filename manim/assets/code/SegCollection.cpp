#include "SegCollection.hpp"

SegCollection::SegCollection() {}

void SegCollection::gotoPosition(float tx, float ty) {
    if (segments.size() == 0) return;

    RealVector pos = segments[0].follow(tx, ty);
    for (int i = 1; i < segments.size(); i++) pos = segments[i].follow(pos.x, pos.y);

    int last = segments.size()-1;
    //changeStartPoint(segments[last], 100, 100);
    segments[last].update();
    segments[last].show();

    for (int i = last-1; i >= 0; i--) {
        //changeStartPoint(segments[i], segments[i+1].b.x, segments[i+1].b.y);
        segments[i].update();
        segments[i].show();
    }
}

void SegCollection::showCollection() {
    for (int i = 0; i < segments.size(); i++) segments[i].show();
}

void SegCollection::changeStartPoint(Segment &seg, float x, float y) {
    seg.a.x = x;
    seg.a.y = y;
}

void SegCollection::addSeg(float x, float y, float len, float angle, float thickness) {
    segments.push_back(Segment(x, y, len, angle, thickness));
}