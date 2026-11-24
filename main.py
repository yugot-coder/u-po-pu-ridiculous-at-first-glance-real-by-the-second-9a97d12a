"""Ridiculous at First Glance, Real by the Second.

Writes one sentence, at most 200 characters, to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt): a pitch
for a bizarre startup idea that sounds absurd until you realise it
would actually sell.

The entry:

    We sell naming rights to potholes: sponsors pay $200 to brand
    the crater outside your house, and the city finally fills it
    with the ad money instead of your taxes.

Why this sentence (reasoning, kept here and in the README; the entry
itself is just the one sentence):

* It is a bizarre startup pitch, not a familiar business with a
  strange adjective bolted on. Nobody sells naming rights to
  potholes; the premise sounds like a joke on first hearing.
* The business logic survives the second look, in the sentence's
  own words: sponsors pay $200 for hyperlocal branding on a crater
  every neighbour already stares at, and the city gets the repair
  paid for with ad money instead of taxes. The payer, the price
  and the mechanism are all named, so a reader can see the
  customers and the money.
* It lands as a pitch: one sentence, 163 characters, with the turn
  from laughing ("brand the crater outside your house") to nodding
  ("fills it with the ad money instead of your taxes").
* It is concrete and vivid: the thing sold (naming rights to
  potholes), who buys it (sponsors), and why it holds together
  (advertising funds road repair) -- no abstractions.

Candidates weighed and set aside: hired stand-ins for awkward
family dinners (clear payer, but the body-double premise is a
familiar comedy trope, less genuinely bizarre); tiny funerals for
dead houseplants (vivid, but the market is a novelty gift, so the
business logic is thinner); break-up texts in the voice of a
Victorian poet (novel and vivid, but one-sided gig work, no
recurring mechanism); renting out vetted grandmothers (the
rent-a-family concept already exists, so it reads familiar);
professional mourners for hire (a real business already, not a
new idea); rain sounds from your childhood roof (a sleep-sounds
app with a strange adjective -- exactly what criterion 2 rules
out); apology notes by pigeon (funny premise, but no clear reason
a pigeon beats a courier, so the logic does not hold).

Standard library only. Deterministic: no randomness, no network, no
clock, no files read. The entry is exactly 163 characters, one
sentence ending in a single period, with no trailing newline.
"""

import os

ENTRY = (
    "We sell naming rights to potholes: sponsors pay $200 to brand "
    "the crater outside your house, and the city finally fills it "
    "with the ad money instead of your taxes."
)

# Gate from the rules: /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space, holding one sentence.
MAX_CHARS = 200


def validate_entry(value) -> str:
    """Guard: value must be the intended one-sentence entry.

    Accepts either the entry string or the raw bytes read back from
    the entry file, so the same check covers the pre-write guard and
    the post-write read-back verification. Returns the entry as a
    str, or raises AssertionError with a clear message.
    """
    if isinstance(value, bytes):
        text = value.decode("utf-8")
    else:
        text = value
    assert isinstance(text, str), f"entry must be text, got {type(text)}"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1 to {MAX_CHARS} characters, got {len(text)}"
    )
    assert text.strip(), "entry must not be only white space"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence ending in a single period"
    )
    assert text == ENTRY, "entry does not match the intended sentence"
    return text


def main() -> None:
    # Pre-write guard: refuse to write anything but the intended
    # one-sentence, 1-to-200-character entry.
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back validation: the gate is 1 to 200 characters of UTF-8
    # text, so the file must decode as UTF-8, hold exactly the
    # intended sentence, and be byte-identical to it.
    with open(path, "rb") as f:
        data = f.read()
    assert validate_entry(data) == ENTRY
    assert data == ENTRY.encode("utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
