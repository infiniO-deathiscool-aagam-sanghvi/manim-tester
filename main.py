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
        targetc = Paragraph(
            "+ → No! [1+2=3]\n"
            "- → No! [1-1=0]\n"
            "× → No! [2×2=4]\n"
            "÷ → No! [1÷2=0.5]",
            t2c = {"No!": RED, "Yes!": GREEN},
            alignment = "left",
            line_spacing = 0.8
        ).to_edge(DOWN,buff=0.5)
        targets = Text("Set : {1,2}").to_edge(UP,buff=0.5)
        self.play(ReplacementTransform(seta,targets),ReplacementTransform(closed,targetc))
        self.wait(6)
        seta = targets
        closed = targetc
        targets = Text("Set : {1,2...}").to_edge(UP,buff=0.5)
        targetc = Paragraph(
            "+ → Yes!\n"
            "- → No! [1-1=0]\n"
            "× → Yes!\n"
            "÷ → No! [1÷2=0.5]",
            t2c = {"No!": RED, "Yes!": GREEN},
            alignment = "left",
            line_spacing = 0.8
        ).to_edge(DOWN,buff=0.5)
        self.play(ReplacementTransform(seta,targets),ReplacementTransform(closed,targetc))
        self.wait(5)
        seta = targets
        closed = targetc
        targets = Text("Set : {0,1,2...}").to_edge(UP,buff=0.5)
        targetc = Paragraph(
            "+ → Yes!\n"
            "- → No! [0-1=-1]\n"
            "× → Yes!\n"
            "÷ → No! [1÷2=0.5]",
            t2c = {"No!": RED, "Yes!": GREEN},
            alignment = "left",
            line_spacing = 0.8
        ).to_edge(DOWN,buff=0.5)
        self.play(ReplacementTransform(seta,targets),ReplacementTransform(closed,targetc))
        self.wait(3)
        seta = targets
        closed = targetc
        targets = Text("Set : {...-1,0,1,2...}").to_edge(UP,buff=0.5)
        targetc = Paragraph(
            "+ → Yes!\n"
            "- → Yes!\n"
            "× → Yes!\n"
            "÷ → No! [1÷2=0.5]",
            t2c = {"No!": RED, "Yes!": GREEN},
            alignment = "left",
            line_spacing = 0.8
        ).to_edge(DOWN,buff=0.5)
        self.play(ReplacementTransform(seta,targets),ReplacementTransform(closed,targetc))
        self.wait(2)
        # --- PREVIOUS STATE: Integers ---
        seta = targets
        closed = targetc

        # 1. RATIONAL NUMBERS (Quotient Closure)
        # "And we go smaller and smaller..."
        targets = Text("Set : Rational Numbers (Q)").to_edge(UP, buff=0.5)
        targetc = Paragraph(
            "+ → Yes!\n"
            "- → Yes!\n"
            "× → Yes!\n"
            "÷ → Yes!",
            t2c = {"No!": RED, "Yes!": GREEN},
            alignment = "left",
            line_spacing = 0.8
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(seta, targets), ReplacementTransform(closed, targetc))
        self.wait(3)

        seta, closed = targets, targetc

        targets = Text("Set : Algebraic Numbers (A)").to_edge(UP, buff=0.5)
        targetc = Paragraph(
            "+ → Yes!\n"
            "- → Yes!\n"
            "× → Yes!\n"
            "÷ → Yes!\n"
            "^ → Yes! (Including fractional exponents)",
            t2c = {"No!": RED, "Yes!": GREEN, "Including fractional exponents": BLUE},
            alignment = "left",
            line_spacing = 0.8
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(seta, targets), ReplacementTransform(closed, targetc))
        self.wait(3)

        seta, closed = targets, targetc
        targets = Text("Set : R(Reals)").to_edge(UP, buff=0.5)
        targetc = Paragraph(
            "+ → Yes!\n"
            "- → Yes!\n"
            "× → Yes!\n"
            "÷ → Yes!\n"
            "^ → Yes!\n"
            "lim → Yes!",
            t2c = {"No!": RED, "Yes!": GREEN},
            alignment = "left",
            line_spacing = 0.8
        ).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(seta, targets), ReplacementTransform(closed, targetc))
        self.wait(4)
        seta, closed = targets, targetc
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        sus = Text("But are they actually closed?")
        self.play(Write(sus))
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.play(Write(Text("√-1",color=BLUE)))
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        self.wait(2)
        self.play(Write(seta))
        closed=Paragraph(
            "+ → Yes!\n"
            "- → Yes!\n"
            "× → Yes!\n"
            "÷ → Yes!\n"
            "^ → No! [-1^0.5=?]\n"
            "lim → Yes!",
            t2c = {"No!": RED, "Yes!": GREEN},
            alignment = "left",
            line_spacing = 0.8
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(closed))
        self.play(Write(Text("But what is the √-1?",t2c = {"-1":RED,"√":BLUE})))
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        # --- CUSTOM NUMBER LINE WITHOUT LATEX ---
        # 1. Create the main horizontal line
        line = Line(LEFT * 5, RIGHT * 5, color=WHITE)
        
        # 2. Add arrows to the ends
        line.add_tip(tip_shape=StealthTip) 

        # 3. Create ticks and labels manually
        ticks = VGroup()
        labels = VGroup()

        for x in range(-4, 5):  # From -4 to 4
            # Create a small vertical line for each tick
            tick = Line(UP * 0.1, DOWN * 0.1).move_to(line.point_from_proportion((x + 5) / 10))
            ticks.add(tick)
            
            
            label = Text(str(x), font_size=24).next_to(tick, DOWN, buff=0.2)
            labels.add(label)

        number_line_group = VGroup(line, ticks, labels).center()

        self.play(Create(line))
        self.play(Create(ticks), Write(labels))
        self.wait(2)
        start_x = -5
        end_x = 5
        dots_per_unit = 15 
        total_dots = int((end_x - start_x) * dots_per_unit)

        # Create the dots using a list comprehension
        # We use Dot(radius=0.04) or SmallDot() for a cleaner look
        dot_line = VGroup(*[
            Dot(
                point=[x, 0, 0], 
                color=WHITE
            ) 
            for x in np.linspace(start_x, end_x, total_dots)
        ])

        # Animate the creation (LaggedStart makes it look like it's drawing)
        self.play(
            LaggedStart(
                *[Create(d) for d in dot_line], 
                lag_ratio=0.01, 
                run_time=3
            )
        )
        self.wait(1)

        # EXAMPLE: How to animate them through a function later
        # Let's move them into a Sine wave
        self.play(
            dot_line.animate.apply_function(
                lambda p: [p[0], np.sin(p[0]), p[2]]
            ),
            run_time=2
        )
        self.wait(2)