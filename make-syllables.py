from typing import Generator, Iterable, IO
from io import open

(M, P, B, F, V) = ("м", "п", "б", "ф", "в")
(N, T, D, S, Z, TS, DZ, L) = ("н", "т", "д", "с", "з", "ц", "ѕ", "л")
(SH, ZH, TSH, DZH) = ("ш", "ж", "ћ", "ђ")
(NG, K, G, H) = ("ӈ", "к", "г", "х")
(I, E, A, O, U) = ("и", "е", "а", "о", "у")
(Y, W) = ( "й", "ў" )

VOWELS = [ I, E, A, O, U ]

PHONOTACTICS = [
    (M, True, False),
    (P, True, False),
    (B, True, False),
    (F, True, False),
    (V, True, False),
    (N, True, False),
    (T, False, False),
    (D, False, False),
    (S, False, False),
    (Z, False, False),
    (TS, False, False),
    (DZ, False, False),
    (L, True, False),
    (SH, False, False),
    (ZH, False, False),
    (TSH, False, False),
    (DZH, False, False),
    (NG, True, True),
    (K, True, True),
    (G, True, True),
    (H, True, True),
    (" ", True, True)
]

def can_prefix_y(vowel: str) -> bool:
    return vowel != I

def can_prefix_w(vowel: str) -> bool:
    return vowel != U

def can_suffix_y(syllable: str) -> bool:
    return syllable[-1] in (E, A, O) and syllable.find(Y) < 0 and syllable.find(W) < 0

def can_suffix_w(syllable: str) -> bool:
    return syllable[-1] in (E, A, O) and syllable.find(Y) < 0 and syllable.find(W) < 0

def make_suffix_parts(body: str) -> Generator[str, None, None]:
    yield body

    if can_suffix_y(body):
        yield body + Y
    
    if can_suffix_w(body):
        yield body + W

def make_vowel_parts(consonant: str, allow_y: bool, allow_w: bool) -> Generator[str, None, None]:
    for v in VOWELS:
        yield from make_suffix_parts(consonant + v)
        
    if allow_y:
        for v in VOWELS:
            if can_prefix_y(v):
                yield from make_suffix_parts(consonant + Y + v)
    
    if allow_w:
        for v in VOWELS:
            if can_prefix_w(v):
                yield from make_suffix_parts(consonant + W + v)

def make_syllables() -> Generator[str, None, None]:
    for (c, y, w) in PHONOTACTICS:
        yield from make_vowel_parts(c, y, w)

def print_syllables(f: IO):
    count = 0
    for (c, y, w) in PHONOTACTICS:
        syllables = list(make_vowel_parts(c, y, w))
        count += len(syllables)
        syllables_str = " ".join(syllables)

        f.write(syllables_str + "\n")
        print(syllables_str)

    print(f"{count} items found")

with open("awsha-syllables.txt", "w") as f:
    print_syllables(f)
