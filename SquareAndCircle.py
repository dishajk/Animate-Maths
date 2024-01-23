from manim import *
        
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square2 = Square()  # create a square
        square2.set_fill(GREEN, opacity=0.5)  # set the color and transparency

        square.next_to(circle, UP, buff=0.5)  # set the position
        square2.next_to(circle, LEFT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square), Create(square2))  # show the shapes on screen    