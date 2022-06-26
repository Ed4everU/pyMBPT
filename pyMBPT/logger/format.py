import logging
import textwrap

## adopted from AMSET


class WrapperFormatter(logging.Formatter):

    def __init__(
        self, fmt=None, datefmt=None, style="%", width=100, simple_ascii=False
    ):

        super().__init__(fmt=fmt, datefmt=datefmt, style=style)
        self.simple_ascii = simple_ascii
        self.wrapper = textwrap.TextWrapper(
            width=width,
            subsequent_indent="  ",
            replace_whitespace=True,
            drop_whitespace=False,
        )

    def format(self, record):
        text = super().format(record)
        if "└" in text or "├" in text:
            # don't have blank time when reporting list
            text = "  " + text
        else:
            text = "\n" + "\n".join(
                [self.wrapper.fill("  " + s) for s in text.splitlines()]
            )

        if self.simple_ascii:
            return self.make_simple_ascii(text)

        return text

    @staticmethod
    def make_simple_ascii(text):
        replacements = {
            "├──": "-",
            "│": " ",
            "└──": "-",
            fancy_logo: simple_logo,
            "ᵢᵢ": "_i",
            "ħω": "hbar.omega",
            "cm²/Vs": "cm2/Vs",
            "β²": "b2",
            "a₀⁻²": "a^-2",
            "cm⁻³": "cm-3",
            "–": "-",
            "₀": "0",
            "₁": "1",
            "₂": "2",
            "₃": "3",
            "₄": "4",
            "₅": "5",
            "₆": "6",
            "₇": "7",
            "₈": "8",
            "₉": "8",
            "\u0305": "-",
            "π": "pi",
            "ħ": "h",
            "ω": "w",
            "α": "a",
            "β": "b",
            "γ": "y",
            "°": "deg",
            "Å": "angstrom",
        }

        for initial, final in replacements.items():
            text = text.replace(initial, final)
        return text