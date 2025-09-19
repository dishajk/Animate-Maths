from manim import *
import numpy as np

class BhaskaraII_ICTS(Scene):
    def construct(self):

# color
        icts_grey="#9BAFC5"
        WHITE = "#fafafa"
        icts_maroon = "#90403d"
        # icts_maroon = "#c32929"
        icts_highlight = "#F88826"
        self.camera.background_color = WHITE

# angle
        angle = np.arctan(507/245)
# scale
        scale = 1/135

# length
        a_length = 245*scale
        b_length = 507*scale
        c_length = 4.0  
# points
        V = [np.array([0,0,0]), np.array([c_length*np.cos(angle),c_length*np.sin(angle),0]), np.array([c_length*(np.cos(angle)-np.sin(angle)),c_length*(np.cos(angle)+np.sin(angle)),0]), np.array([-c_length*np.sin(angle),c_length*np.cos(angle),0])]

        triangles = VGroup()

        for i in range(len(V)):
                A = V[i]
                B = V[(i + 1) % len(V)]
                if i % 2 == 1:
                        C = np.array([B[0], A[1], 0])
                else:           
                        C = np.array([A[0], B[1], 0])
                triangle = Polygon(A, B, C,stroke_color=WHITE,fill_color=icts_maroon,fill_opacity=1,stroke_width=5)

                triangles.add(triangle)
                
        square = Polygon(*V, stroke_color=BLACK, stroke_width=2)



        # right_angles = VGroup(*[RightAngle(Line(V[i], V[(i+1) % 4]), Line(V[(i+1) % 4], V[(i+2) % 4]), length=0.3, quadrant=(i+1) % 4, stroke_color=WHITE) for i in range(4)])
        
        c_labels = VGroup()
        for i in range(len(V)):
            A = V[i]
            B = V[(i + 1) % 4]
            midpoint = (A + B) / 2
            label = Tex("c").move_to(midpoint+outward)
            c_labels.add(label)

        figure = VGroup(triangles, square, c_labels).move_to(ORIGIN)
        
        self.play(FadeIn(triangles),run_time=1)
        self.play(Create(square), FadeIn(labels), run_time=2)
        
        self.wait(2)

        # vertices = [V1, V2, V3, V4]
        # quad = Polygon(V1, V2, V3, V4, stroke_color=WHITE)
        # self.add(quad)

        # def right_triangle_at(vertex):
        #         # Right-angled triangle pointing "outward" along x and y axes
        #         p1 = vertex
        #         p2 = vertex + np.array([size,0,0])
        #         p3 = vertex + np.array([0,size,0])
        #         return Polygon(p1, p2, p3, fill_opacity=0.5, fill_color=BLUE, stroke_color=WHITE)


        # square = Square(side_length=c_length)
        # square.set_fill(icts_grey, opacity=0.5)
        # square.rotate(angle)
        # self.play(Create(square),run_time=2)
        # tr = Polygon(V1,V2,V3,V4,stroke_color=WHITE,fill_color=icts_maroon,fill_opacity=1,stroke_width=4)
        # square.move_to(ORIGIN)
        # self.play(Create(square),run_time=2)

        # A = np.array([-(a_length+b_length)/2,-(b_length-a_length)/2,0])
        # B = A + a_length*RIGHT
        # C = B + b_length*UP
        # mA = -A

        # triangle = Polygon(A,B,C,stroke_color=WHITE,fill_color=icts_maroon,fill_opacity=1,stroke_width=4)
        # triangle2 = triangle.copy().rotate(PI/2).shift(DOWN*(a_length+b_length)/2+RIGHT*(b_length-a_length)/2)
        # triangle3 = triangle2.copy().rotate(PI/2).shift(UP*(b_length-a_length)/2+RIGHT*(a_length+b_length)/2)
        # triangle4 = triangle3.copy().rotate(PI/2).shift(UP*(a_length+b_length)/2+LEFT*(b_length-a_length)/2)
        # self.play(FadeIn(triangle),FadeIn(triangle2),FadeIn(triangle3),FadeIn(triangle4))
        
        # AC = C-A
        # c_label = MathTex("$c$",color=BLACK).next_to(A,LEFT)
        # perp = np.array([AC[1], -AC[0], 0])
        # D = A + perp
        # E = C + perp
        # square = Polygon(A, C, E, D, stroke_color=BLACK)
        
        # self.wait(2)
        # self.play(Create(square),c_label,)
        # self.wait(2)