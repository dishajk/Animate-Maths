from manim import *
import random

class mathsCircle(Scene):
    def construct(self):
        icts_maroon = "#90403d"
        organisers = VGroup()
        org_pos = [0.7, 0.8, 0]
        z = org_pos[0] + 1j*org_pos[1]
        for i in range(4):
            org_tri = Triangle(color=WHITE,fill_color=icts_maroon,fill_opacity=1)
            org_tri.set_height(0.5).rotate(i*10*DEGREES)
            rotated_z = z * np.exp(1j * np.pi * i/ 2)
            org_pos_rotated = [round(float(rotated_z.real),2), round(float(rotated_z.imag),2), 0]
            org_tri.shift(org_pos_rotated)  
            organisers.add(org_tri)
        
        text = Text("Organising Team",font_size=36).move_to(1.5*DOWN)
        # Organisers appear
        self.play(*[FadeIn(org_tri) for org_tri in organisers])
        self.play(FadeIn(text))
        self.wait(3)

        # Organisers move to left top corner
        self.play(organisers.animate.shift([-5,2,0]-organisers[2].get_center()))
        self.wait(2)

