from manim import *

class sc(Scene):
    def construct(self):
        text = Text("Let's start with all of the files we'll need")
        filesNeeded = Text("Makefile\nmain.cpp\nRealVector.cpp\nRealVector.hpp\nSegment.cpp\nSegment.hpp\nSegCollection.cpp\nSegCollection.hpp")
        self.play(Write(text))
        self.wait(1)
        self.play(Transform(text, filesNeeded))
        self.wait(7)
        self.play(text.animate.scale(0.25).to_edge(UL))
        self.wait(1)
