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

        # 4. Transition to Identities
        self.play(
            intro_group.animate.scale(3).set_opacity(0), 
            rate_func=lambda t: t**2,
            run_time=1
        )
        self.remove(intro_group) 

        # 5. Trigonometry Section (Text based math)
        eq1 = Text("cos(a + b) = cos a cos b - sin a sin b").shift(UP).scale(0.7)
        eq2 = Text("sin(a + b) = sin a cos b + cos a sin b").shift(DOWN).scale(0.7)
        identities = VGroup(eq1, eq2)
        
        self.play(Write(eq1), Write(eq2))
        
        rect = SurroundingRectangle(identities, color=RED)
        why_text = Text("Why?", font="Sans").scale(0.8).next_to(identities, DOWN, buff=0.5)
        
        self.play(Create(rect), Write(why_text))
        self.play(Indicate(why_text, color=RED, scale_factor=1.2))
        self.wait(1)
        
        # 6. Chapter 1 Transition
        self.play(FadeOut(identities), FadeOut(rect), FadeOut(why_text))
        
        chapter_title = Text("Chapter 1: Negative Square Roots", font="Sans").scale(1.2)
        self.play(Write(chapter_title), run_time=1.5)
        self.wait(1)

        # 7. Number Line Animation (Forcing Text labels to avoid LaTeX error)
        number_line = NumberLine(
            x_range=[-7, 7, 1],
            length=10,
            include_numbers=True,
            label_direction=DOWN,
            label_constructor=Text  # This bypasses the 'latex' FileNotFoundError
        )

        self.play(ReplacementTransform(chapter_title, number_line))
        
        # Create dots for integers -7 to 7
        dots = VGroup(*[Dot(number_line.number_to_point(i), color=YELLOW) for i in range(-7, 8)])
        self.play(FadeIn(dots, lag_ratio=0.1))
        self.wait(1)

        # 8. Square Logic Animation
        animations = []
        for i, dot in zip(range(-7, 8), dots):
            # Map each integer to its square (i -> i^2)
            target_point = number_line.number_to_point(i**2)
            arc_path = ArcBetweenPoints(dot.get_center(), target_point, angle=-PI/2)
            animations.append(MoveAlongPath(dot, arc_path))

        self.play(*animations, run_time=2)
        self.wait(2)