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

        cur_file = filesNeeded[43:54]
        other_files1, other_files1_copy = filesNeeded[:43], filesNeeded[:43].copy()
        other_files2, other_files2_copy = filesNeeded[54:], filesNeeded[54:].copy()

        self.play(Unwrite(other_files1), Unwrite(other_files2))
        cur_file_og_position = cur_file.get_center()
        self.play(cur_file.animate.center().to_edge(UP))

        self.wait(1)

        code = Code("assets/code/Segment.cpp", language="cpp", font_size=10, line_spacing=0.8)[2]
        self.play(Write(code))

        self.wait(3)

        self.ripple(code, range(4, 12), -1) # constructors
        self.wait(10)
        self.ripple(code, range(23, 28), -1) # update functions
        self.wait(10)

        # follow function
        self.ripple(code, range(13, 14), -1) 
        self.wait(10)
        self.ripple(code, range(14, 17), -1) 
        self.wait(10)

        # showing vector example
        self.play(code.animate.scale(0.25).to_edge(DL))
        axes = Axes()
        main_dot = Dot([0,0,0], radius=0.25)
        a_dot = LabeledDot(Text("a", color=RED, font_size=24), point=[1.5, -3, 0])
        t_dot = LabeledDot(Text("t", color=RED, font_size=24), point=[5.3, -1.4, 0])
        aVec = Arrow(start=[0, 0, 0], end=a_dot.get_center())
        tVec = Arrow(start=[0, 0, 0], end=t_dot.get_center())

        self.play(Write(axes), Write(main_dot), Write(a_dot), Write(t_dot), Write(aVec), Write(tVec))
        self.wait(2)

        
        subVec = LabeledArrow("t - a", start=a_dot.get_center(), end=t_dot.get_center(), label_position=0.5)
        xLine = Line(a_dot.get_center()+RIGHT*0.1, [t_dot.get_x(), a_dot.get_y(), 0]);
        yLine = Line([t_dot.get_x(), a_dot.get_y(), 0], t_dot.get_center()+DOWN*0.15)
        angle = Angle(xLine, subVec)
        self.play(Write(subVec), Write(xLine), Write(yLine), Write(angle))
        self.wait(5)
        self.play(Unwrite(axes), Unwrite(main_dot), Unwrite(a_dot), Unwrite(t_dot), Unwrite(aVec), Unwrite(tVec), Unwrite(subVec), Unwrite(xLine), Unwrite(yLine), Unwrite(angle))
        self.play(code.animate.scale(4).center())
        self.wait(2)

        self.ripple(code, range(18, 21), -1)
        self.wait(21)

        self.ripple(code, range(29, 32), -1) # show function
        self.wait(2)

        self.play(Unwrite(code))


        self.play(cur_file.animate.move_to(cur_file_og_position))
        self.play(Write(other_files1_copy), Write(other_files2_copy))
