# Japanese text normalization symbols and emoji

`data/whitelist/symbol.tsv` contains the 2,203 active entries from eSpeak-ng
`dictsource/ja_emoji` at commit
`ba90c8e9f440ad544f674a790bb5f53878b6ffc5`. Commented or disabled
entries are excluded. The source has no duplicate keys. Existing NeMo wording
for `©`, `®`, `™`, and `€` takes precedence over eSpeak. The source labels `₰`
as a German mark, but Unicode defines it as the German penny sign; the imported
label is corrected to `ドイツペニヒ`.
Clock, keycap, and other numeric labels were written as Japanese words. Flag
and family labels were changed from colon-separated source annotations to
spoken phrases. Spaces inside imported currency names were removed for natural
Japanese text; a few awkward math and skin-tone labels were also clarified.

`data/symbol.tsv` remains the existing punctuation exclusion table. The new
generic file is loaded by the whitelist and excluded from punctuation matching.
The money classifier actively loads `data/money/currency_prefix.tsv` and
`data/money/currency_major.tsv`, so 26 additional major-currency signs occur in
both those contextual files and the generic whitelist. This intentional
duplication lets a sign alone use the whitelist while an amount uses the money
grammar. `₥` (mill) and `₰` (German penny) are minor units and remain generic
only; the money grammar's currency field represents major units.
Clock emoji and mathematical operators remain generic because the active time
grammar accepts numeral-based times and there is no Japanese math classifier.
The electronic grammar consumes ASCII web patterns; its symbol TSV is used by
the verbalizer and postprocessor, not for these emoji.
