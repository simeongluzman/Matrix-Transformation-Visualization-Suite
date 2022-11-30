
from manim import *
from manim.opengl import *
import numpy as np

config.frame_width =13
class InteractiveRadius(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(axis_config={"include_numbers": True})
        label_x = axes.get_x_axis_label('x')
        label_y = axes.get_y_axis_label('y')
        label_z = axes.get_z_axis_label('z')

        
        text3d = VGroup(
            Tex("x- rotate 30 deg. around X"),
            Tex("y- rotate 30 deg. around Y"),
            Tex("z- rotate 30 deg. around Z"),
            Tex("p- project matrix onto XY Plane"),
            Tex("g- return to identity cube"),

        ).arrange(DOWN, aligned_edge=LEFT).scale(0.5)
        
        
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(DR)

        cube = Cube(side_length=1)
        cube.move_to([0.5,0.5,0.5])
        cube.set_fill(PINK, opacity=0.5)
        self.cube = cube

        x1 =round(cube.get_all_points()[2][0],2)
        x2 =round(cube.get_all_points()[2][1],2)
        x3 =round(cube.get_all_points()[2][2],2)
        y1 =round(cube.get_all_points()[9][0],2)
        y2 =round(cube.get_all_points()[9][1],2)
        y3 =round(cube.get_all_points()[9][2],2)
        z1 =round(cube.get_all_points()[20][0],2)
        z2 =round(cube.get_all_points()[20][1],2)
        z3 =round(cube.get_all_points()[20][2],2)

        res = [[x1,x2,x3], [y1,y2,y3], [z1,z2,z3]]
        self.res = res
        
        ma = matrix_to_mobject([[x1,x2,x3], [y1,y2,y3], [z1,z2,z3]])
        b1 = Brace(ma[0],DOWN)
        t1 = b1.get_text("Original Matrix")
        form1 = VGroup(ma,b1,t1).scale(0.5)
        form1.to_corner(DL)
        self.add_fixed_in_frame_mobjects(form1)

        
           
        arrowX = Line3D(
            start=cube.get_all_points()[0],
            end=cube.get_all_points()[2],
            thickness=0.04,  
            color = GREEN,
            
        )
        arrowY = Line3D(
            start=cube.get_all_points()[0],
            end=cube.get_all_points()[9],
            thickness=0.04,  
            color = RED,
            
        )
        arrowZ = Line3D(
            start=cube.get_all_points()[0],
            end=cube.get_all_points()[20],
            thickness=0.04,  
            color = BLUE,           
        )
       
        
        self.add(label_x)
        self.add(label_y)
        self.add(label_z)
        self.add(axes)
        self.add(arrowX)
        self.add(arrowY)
        self.add(arrowZ)
    
        self.move_camera(phi = 45*DEGREES,
            theta = -45*DEGREES,
            )
        self.begin_ambient_camera_rotation()
        
        
        self.cube = cube
        self.form1 = form1
        self.res = res
        self.arrowX = arrowX
        self.arrowY = arrowY
        self.arrowZ = arrowZ
        self.interactive_embed()  # not supported in online environment

   


    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key as pyglet_key
        
        if symbol == pyglet_key.G:
            
            cube1 = Cube(side_length=1)
            cube1.move_to([0.5,0.5,0.5])
            cube1.set_fill(PINK, opacity=0.5)
            #self.cube = cube1

            self.play(
                (Transform(self.cube,cube1)),
                self.wait()
              
            )

            self.play(
                (self.arrowX.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[2]), RED),
            self.wait()
              
            
            

            )
            self.play(
                cube1.animate.set_fill(GREEN,opacity=0.5),
                self.wait()
              
            )

            self.play(
                (self.arrowY.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[9])),
            self.wait()
              

            )
            self.play(
                self.arrowY.set_fill(RED,opacity=0.5),
                self.wait()
              
            )

            self.play(
                (self.arrowZ.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[20])),
            self.wait()
              

            )

            m1 = matrix_to_mobject([[1,0,0],[0,1,0],[0,0,1]])
            m1.add_background_rectangle(color=BLACK, opacity=1)
            brace = Brace(m1[0],DOWN)
            self.wait()
              
            
            text = brace.get_text("Cube Matrix")
            form2 = VGroup(m1,brace,text).scale(0.5)
            form2.to_corner(UR)
            self.add_fixed_in_frame_mobjects(form2)
            self.play(
                Create(form2),  
                self.wait()
               
            )


            

        if symbol == pyglet_key.Y:

            tMatrix = matrix_to_mobject([["cos(30)", 0, "sin(30)"], [0, 1, 0], ["-sin(30)", 0, "cos(30)"]])
            b = Brace(tMatrix[0],DOWN)
            t = b.get_text("Transformation Matrix")
            form = VGroup(tMatrix,b,t).scale(0.5)

            form.to_corner(UL)
            self.add_fixed_in_frame_mobjects(form)
            self.play(
                Create(form),
                self.wait()
              
            )

            self.play(
                #[[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]]
                (ApplyMatrix([[0.866025, 0, 0.5], [0, 1, 0], [-0.5, 0, 0.866025]], self.cube)),
                self.wait()
              
                


            )
            self.play(
                (self.arrowX.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[2])),
            self.wait()
              

            )

            self.play(
                (self.arrowY.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[9])),
            self.wait()
              

            )

            self.play(
                (self.arrowZ.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[20])),
            self.wait()
              

            )

           
            #A = [[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]]
            #mat = np.matmul(A,self.res).round(2)
            x1 =round(self.cube.get_all_points()[2][0],2)
            x2 =round(self.cube.get_all_points()[2][1],2)
            x3 =round(self.cube.get_all_points()[2][2],2)
            y1 =round(self.cube.get_all_points()[9][0],2)
            y2 =round(self.cube.get_all_points()[9][1],2)
            y3 =round(self.cube.get_all_points()[9][2],2)
            z1 =round(self.cube.get_all_points()[20][0],2)
            z2 =round(self.cube.get_all_points()[20][1],2)
            z3 =round(self.cube.get_all_points()[20][2],2)
            self.wait()
              

            temp = [[x1,x2,x3], [y1,y2,y3], [z1,z2,z3]]
            
            m1 = matrix_to_mobject(temp)
            m1.add_background_rectangle(color=BLACK, opacity=1)
            brace = Brace(m1[0],DOWN)
            
            text = brace.get_text("Cube Matrix")
            form2 = VGroup(m1,brace,text).scale(0.5)
            form2.to_corner(UR)
            self.add_fixed_in_frame_mobjects(form2)
            self.play(
                Create(form2),   
                self.wait()
              
            )

            self.play(
                Uncreate(form),
                self.wait()
              
            )
            
            
            
        super().on_key_press(symbol, modifiers)
        

        if symbol == pyglet_key.X:

            tMatrix = matrix_to_mobject([[1, 0, 0], [0, "cos(30)", "-sin(30)"], [0, "sin(30)", "cos(30)"]])
            b = Brace(tMatrix[0],DOWN)
            t = b.get_text("Transformation Matrix")
            form = VGroup(tMatrix,b,t).scale(0.5)

            form.to_corner(UL)
            self.add_fixed_in_frame_mobjects(form)
            self.play(
                Create(form)
            )

            self.play(
                #[[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]]
                (ApplyMatrix([[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]], self.cube)),
                


            )
            self.play(
                (self.arrowX.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[2])),

            )

            self.play(
                (self.arrowY.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[9])),

            )

            self.play(
                (self.arrowZ.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[20])),

            )

           
            #A = [[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]]
            #mat = np.matmul(A,self.res).round(2)
            x1 =round(self.cube.get_all_points()[2][0],2)
            x2 =round(self.cube.get_all_points()[2][1],2)
            x3 =round(self.cube.get_all_points()[2][2],2)
            y1 =round(self.cube.get_all_points()[9][0],2)
            y2 =round(self.cube.get_all_points()[9][1],2)
            y3 =round(self.cube.get_all_points()[9][2],2)
            z1 =round(self.cube.get_all_points()[20][0],2)
            z2 =round(self.cube.get_all_points()[20][1],2)
            z3 =round(self.cube.get_all_points()[20][2],2)

            temp = [[x1,x2,x3], [y1,y2,y3], [z1,z2,z3]]
            
            m1 = matrix_to_mobject(temp)
            m1.add_background_rectangle(color=BLACK, opacity=1)
            brace = Brace(m1[0],DOWN)
            
            text = brace.get_text("Cube Matrix")
            form2 = VGroup(m1,brace,text).scale(0.5)
            form2.to_corner(UR)
            self.add_fixed_in_frame_mobjects(form2)
            self.play(
                Create(form2),   
            )

            self.play(
                Uncreate(form)
            )
            
            
            
        super().on_key_press(symbol, modifiers)

        if symbol == pyglet_key.Z:

            tMatrix = matrix_to_mobject([["cos(30)", "-sin(30)", 0], [ "sin(30)", "cos(30)", 0], [0, 0, 1]])
            b = Brace(tMatrix[0],DOWN)
            t = b.get_text("Transformation Matrix")
            form = VGroup(tMatrix,b,t).scale(0.5)

            form.to_corner(UL)
            self.add_fixed_in_frame_mobjects(form)
            self.play(
                Create(form)
            )

            self.play(
                #[[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]]
                (ApplyMatrix([[0.866025, -0.5, 0], [0.5, 0.866025, 0], [0, 0, 1]], self.cube)),
                


            )
            self.play(
                (self.arrowX.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[2])),

            )

            self.play(
                (self.arrowY.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[9])),

            )

            self.play(
                (self.arrowZ.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[20])),

            )

           
            #A = [[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]]
            #mat = np.matmul(A,self.res).round(2)
            x1 =round(self.cube.get_all_points()[2][0],2)
            x2 =round(self.cube.get_all_points()[2][1],2)
            x3 =round(self.cube.get_all_points()[2][2],2)
            y1 =round(self.cube.get_all_points()[9][0],2)
            y2 =round(self.cube.get_all_points()[9][1],2)
            y3 =round(self.cube.get_all_points()[9][2],2)
            z1 =round(self.cube.get_all_points()[20][0],2)
            z2 =round(self.cube.get_all_points()[20][1],2)
            z3 =round(self.cube.get_all_points()[20][2],2)

            temp = [[x1,x2,x3], [y1,y2,y3], [z1,z2,z3]]
            
            m1 = matrix_to_mobject(temp)
            m1.add_background_rectangle(color=BLACK, opacity=1)
            brace = Brace(m1[0],DOWN)
            
            text = brace.get_text("Cube Matrix")
            form2 = VGroup(m1,brace,text).scale(0.5)
            form2.to_corner(UR)
            self.add_fixed_in_frame_mobjects(form2)
            self.play(
                Create(form2),   
            )

            self.play(
                Uncreate(form)
            )
            
            
            
        super().on_key_press(symbol, modifiers)

        if symbol == pyglet_key.P:

            tMatrix = matrix_to_mobject([[1, 0, 0], [ 0, 1, 0], [0, 0, 0]])
            b = Brace(tMatrix[0],DOWN)
            t = b.get_text("Transformation Matrix")
            form = VGroup(tMatrix,b,t).scale(0.5)

            form.to_corner(UL)
            self.add_fixed_in_frame_mobjects(form)
            self.play(
                Create(form)
            )

            self.play(
                #[[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]]
                (ApplyMatrix([[1, 0, 0], [ 0, 1, 0], [0, 0, 0]], self.cube)),
                


            )
            self.play(
                (self.arrowX.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[2])),

            )

            self.play(
                (self.arrowY.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[9])),

            )

            self.play(
                (self.arrowZ.animate.set_start_and_end_attrs(self.cube.get_all_points()[0],
            self.cube.get_all_points()[20])),

            )

           
            #A = [[1, 0, 0], [0, 0.866, -0.5], [0, 0.5, 0.866]]
            #mat = np.matmul(A,self.res).round(2)
            x1 =round(self.cube.get_all_points()[2][0],2)
            x2 =round(self.cube.get_all_points()[2][1],2)
            x3 =round(self.cube.get_all_points()[2][2],2)
            y1 =round(self.cube.get_all_points()[9][0],2)
            y2 =round(self.cube.get_all_points()[9][1],2)
            y3 =round(self.cube.get_all_points()[9][2],2)
            z1 =round(self.cube.get_all_points()[20][0],2)
            z2 =round(self.cube.get_all_points()[20][1],2)
            z3 =round(self.cube.get_all_points()[20][2],2)

            temp = [[x1,x2,x3], [y1,y2,y3], [z1,z2,z3]]
            
            m1 = matrix_to_mobject(temp)
            m1.add_background_rectangle(color=BLACK, opacity=1)
            brace = Brace(m1[0],DOWN)
            
            text = brace.get_text("Cube Matrix")
            form2 = VGroup(m1,brace,text).scale(0.5)
            form2.to_corner(UR)
            self.add_fixed_in_frame_mobjects(form2)
            self.play(
                Create(form2),   
            )

            self.play(
                Uncreate(form)
            )
            
            
            
        super().on_key_press(symbol, modifiers)