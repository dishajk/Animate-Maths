# manim -pql mathsCircle.py mathsCircle

from manim import *
from manim import XKCD
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
        
        text = [Text("Organising Team",font_size=24).move_to(1.5*DOWN),
                Text("Organising Team reaches out to potential leads for the session",font_size=24).move_to(2.5*DOWN),
                Text("A lead is found at least a month before the session", font_size=24).move_to(1.75*DOWN),
                Text("This gives the lead time to observe a session,\n" "understand the students, and prepare an exploration sheet.",font_size=24).move_to(2.5*DOWN),
                Text("The students recieve the exploration sheet about a week before the session.", font_size=24).move_to(2.5*DOWN),
                Text("Maths Circle Students",font_size=24,color=GREEN).move_to(3*UP+2*RIGHT)]
        
        reach = VGroup()
        for i in range(4):
            reach_line = Line(organisers[i].get_center(),[0,0,0])
            reach_line.rotate(180*DEGREES,about_point=organisers[i].get_center())
            reach.add(reach_line)

        potential_leads = VGroup()
        for i in range(4):
            lead_pos = reach[i].get_end()
            dir = [UP,RIGHT,LEFT,DOWN]
            for j in range (3):
                if i < 2:
                    lead = Square(side_length=0.4,fill_color=XKCD.BRIGHTPINK,fill_opacity=1).next_to(lead_pos,direction=dir[j])
                else: 
                    lead = Square(side_length=0.4,fill_color=XKCD.BRIGHTPINK,fill_opacity=1).next_to(lead_pos,direction=dir[j+1])
                lead.rotate(i*j*10*DEGREES)
                potential_leads.add(lead)
        
        tables = VGroup()
        table_pos = [[-2,0,0],[-0.5,2,0],[1.5,1,0]]
        for i in range(3):
            table = Circle(radius=0.75,fill_color=XKCD.BLUEGREY,fill_opacity=1).move_to(table_pos[i])
            tables.add(table)
        grid = NumberPlane()
        # self.add(grid)
        stud_colors = [XKCD.LIGHTAQUA,XKCD.LIGHTERGREEN,XKCD.LIGHTFORESTGREEN,XKCD.LIGHTGRASSGREEN]
        stud_pos=[8* np.pi/25, np.pi/3,2*np.pi/5]
        students = VGroup()
        for i in range(3):
            for j in range(5):
                stud_dir = Line(table_pos[i],table_pos[i]+RIGHT).rotate(j *stud_pos[i]+i*np.pi/18,about_point=tables[i].get_center())
                stud = RegularPolygon(n=5,fill_color=stud_colors[(i+j)%4],fill_opacity=1).set_height(0.5).move_to(stud_dir.get_end())
                students.add(stud)

        lead_path = ArcPolygon([0,-1,0],[-3,-1,0],[-3,1.5,0],[0,3.5,0],[3,1,0],arc_config=[{'radius':-4},{'radius':-4},{'radius':-4},{'radius':-4},{'radius':-4}])
        # self.add(lead_path)

        # Organisers appear
        self.play(*[FadeIn(org_tri) for org_tri in organisers])
        self.play(FadeIn(text[0]))
        self.wait(1)
        self.play(FadeOut(text[0]))
        self.wait(1)

        # Organising team reaches out
        self.play(*[Create(reach_line) for reach_line in reach])
        # potential leads appear
        self.play(*[FadeIn(lead) for lead in potential_leads])
        self.play(FadeIn(text[1]))
        self.wait(2)
        self.play(FadeOut(text[1]))
        self.wait(1)
        self.play(*[FadeOut(reach_line) for reach_line in reach],*[FadeOut(lead) for i, lead in enumerate(potential_leads) if i != 7])
        self.play(FadeIn(text[2]))
        self.wait(2)
        self.play(FadeOut(text[2]))
        self.wait(1)
        # Some Organisers move to left top corner
        self.play(*[org.animate.shift([-5,2,0] - organisers[2].get_center())for i, org in enumerate(organisers)
        if i not in [2, 3]
        ],potential_leads[7].animate.move_to(lead_path.get_start()))
        self.wait(1)
        
        self.play(FadeIn(text[5]),*[FadeIn(stud) for stud in students])
        self.wait(2)
        self.play(FadeOut(text[5]),FadeIn(text[3]),*[FadeIn(table) for table in tables])
        self.wait(2)
        self.play(MoveAlongPath(potential_leads[7],lead_path,rate_func=rate_functions.double_smooth,run_time=15), organisers[3].animate(run_time=8,rate_func=rate_functions.there_and_back_with_pause).move_to([0,1,0]),
        students[0].animate(run_time=2,rate_func=rate_functions.there_and_back_with_pause).next_to(students[12],direction=DOWN),
        students[8].animate(run_time=3,rate_func=rate_functions.there_and_back_with_pause,lag_ratio=0.5).next_to(students[2],direction=LEFT))
        self.wait(3)
        self.play(FadeOut(text[3]))
        self.wait(1)
        self.play(FadeIn(text[4]),*[FadeOut(organiser) for organiser in organisers],*[FadeOut(table) for table in tables])
        self.wait(3)

        

