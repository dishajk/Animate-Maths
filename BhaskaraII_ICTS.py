from manim import *

class BhaskaraII_ICTS(Scene):
    def construct(self):
        white="#fafafa"
        self.camera.background_color = white
        icts_maroon = "#90403d"
        icts_highlight="#F88826"
        icts_grey="#9BAFC5"
        a_length = 8/4
        b_length = 15/4  

        A = np.array([-(a_length+b_length)/2,-(b_length-a_length)/2,0])
        B = A + a_length*RIGHT
        C = B + b_length*UP
        mA = -A

        triangle = Polygon(A,B,C,stroke_color=white,fill_color=icts_maroon,fill_opacity=1,stroke_width=2)
        triangle2 = triangle.copy().rotate(PI/2).shift(DOWN*(a_length+b_length)/2+RIGHT*(b_length-a_length)/2)
        triangle3 = triangle2.copy().rotate(PI/2).shift(UP*(b_length-a_length)/2+RIGHT*(a_length+b_length)/2)
        triangle4 = triangle3.copy().rotate(PI/2).shift(UP*(a_length+b_length)/2+LEFT*(b_length-a_length)/2)
         
        square_In = Polygon(B,B+UP*(b_length-a_length),B+UP*(b_length-a_length)+RIGHT*(b_length-a_length),B+RIGHT*(b_length-a_length),fill_opacity=0.2,color=icts_grey,stroke_width=0)
        line1 = Line(A,C,color=BLACK)
        line2 = line1.copy().rotate(-PI/2,about_point=A)
        line3 = line2.copy().rotate(-PI/2,about_point=line2.get_end())
        line4 = line1.copy().rotate(PI/2,about_point=C)

        # bracel1 = Brace(line1,direction=line1.copy().rotate(PI / 2).get_unit_vector(),color=ORANGE,buff=0.1)
        
        # c_label = bracel1.get_text("$c$").set_color(BLACK)
        c_label = Tex("$c$",color=BLACK).next_to(line1.get_center(),LEFT)
        c_label2 = Tex("$c$",color=BLACK).next_to(line2.get_center(),DOWN)
        c_label3 = Tex("$c$",color=BLACK).next_to(line3.get_center(),RIGHT)
        c_label4 = Tex("$c$",color=BLACK).next_to(line4.get_center(),UP)

        rightangles1 = RightAngle(line1, line2,stroke_width=4)
        rightangles2 = RightAngle(line3, line2,stroke_width=4,quadrant=(-1,-1))
        rightangles3 = RightAngle(line4, line3,stroke_width=4)
        rightangles4 = RightAngle(line1, line4,stroke_width=4,quadrant=(-1,-1))

        linea1 = Line(A,A+RIGHT*b_length,color=icts_highlight)
        linea2 = Line(C,C+DOWN*b_length,color=icts_highlight)
        linea3 = Line(mA,mA+LEFT*b_length,color=icts_highlight)
        linea4 = Line(-C,-C+UP*b_length,color=icts_highlight)
        a_label = Tex("$a$",color=icts_highlight).next_to(linea1.get_center(),DOWN)
        a_label2 = Tex("$a$",color=icts_highlight).next_to(linea2.get_center(),LEFT)
        a_label3 = Tex("$a$",color=icts_highlight).next_to(linea3.get_center(),UP)
        a_label4 = Tex("$a$",color=icts_highlight).next_to(linea4.get_center(),RIGHT)
    
        lineb1 = Line(A,A+RIGHT*a_length,color=icts_grey)
        b_label = Tex("$b$", color=icts_grey).next_to(lineb1.get_center(),UP)
        lineb2 = Line(C,C+DOWN*a_length,color=icts_grey)
        b_label2 = Tex("$b$", color=icts_grey).next_to(lineb2.get_center(),RIGHT)
        lineb3 = Line(-A,-A+LEFT*a_length,color=icts_grey)
        b_label3 = Tex("$b$", color=icts_grey).next_to(lineb3.get_center(),DOWN)
        lineb4 = Line(-C,-C+UP*a_length,color=icts_grey)
        b_label4 = Tex("$b$", color=icts_grey).next_to(lineb4.get_center(),LEFT)

        rightangles11 = RightAngle(lineb1,linea2,stroke_width=3,quadrant=(-1,-1))
        rightangles22 = RightAngle(lineb4,linea1,stroke_width=3,quadrant=(-1,-1))
        rightangles33 = RightAngle(lineb3,linea4,stroke_width=3,quadrant=(-1,-1))
        rightangles44 = RightAngle(lineb2,linea3,stroke_width=3,quadrant=(-1,-1))

        t1 = Angle(lineb1, line1, radius=0.4,color=icts_grey)
        t2 = Angle(line1, linea2, radius=0.4,color=icts_highlight,quadrant=(-1,1))
        t3 = Angle(linea2,line4,radius=0.4,color=icts_grey,quadrant=(1,-1))
        t4 = Angle(line4,lineb3,radius=0.4,color=icts_highlight)
        t5 = Angle(lineb3,line3,radius=0.4,color=icts_grey)
        t6 = Angle(line3,linea4,radius=0.4,color=icts_highlight,quadrant=(-1,1))
        t7 = Angle(linea4,line2,radius=0.4,color=icts_grey,quadrant=(1,-1))
        t8 = Angle(line2,lineb1,radius=0.4,color=icts_highlight)
        t1_label = MathTex(r"90^{\circ}-\theta",font_size=28,color=icts_grey).next_to(t1,UR,buff=0)
        t2_label = MathTex(r"\theta",font_size=28,color=icts_highlight).next_to(t2,DOWN,buff=0.1)

        csquare = Tex("$c^2$",color=BLACK).shift(DOWN*2.9 + LEFT)

        self.play(FadeIn(triangle),FadeIn(triangle2),FadeIn(triangle3),FadeIn(triangle4),FadeIn(square_In))
        self.wait(1)
        self.play(FadeIn(line1),FadeIn(c_label))
        self.play(FadeIn(line2),FadeIn(c_label2))
        self.play(FadeIn(rightangles1))
        self.play(FadeIn(line3),FadeIn(c_label3))
        self.play(FadeIn(rightangles2))
        self.play(FadeIn(line4),FadeIn(c_label4))
        self.play(FadeIn(rightangles3))
        self.play(FadeIn(rightangles4))
        self.play(FadeOut(rightangles1),FadeOut(rightangles2),FadeOut(rightangles4),FadeOut(rightangles3),ReplacementTransform(c_label,csquare),ReplacementTransform(c_label2,csquare),ReplacementTransform(c_label3,csquare),ReplacementTransform(c_label4,csquare),ReplacementTransform(line1,csquare),ReplacementTransform(line2,csquare),ReplacementTransform(line3,csquare),ReplacementTransform(line4,csquare))
        whole = VGroup(triangle,triangle2,triangle3,triangle4,
                       square_In,
                    #    rightangles1,rightangles2,rightangles4,rightangles3,
                       linea1,linea2,linea3,linea4,
                       a_label,a_label2,a_label3,a_label4,
                       b_label,b_label2,b_label3,b_label4,
                       lineb2,lineb3,lineb1,
                       rightangles11,rightangles44,
                       t2,t1,t3,t4,t5,t6,t7,t8,
                    #    t2_label,t1_label
                       )
        tr = VGroup(triangle4,rightangles44,lineb2,b_label2,t3,t4)
        tr2 = VGroup(triangle,rightangles11,linea2,a_label2,t1,t2)
        # self.add(csquare)
        self.play(FadeIn(rightangles11))
        self.play(FadeIn(t1), FadeIn(t1_label), FadeIn(t2), FadeIn(t2_label))
        # self.play(FadeOut(b_label),FadeOut(a_label2))
        self.play(FadeOut(t1_label),FadeOut(t2_label))
        self.play(Create(linea2))
        self.play(FadeIn(a_label2))
        self.play(Create(lineb1))
        self.play(FadeIn(b_label))
        self.play(Create(linea1),FadeIn(a_label),Create(lineb4),FadeIn(b_label4),FadeIn(rightangles22),FadeIn(t7),FadeIn(t8))
        #3
        self.play(FadeOut(linea1),FadeOut(a_label),FadeOut(lineb4),FadeOut(b_label4),FadeOut(rightangles22),FadeOut(t7),FadeOut(t8),Create(linea4),FadeIn(a_label4),Create(lineb3),FadeIn(b_label3),FadeIn(rightangles33),FadeIn(t5),FadeIn(t6))
        #4
        self.play(FadeOut(linea4),FadeOut(a_label4),FadeOut(lineb3),FadeOut(b_label3),FadeOut(rightangles33),FadeOut(t5),FadeOut(t6),
            Create(linea3),FadeIn(a_label3),Create(lineb2),FadeIn(b_label2),FadeIn(rightangles44),FadeIn(t3),FadeIn(t4))
        self.play(whole.animate.shift(UL*a_length/2))
        self.play(tr.animate.shift(DOWN*b_length+LEFT*a_length))
        self.play(tr2.animate.shift(RIGHT*b_length+DOWN*a_length))
        self.wait(1)
        # self.add(triangle,triangle2,triangle3,triangle4,rightangles1,rightangles2,rightangles4,rightangles3,line1,line2,line3,line4,c_label,c_label2,c_label3,c_label4,linea1,a_label,a_label2,a_label3,a_label4,b_label,lineb2,b_label2,lineb3,b_label3,lineb4,b_label4,rightangles11,t2,t2_label,t1,t1_label,t3,t4,t5,t6,t7,t8)
        # self.wait(2)


        # A = ORIGIN
        # B = A + square_side_length * np.array([np.cos(tilt_angle), np.sin(tilt_angle), 0])
        # C = B + square_side_length * np.array([np.cos(tilt_angle), np.sin(tilt_angle),0])

        # triangle = Polygon(A,B,C)
        # self.play(Create(triangle))q