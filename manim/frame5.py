from manim import *

class sc(Scene):
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

        cur_file = filesNeeded[7:15]
        other_files1, other_files1_copy = filesNeeded[:7], filesNeeded[:7].copy()
        other_files2, other_files2_copy = filesNeeded[15:], filesNeeded[15:].copy()


        self.play(Unwrite(other_files1), Unwrite(other_files2))
        cur_file_og_position = cur_file.get_center()
        self.play(cur_file.animate.center().to_edge(UP))

        self.wait(1)
        code = Code("assets/code/main1.cpp", language="cpp", font_size=18, line_spacing=0.8)[2]
        self.play(Write(code))
        self.wait(3)

        self.ripple(code, range(3, 5), -1)
        self.wait(1)
        self.ripple(code, range(9, 12), -1)
        self.wait(3)
        self.ripple(code, range(13, 14), 2)
        self.wait(1)

        self.play(Unwrite(code))


        self.play(cur_file.animate.move_to(cur_file_og_position))
        self.play(Write(other_files1_copy), Write(other_files2_copy))
