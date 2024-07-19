#include <raylib.h>
#include "SegCollection.hpp"

int main() {
    int screenWidth = 1250, screenHeight = 750;
    InitWindow(screenWidth, screenHeight, "Inverse Kinematics");

    SegCollection segments;
    for (int i = 0; i < 500; i++) segments.addSeg(0, 0, 1, 0, i+1);

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(WHITE);

        segments.gotoPosition(GetMouseX(), GetMouseY());

        EndDrawing();
    }
    CloseWindow();
    return 0;
}