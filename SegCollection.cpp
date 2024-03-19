#include "SegCollection.hpp"
#include "Segment.hpp"
#include "RealVector.hpp"
#include "stdlib.h"

SegCollection::SegCollection(float x, float y, int amount, float width, float len) {
    root = (Segment*)malloc(sizeof(Segment)); 
    *root = Segment(x, y, len, 0, width);
    rootCopy = root;
    for (int i = 1; i < amount; i++) {
        Segment *seg = (Segment*)malloc(sizeof(Segment)); 
        *seg = Segment(root, len, 0, width);
        root->child = seg;
        root = seg;
    }
    
}

void SegCollection::gotoPosition(float tx, float ty) {
    RealVector vec = root->follow(tx, ty);
    while (true) {
        if (root->parent == nullptr) break;
        root = root->parent;
        vec = root->follow(vec.x, vec.y);
    }

    while (true) {
        root->update();
        root->show();
        if (root->child == nullptr) break;
        root->child->a.x = root->b.x;
        root->child->a.y = root->b.y;
        root = root->child;
    }
}

void SegCollection::changeStartPoint(float x, float y) {
    rootCopy->a.x = x;
    rootCopy->a.y = y;
}

void SegCollection::freeSeg() {
    while (root->parent != nullptr) {
        root = root->parent;
        free(root->child);
    }
    free(root);
}

