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

    def ripple(self, code, lines, time):
        curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1])

        ripples = []

        for line in lines:
            if (len(code[line]) > 0):
                anims = []
                for char in code[line]:
                    curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
                    anims.append(MoveAlongPath(char, curve, run_time=0.5))
                ripples.append(AnimationGroup(anims, lag_ratio=0.1))
        if (time != -1):
            self.play(*ripples, run_time=time)
        else:
            self.play(*ripples)

    def construct(self):
        filesNeeded = Text("Makefile\nmain.cpp\nRealVector.cpp\nRealVector.hpp\nSegment.cpp\nSegment.hpp\nSegCollection.cpp\nSegCollection.hpp").scale(0.25).to_edge(UL)
        self.add(filesNeeded)
        self.wait(2)

        cur_file = filesNeeded[65:82]
        other_files1, other_files1_copy = filesNeeded[:65], filesNeeded[:65].copy()
        other_files2, other_files2_copy = filesNeeded[82:], filesNeeded[82:].copy()

        self.play(Unwrite(other_files1), Unwrite(other_files2))
        cur_file_og_position = cur_file.get_center()
        self.play(cur_file.animate.center().to_edge(UP))

        self.wait(1)

        code = Code("assets/code/SegCollection.cpp", language="cpp", font_size=10, line_spacing=0.8)[2]
        self.play(Write(code))

        self.wait(1)
        self.ripple(code, range(4, 5), -1) # goto function
        self.wait(2)
        self.ripple(code, range(5 ,6), -1) # first line
        self.wait(1)

        self.ripple(code, range(7, 9), -1) # follow logic
        self.wait(8)

        self.ripple(code, range(10, 20), -1) # update logic
        self.wait(10)

        # Random dots
        dot_1 = Dot([0, 0, 0], color=BLUE)
        dot_2 = Dot([0.5, 0.25, 0], color=BLUE)
        dot_3 = Dot([1, 1.75, 0], color=BLUE)
        dots = VGroup(dot_1, dot_2, dot_3).center()

        # Lines connecting dots
        line_1 = Line(dot_1.get_center(), dot_2.get_center(), 2.0)
        line_2 = Line(dot_2.get_center(), dot_3.get_center(), 2.0)

        lines = VGroup(line_1, line_2)
        dotsWithLines = VGroup(lines, dots)

        self.play(code.animate.shift(DOWN*10))
        self.play(Write(dotsWithLines))

        linesArr = [line_1, line_2]
        dotsArr = [dot_1, dot_2, dot_3]
        target = Dot([-4, 2, 0], color=BLUE)
        self.moveLines(dotsArr, linesArr, target, BLUE)

        dotsWithLines = VGroup(*(linesArr + dotsArr))
        self.play(dotsWithLines.animate.center())
        self.wait(3)

        self.play(Transform(dotsWithLines, code.copy().shift(UP*10)))
        code = dotsWithLines
        self.wait(5)

        self.ripple(code, range(22, 25), -1)
        self.wait(2)
        self.ripple(code, range(26, 30), -1)
        self.wait(2)
        self.ripple(code, range(31, 34), -1)
        self.wait(2)

        self.play(Unwrite(code))


        self.play(cur_file.animate.move_to(cur_file_og_position))
        self.play(Write(other_files1_copy), Write(other_files2_copy))
        self.play(Unwrite(other_files1_copy), Unwrite(other_files2_copy), Unwrite(cur_file))
        self.wait(1)