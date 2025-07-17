# smallfont.py
SMALL_DIGITS = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄",
    "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉",
    ":": ":"
}

def to_small(text: str) -> str:
    return "".join(SMALL_DIGITS.get(ch, ch) for ch in text)
  
