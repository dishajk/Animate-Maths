from manim import *

class ShowWrite(Scene):
    def construct(self):
        numbers = ["14", "25", "3", "8", "30", "21", "11", "5", "17", "9", "28", "1", "19", "12", "24", "15", "20", "7", "2", "23", "29", "10", "18", "26", "16", "6", "13", "22", "4", "27"]
        number_mob_list = [Tex(number, font_size=48) for number in numbers]  # Adjust font size for visibility
        animations = []
        current_position = np.array([-6, 3.5, 0])  # Start position at the top-left corner
        for number_mob in number_mob_list:
            number_mob.move_to(current_position)
            animations.append(Write(number_mob))
            current_position += np.array([number_mob.get_width() * 1.2, 0, 0])  # Adjust spacing between numbers
        self.play(*animations, run_time=10)  # Adjust run_time as needed
