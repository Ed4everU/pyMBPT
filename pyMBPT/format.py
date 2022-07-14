import logging
from textwrap import TextWrapper

_output_width_ = 70


class Format(logging.Formatter):

    def __init__(
        self, fmt=None, datefmt=None, style="%", width=_output_width_
    ):
        super.__init__(fmt, datefmt, style, width)
        self.wrapper = TextWrapper(
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

        return text
