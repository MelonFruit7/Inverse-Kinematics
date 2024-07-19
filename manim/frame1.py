#!/usr/bin/env manim
from manim import *
from numpy import sin, cos

class sc(Scene):

    def moveLines(self, dots, lines, targetDot, COLOR):
        curDot, curLine = len(dots)-1, len(lines)-1
        while (curDot >= 0):
            self.play(Unwrite(dots[curDot]), Write(targetDot))
            if (curLine >= 0):
                self.play(Rotate(lines[curLine],
                                angle=Line(lines[curLine].get_start(), targetDot.get_center()).get_angle()-lines[curLine].get_angle(),
                                about_point=dots[curDot-1].get_center()))
                self.play(lines[curLine].animate.move_to(targetDot.get_center()-
                                        [lines[curLine].get_length()/2*cos(lines[curLine].get_angle()), lines[curLine].get_length()/2*sin(lines[curLine].get_angle()), 0]))
            dots[curDot] = targetDot
            if (curLine >= 0):
                targetDot = Dot(lines[curLine].get_start(), color=COLOR)
            curDot -= 1
            curLine -= 1

    def construct(self):
        text = Text("What is Inverse Kinematics?")
        self.play(Write(text))
        self.wait(0.5)

        self.play(text.animate.scale(0.25).to_edge(UP+LEFT))
        self.wait(0.5)
        
        explaination = Text("Inverse kinematics is the process of getting\nthe angles of joints as they move towards a point", font_size=24, color=BLUE)
        self.play(Write(explaination))
        self.wait(3)
        self.play(explaination.animate.scale(0.5).move_to(text.get_center()).shift(DOWN*0.5+RIGHT*0.85))
        self.wait(1)

        # Random dots
        dot_1 = Dot([0, 0, 0], color=RED)
        dot_2 = Dot([0.5, 0.25, 0], color=BLUE)
        dot_3 = Dot([1, 1.75, 0], color=GREEN)
        dots = VGroup(dot_1, dot_2, dot_3).center()

        # Lines connecting dots
        line_1 = Line(dot_1.get_center(), dot_2.get_center(), 2.0)
        line_2 = Line(dot_2.get_center(), dot_3.get_center(), 2.0)

        lines = VGroup(line_1, line_2)

        self.play(Write(lines), Write(dots))
        self.wait(3)

        dots = [dot_1, dot_2, dot_3]
        lines = [line_1, line_2]

        target_dot_1 = Dot([2, -1, 0], color=PURPLE)
        self.moveLines(dots, lines, target_dot_1, PURPLE)
        self.wait(2)

        target_dot_1 = Dot([-2, 1.5, 0], color=RED)
        self.moveLines(dots, lines, target_dot_1, RED)
        self.wait(2)

        target_dot_1 = Dot([-2, 1.25, 0], color=ORANGE)
        self.moveLines(dots, lines, target_dot_1, ORANGE)
        self.wait(2)

        self.play(Uncreate(VGroup(*dots)), Uncreate(VGroup(*lines)), Uncreate(explaination), Uncreate(text))



