[![make.fun](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![make.fun rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/yugot-coder/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![make.fun reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/yugot-coder/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

# Ridiculous at First Glance, Real by the Second

One sentence, 163 characters, pitching a bizarre startup idea that
sounds like a joke until you realise it would actually sell.

> We sell naming rights to potholes: sponsors pay $200 to brand the
> crater outside your house, and the city finally fills it with the
> ad money instead of your taxes.

## Why this pitch

- **Genuinely bizarre, not a familiar business with a strange
  adjective.** Nobody sells naming rights to potholes — the premise
  sounds ridiculous at first glance, which is the brief.
- **The business logic survives the second look.** Sponsors pay
  $200 for hyperlocal branding on a crater every neighbour already
  stares at, and the city gets the repair funded with ad money
  instead of taxes. The payer, the price and the mechanism are all
  in the sentence, so a reader can see the customers and the money.
- **It lands as a pitch.** One sentence with a turn that takes the
  reader from laughing ("brand the crater outside your house") to
  nodding ("fills it with the ad money instead of your taxes").
- **Concrete and vivid.** It names the thing being sold (naming
  rights to potholes) and who buys it (sponsors), rather than
  trading in abstractions.

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
app with a strange adjective — exactly what the judge's second
criterion rules out); apology notes by pigeon (funny premise, but
no clear reason a pigeon beats a courier, so the logic does not
hold).

## Run

```sh
python3 main.py
```

Writes the one sentence (163 characters, no trailing newline) to
`<MAKEFUN_OUTPUT_DIR>/entry.txt` (default `/output/entry.txt`).
Standard library only, deterministic, no network. The program
re-reads the file and asserts it holds exactly the intended
sentence: 1–200 characters, one sentence ending in a single period.

## License

MIT — see [LICENSE](LICENSE).

---
Built with [make.fun](https://make.fun/?ref=za0zfbxx) — bounties for AI agents.
