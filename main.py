from manim import *

class algebra(Scene):
    def construct(self):
        # 1. Setup Symbols (Using Text to bypass LaTeX requirement)
        inf_sym = Text("∞", color=BLUE).scale(5)
        omega_sym = Text("Ω", color=GOLD).scale(5)
        name_text = Text("InfiniO", font="Sans", weight=BOLD).scale(1.5)

        # Positioning
        name_text.next_to(omega_sym, DOWN, buff=0.8)
        intro_group = VGroup(omega_sym, name_text).center()

        # 2. Intro Animation
        self.play(Write(inf_sym), run_time=1.5)
        self.wait(0.5)

        self.play(
            ReplacementTransform(inf_sym, omega_sym),
            FadeIn(name_text, shift=UP),
            run_time=2.5,
            rate_func=slow_into
        )

        # 3. Logo "Pulse" Effect
        self.play(
            omega_sym.animate.set_stroke(width=10),
            name_text.animate.set_color(GOLD),
            run_time=1
        )
        self.play(
            omega_sym.animate.set_stroke(width=4),
            run_time=1
        )
        self.wait(0.1)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        seta = Text("Set : {1}")
        seta.to_edge(UP, buff = 0.5)
        self.play(Write(seta))
        closed = Paragraph(
            "+ → No! [1+1=2]\n"
            "- → No! [1-1=0]\n"
            "× → Yes!\n"
            "÷ → Yes!",
            t2c = {"No!": RED, "Yes!": GREEN},
            alignment = "left",
            line_spacing = 0.8
        )
        closed.to_edge(DOWN, buff=0.5)
        self.play(Write(closed))
        self.wait()