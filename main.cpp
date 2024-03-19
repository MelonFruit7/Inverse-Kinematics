#include "raylib.h"
#include "RealVector.hpp"
#include "Segment.hpp"
#include "SegCollection.hpp"
#include <iostream>

int main() {
    int screenWidth, screenHeight;
    InitWindow(1000, 750, "Inverse Kinematics");
    screenWidth = GetScreenWidth();
    screenHeight = GetScreenHeight();
    SetTargetFPS(120);

    Segment seg(200, 200, 100, 0, 5);
    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(WHITE);

        seg.follow(GetMouseX(), GetMouseY());
        seg.update();
        seg.show();

        DrawFPS(0, 0);
        EndDrawing();
    }
    CloseWindow();
}