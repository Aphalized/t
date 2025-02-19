from manim import *
from manim_slides import Slide

greek = TexTemplate(tex_compiler="xelatex", output_format=".xdv")
greek.add_to_preamble(r"""
\usepackage{fontspec}
\setmainfont{Times_New_Roman}
\usepackage{polyglossia}
\setdefaultlanguage{greek}
""")

class Introduction(Slide):
    def construct(self):
        Title = Text("Τριγωνομετρική απόδειξη του", line_spacing=1, font_size=40).shift(UP*1)
        self.play(FadeIn(Title))
        Title2 = Text("Πυθαγορείου Θεωρήματος", line_spacing=1, font_size=60)
        Title2.set_color_by_gradient(BLUE, LIGHT_PINK, RED)
        self.wait(2)
        self.play(Write(Title2), run_time=3)
        self.wait(2)
        self.play(FadeOut(Title, Title2))
        self.wait(2)

class WithTeX(Slide):
    def construct(self):
# Define the vertices of the triangle
        B = DOWN * 3 + LEFT * 5  # Bottom-left corner
        C = DOWN * 3 + RIGHT * 5  # Bottom-right corner
        A = UP * 3 + LEFT * 5  # Top-left corner
        # Create the triangle
        triangle = Polygon(A, B, C, color=WHITE)
        # Label the vertices
        label_A = Text("Α").next_to(A, UL, buff=0.2)
        label_B = Text("Β").next_to(B, DL, buff=0.2)
        label_C = Text("Γ").next_to(C, DR, buff=0.2)
        # Add the triangle to the scene
        self.play(Create(triangle))
        # Add the 90-degree angle label
        right_angle_marker = RightAngle(Line(B, C), Line(B, A), length=0.4)

        self.play(Create(right_angle_marker))

        # Add vertex labels to the scene
        self.play(Write(label_A), run_time=0.5)
        self.play(Write(label_B), run_time=0.5)
        self.play(Write(label_C), run_time=0.5)
        self.wait(2)
        # Label the sides
        label_a = MathTex(r"\alpha").next_to(Line(A, B).get_midpoint(), LEFT, buff=0.2).scale(1.5)
        label_b = MathTex(r"\beta").next_to(Line(B, C).get_midpoint(), DOWN, buff=0.2).scale(1.5)
        label_c = MathTex(r"\gamma").next_to(Line(C, A).get_midpoint(), UR, buff=0.2).scale(1.5)
        self.play(Write(label_a), run_time=0.5)
        self.play(Write(label_b), run_time=0.5)
        self.play(Write(label_c), run_time=0.5)
        # Group the triangle, labels, and angle marker
        group = VGroup(triangle, label_A, label_B, label_C, label_a, label_b, label_c, right_angle_marker)
        self.wait(2)
        # Shrink the triangle and labels with respect to point A
        self.play(group.animate.scale(0.7, about_point=B))
        label_b.save_state()
        label_c.save_state()
        label_a.save_state()
        Hmitono = Text(r"Ο λόγος που σχηματίζεται, αν διαιρέσουμε την " r"απέναντι κάθετη" r" πλευρά", font_size=25).shift(UP * 3)
        Hmitono1 = Text(r"μίας οξείας γωνίας ω ενός ορθογωνίου τριγώνου με την " r"υποτείνουσα" r",", font_size=25).shift(UP * 2.5)
        Hmitono2 = Text(r"είναι πάντοτε σταθερός και λέγεται " r"ημίτονο " r"της γωνίας ω", font_size=25).shift(UP * 2)
        Hmitono2[30:37].set_color(YELLOW)
        Hmitono1[44:55].set_color(RED)
        Hmitono[38:52].set_color(BLUE)
        self.play(Write(Hmitono))
        self.play(Write(Hmitono1))
        self.play(Write(Hmitono2))
        # Wait for a while
        self.wait(2)

            # Highlight and isolate important words
        important_words = VGroup(
            Hmitono2[30:37],
            Hmitono[38:52],
            Hmitono1[44:55]
        )
        # Create a group animation
        animations = AnimationGroup(
            Hmitono.animate.set_opacity(0),
            Hmitono1.animate.set_opacity(0),
            Hmitono2.animate.set_opacity(0),
            *[word.animate.set_opacity(1).scale(1.5) for word in important_words],
            lag_ratio=0.0  # Synchronous animation
        )

        # Play the group animation
        self.play(animations)
        # Create the equation manually
        sin_text = Text("ημίτονο", font_size=30, color=YELLOW).shift(UP * 2.5 + LEFT * 2.5)
        equal_sign = Text("=", font_size=30).next_to(sin_text)

        # Create numerator and denominator
        numerator = Text("απέναντι κάθετη", font_size=30, color=BLUE).next_to(equal_sign, RIGHT * 0.7 + UP * 0.3)
        denominator = Text("υποτείνουσα", font_size=30, color=RED).next_to(numerator, DOWN, buff=0.3)

        # Draw the fraction line
        fraction_line = Line(
            numerator.get_bottom(),
            denominator.get_top(),
            color=WHITE
        ).scale(12, about_edge=LEFT).rotate(PI * 0.5)

        # Group equation elements
        equation_group = VGroup(sin_text, numerator, denominator)

        # Animate transformation into the equation
        self.play(
            ReplacementTransform(important_words, equation_group), run_time=1)
        self.play(
            Write(equal_sign),
            Create(fraction_line)
        )
        groupp = VGroup(equation_group, equal_sign, fraction_line)
        self.play(Circumscribe(groupp))
        self.wait(2)

        angleexample = Angle(Line(A, B), Line(A, C), color=YELLOW).scale(0.7, about_point=B)
        angleexamplelabel = Text("ω", color=YELLOW).next_to(angleexample).scale(0.7).shift(DOWN * 0.4 + LEFT * 0.4)
        exhm = MathTex(r"\eta \mu \omega = \ ").shift(RIGHT * 2)
        exhm1 = MathTex(r"\frac{\beta}{\gamma}").next_to(exhm)
        exhm[0][2].set_color(YELLOW)
        exhm1[0][0].set_color(BLUE)
        exhm1[0][2].set_color(RED)
        self.play(Create(angleexample), Write(angleexamplelabel))
        self.play(Write(exhm[0]))
        self.wait(2)
        self.play(label_b.animate.set_color(BLUE))
        self.wait(2)
        self.play(label_c.animate.set_color(RED))
        groupationingmings = VGroup(label_b, label_c)
        self.play(ReplacementTransform(groupationingmings.copy(), exhm1))
        grouppppp = VGroup(exhm1, exhm)
        self.play(Circumscribe(grouppppp))
        self.wait(2)
        # Fade out the last equation
        self.play(FadeOut(exhm1), Restore(label_c), Restore(label_b), Uncreate(angleexample))
        aangleexample = Angle(Line(C, A), Line(C, B), color=YELLOW).scale(0.7, about_point=B)
        aangleexamplelabel = Text("ω", color=YELLOW).next_to(aangleexample).scale(0.7).shift(UP * 0.1 + LEFT * 1)
        aexhm1 = MathTex(r"\frac{\alpha}{\gamma}").next_to(exhm)
        aexhm1[0][0].set_color(BLUE)
        aexhm1[0][2].set_color(RED)
        self.play(Create(aangleexample), ReplacementTransform(angleexamplelabel, aangleexamplelabel))
        self.wait(2)
        self.play(label_a.animate.set_color(BLUE))
        self.wait(2)
        self.play(label_c.animate.set_color(RED))
        agroupationingmings = VGroup(label_a, label_c)
        self.play(ReplacementTransform(agroupationingmings.copy(), aexhm1))
        agrouppppp = VGroup(aexhm1, exhm)
        self.play(Circumscribe(agrouppppp))
        self.wait(2)
        # Fade out
        self.play(FadeOut(agrouppppp), FadeOut(groupp), FadeOut(label_a), FadeOut(label_c), FadeOut(label_b), Uncreate(aangleexample), FadeOut(aangleexamplelabel), Uncreate(right_angle_marker), FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), Uncreate(triangle))


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
