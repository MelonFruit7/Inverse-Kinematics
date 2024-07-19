#include <raylib.h>

int main() {
    int screenWidth = 750, screenHeight = 500;
    InitWindow(screenWidth, screenHeight, "Inverse Kinematics");

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(WHITE);

        EndDrawing();
    }
    
    CloseWindow();
    return 0;
}