# Localization Note

Depending on locale, Spanish number strings will vary in formatting. In the EU and South American countries, it is common to use a period (".") or space to delineate groupings of three
digits. e.g.
	`1.000.000` -> "un millón"
	`1 000 000` -> "un millón"

and commas (",") to seperate cardinal and decimal strings. e.g.

	`1,00` -> "uno coma cero cero"

While Central and Northern America will use commas (",") to delineate groupings of three digits, e.g.
	`1,000,000` -> "un millón"

and periods (".") to seperate cardinal and decimal strings. e.g.

	`1.00` -> "uno coma cero cero"

As inclusion of both forms will create inherrent ambiguity for verbalization, this module defaults to the former formatting (periods for cardinal delineation and commas for decimals).

To toggle the alternate formatting, you may edit the `LOCALIZATION` variable in `nemo_text_processing.text_normalization.es.__init__` with the value of `'am'`. This will perform necessary
adjustments to all affected classes.

## Symbols and emoji

`data/whitelist/symbol.tsv` contains active Spanish entries from eSpeak-ng
`dictsource/es_emoji` at commit `ba90c8e9f440ad544f674a790bb5f53878b6ffc5`.
Existing NeMo currency names take precedence when the two sources overlap. A few
source descriptions were adjusted for text normalization: clock digits are
spelled out, flags and family emoji use natural Spanish phrasing, keycaps are
named as keys, and some mathematical labels were simplified. The ambiguous `⊶` description
(`original`) was omitted.

Currency signs can intentionally occur in both `data/whitelist/symbol.tsv`
and `data/money/currency_major.tsv`: the whitelist handles a standalone sign,
while the money grammar handles an amount such as `₿100`. Arithmetic operator
signs can similarly occur in the symbol whitelist and the active
`data/measures/math_symbols.tsv`, where they are used inside equations. The
`data/money/*_ext.tsv` files are optional data; the classifier currently loads
the main money TSV files.
