from manim import *


class t(Scene):
    def construct(self):
        
        plane = NumberPlane(
        axis_config={"include_numbers": True, "include_tip": True
        }
        )

        label = plane.get_axis_labels(
        x_label=MathTex(r"\\x"), 
        y_label=MathTex(r"\\y")
        )

        self.add(plane, label)
        self.wait(1.5)

        circle = Circle(
        radius=1,
        color=RED_C,
        fill_opacity=0.5
        )
        circle.move_to([0, 0, 0])

        self.play(GrowFromCenter(circle), run_time=2)
        self.wait(1.5)
        self.play(ShrinkToCenter(circle))

        ellipse = Ellipse(
        width=2,
        height=1,
        color=GREEN_C,
        fill_opacity=0.5
        )
        ellipse.move_to([0, 0, 0])

        self.play(Transform(circle, ellipse))
        self.wait(1.5)
        self.play(ShrinkToCenter(circle))

        hyperbole = ImplicitFunction(
        lambda x, y: x**2 - y**2 -4,
        color=BLUE_C
        )

        self.play(Transform(circle, hyperbole))
        self.wait(1.5)
        self.play(ShrinkToCenter(circle))

        def func(x):
            return 0.3*(x)**2 -1
        parabole = plane.plot(func,
        color=YELLOW_C
        )

        dot = Dot()

        self.play(Transform(circle, parabole))
        self.wait(1.5)
        self.play(Transform(circle, dot))

        self.play(FadeOut(circle, plane, label))

        logo = ManimBanner()

        self.play(logo.create())
        self.play(logo.expand())
        self.wait(1)
        self.play(Unwrite(logo))
        self.wait(1)
