from manim import *

class sc(Scene):
    def construct(self):
        cppLogo = SVGMobject("assets/cpp.svg")

        rayLogo = SVGMobject("assets/raylib.svg")
        rayBackground = Rectangle(WHITE, rayLogo.height, rayLogo.width, fill_opacity=1)

        cppLogo.move_to(LEFT*2)
        rayLogo.move_to(RIGHT*2)
        rayBackground.move_to(rayLogo.get_center())

        self.play(DrawBorderThenFill(cppLogo), DrawBorderThenFill(rayBackground), DrawBorderThenFill(rayLogo))
        self.wait(6)

        dot = Dot()
        self.play(Transform(rayLogo, dot), Transform(rayBackground, dot), Transform(cppLogo, dot))
        self.play(Unwrite(rayLogo), Unwrite(cppLogo), Unwrite(rayBackground))
        self.wait(1)