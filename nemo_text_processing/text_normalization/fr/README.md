# French text normalization symbols and emoji

`data/whitelist/symbol.tsv` contains active symbol and emoji pronunciations from
eSpeak-ng `dictsource/fr_emoji` at commit
`ba90c8e9f440ad544f674a790bb5f53878b6ffc5`.
Commented and disabled entries are excluded. The source repeats `⏯`, `🕛`,
and `🕧`; each key appears once here, based on its first active entry. Source
comments joined to three family emoji labels were removed. The clock labels
`🕛` and `🕧` use natural spoken times. Other awkward source labels were
edited for French TN: `⏯` and `🧑‍🎄`. Annotation-style flag, family, couple,
and keycap labels were turned into spoken phrases; numeric labels such as
`🔞` were written out in words.

Existing NeMo TSV mappings take precedence over eSpeak wording. The French
classifier currently has no active money, measure, math, time, or electronic
grammar for symbol plus number expressions. All 29 active currency signs are
excluded because importing a standalone currency sign makes the classifier
split a sign followed by a number. For example, adding `€` changes the
existing `€100` output from `€100` to `euro cent`. Without a money grammar,
the same risk applies to `₿100` and other currency amounts. The other 2,173
imported symbols are standalone whitelist entries.
`data/measures/measurements.tsv` is loaded only as a standalone whitelist
alternative in non-deterministic mode.
If a contextual grammar is added later, a symbol may intentionally appear in
both its contextual TSV and the generic symbol whitelist: the two files
handle different input contexts.
