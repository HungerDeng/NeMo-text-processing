# Korean symbol and emoji normalization

`data/whitelist/symbol.tsv` is derived from eSpeak-ng
[`dictsource/ko_emoji`](https://github.com/espeak-ng/espeak-ng/blob/ba90c8e9f440ad544f674a790bb5f53878b6ffc5/dictsource/ko_emoji)
at commit `ba90c8e9f440ad544f674a790bb5f53878b6ffc5`. Only active entries are
included. Existing NeMo mappings take precedence: `€` uses the established
`유로` money name instead of eSpeak's `유로화`.

The source labels for `⁻`, `₪`, `⏮`, and `🧬` were adapted for natural Korean
text normalization. Flag, keycap, family, and couple descriptions use spoken
phrases instead of eSpeak's colon-separated annotations, and numeric labels
spell out their digits. Currency signs intentionally appear in both the generic
symbol whitelist and `data/money/currency_major.tsv`: the whitelist handles a
standalone sign, while the active money grammar handles a sign with an amount.
The fractional signs `₥` and `₰` remain standalone because this money grammar
has no minor currency unit field. Mathematical signs remain generic because
Korean has no active math classifier, and clock emoji remain generic because
the time classifier does not consume emoji names.
