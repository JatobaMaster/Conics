from manim import *

class Cônicas(Scene):
    def construct(self):

        plano_cartesiano = NumberPlane(axis_config={"include_numbers": True, "include_tip": True})
        legenda = plano_cartesiano.get_axis_labels(x_label=MathTex(r"\\x"), y_label=MathTex(r"\\y"))

        ponto = Dot()
        ponto.move_to([0, 0, 0])

        circulo = Circle(radius=2, color=WHITE, fill_opacity=0.5)
        circulo.move_to([0, 0, 0])

        elipse = Ellipse(width=4, height=2, color=WHITE, fill_opacity=0.5)
        elipse.move_to([0, 0, 0])

        hipérbole = ImplicitFunction(lambda x, y: x**2 - y**2 -4, color=WHITE)

        def func(x):
            return 0.3*(x)**2 -1
        parábola = plano_cartesiano.plot(func, color=WHITE) 

        logo = ManimBanner()

        self.wait(1)
        self.play(Create(plano_cartesiano), run_time=2)
        self.play(Write(legenda))
        self.play(GrowFromCenter(circulo), run_time=2)
        self.wait(1)
        self.play(Transform(circulo, ponto))
        self.play(Transform(circulo, elipse), run_time=2)
        self.wait(1)
        self.play(Transform(circulo, ponto))
        self.play(Transform(circulo, hipérbole), run_time=2)
        self.wait(1)
        self.play(Transform(circulo, ponto))
        self.play(Transform(circulo, parábola), run_time=2)
        self.wait(1)
        self.play(FadeOut(plano_cartesiano, legenda, circulo))
        self.play(logo.create())
        self.play(logo.expand())
        self.wait(1)
        self.play(Unwrite(logo))
        self.wait(1)
