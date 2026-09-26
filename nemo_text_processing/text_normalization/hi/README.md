# Hindi text normalization symbols

Standalone symbol and emoji names in `data/whitelist/symbol.tsv` come from
eSpeak-ng `dictsource/hi_emoji` at commit
`ba90c8e9f440ad544f674a790bb5f53878b6ffc5`. Active entries were
deduplicated, and existing NeMo wording takes precedence on collisions. The
source's `☦` label ends in a stray backslash, so it is rendered as
`ईसाई क्रॉस`. The 24 clock-face labels were shortened from keyword lists to
natural spoken times (for example, `🕐` is `एक बजे`). Flag, keycap, and
family/couple emoji labels were also changed from colon-separated source
annotations to spoken phrases; digit-bearing descriptions now spell out the
numbers.

Currency signs also appear in `data/money/currency.tsv` and
`data/money/currency_singular.tsv`: the whitelist handles a standalone sign,
while the active money grammar handles amounts such as `₿100`. The `⁻` entry
also appears in the active electronic verbalizer's `symbols.tsv`, retaining
NeMo's established name in both contexts. Mathematical signs remain in the
generic symbol whitelist because Hindi TN has no active general math grammar.
The minor-unit signs `₥` and `₰` remain standalone only: the money grammar's
currency files describe major units.
