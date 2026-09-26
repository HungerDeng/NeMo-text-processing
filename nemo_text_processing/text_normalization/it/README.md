# Italian symbol and emoji normalization

`data/whitelist/symbol.tsv` is derived from eSpeak-ng
[`dictsource/it_emoji`](https://github.com/espeak-ng/espeak-ng/blob/ba90c8e9f440ad544f674a790bb5f53878b6ffc5/dictsource/it_emoji)
at commit `ba90c8e9f440ad544f674a790bb5f53878b6ffc5`. Only active entries are
included. Existing NeMo mappings take precedence: the standalone `€` and `₽`
entries use the established money names (`euro` and `rublo`) instead of the
eSpeak descriptions. The English or misspelled labels for `⇐`, `∎`, `∧`, `⋁`,
`⩣`, and `♐` were corrected for Italian text normalization; the obscure `∾`
label was omitted. The standalone `₹` and `₦` names were shortened to
"rupia indiana" and "naira" so they agree with the money grammar.
Flag, keycap, family, and couple descriptions use spoken phrases instead of
eSpeak's colon-separated annotations. Numeric labels spell out their digits.
The source's English `₥ → mill` was omitted because it has no clear standalone
Italian reading; it is also absent from the major-currency grammar.

Currency signs intentionally appear in both `data/whitelist/symbol.tsv` and
`data/money/currency_major.tsv`. The whitelist handles a standalone sign,
while the active money grammar handles a sign with an amount. Currency names
with reliable singular and plural forms were added to the money data;
`₰`, `₶`, and `₷` remain standalone only because their fractional or
historical usage has no reliable Italian major-currency inflection here.
Other mathematical signs remain in the whitelist because Italian has no
active math classifier. Clock emoji remain there because the time classifier
does not read emoji names.
