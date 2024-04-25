from manim import *

class ShowWrite(Scene):
    def construct(self):
        numbers = [14, 25,3,8, 30, 21, 11,5, 17,9, 28,1, 19, 12, 24, 15, 20,7,2, 23, 29, 10, 18, 26, 16,6, 13, 22,4, 27]

        starting_position = LEFT*6
        ES_sequence = VGroup()

        for i, number in enumerate(numbers):
            if i == len(numbers) - 1:
                number_text = Tex(str(number), font_size=29)
            else:
                number_text = Tex(str(number) + ",", font_size=29)
            number_text.move_to(starting_position)
            ES_sequence.add(number_text)
            self.play(AddTextWordByWord(number_text))
            starting_position += RIGHT * 0.42

        self.wait(2)
        self.play(ES_sequence.animate.shift(UP*2.5))
        self.wait(2)

        l = Line(6*LEFT+UP*2.25,6*RIGHT+UP*2.25,stroke_width=0.5)
        self.play(Create(l))
        self.wait(2)
        row = []
        row.add(Tex("row 0", font_size=22).move_to(6.8*LEFT+UP*2))
        self.play(FadeIn(row[0]))
        self.play(FadeOut(row[0]))
        self.play(FadeIn(Tex("$-\infty$", font_size=29).move_to(6.25*LEFT+UP*2)))
        self.play(ES_sequence[0].animate.move_to(5.25*LEFT+UP*2))
        lt = Tex("$<$",color='#90B134', font_size=29).move_to(5.75*LEFT+UP*2)
        self.play(FadeIn(lt))
        self.play(FadeIn(l.copy().shift(DOWN*0.5)))
        row.add(Tex("row 1", font_size=22).move_to(6.8*LEFT+UP*2))
        self.wait(2)