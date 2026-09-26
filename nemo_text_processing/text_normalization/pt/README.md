# Portuguese (Brazil) symbols and emoji

Portuguese TN is implemented under `pt` and uses Brazilian wording. The active
symbol and emoji mappings in `data/whitelist/symbol.tsv` come from eSpeak-ng
`dictsource/pt_emoji` at commit
`ba90c8e9f440ad544f674a790bb5f53878b6ffc5`. eSpeak-ng labels this source
Portuguese (Portugal); it provides no separate Brazilian emoji dictionary.
Existing NeMo symbol mappings take precedence on collisions.

The imported labels retain their exact Unicode keys, including flags, keycaps,
variation selectors, and ZWJ sequences. Spoken wording was adjusted where the
source contains digits or annotation-style labels for clocks, flags, keycaps,
and families. The pt-PT `dececionada` is rendered as pt-BR `decepcionada`.
The source's `₥ → mill` was omitted because it is an English
minor-currency name with no clear Brazilian Portuguese standalone reading.

Currency signs may intentionally appear both in `data/whitelist/symbol.tsv`
and the active `data/money/currency_major.tsv`: the whitelist handles a
standalone sign, while the money grammar handles amounts such as `₿100`.
Portuguese TN has no active math grammar, so mathematical signs remain in the
symbol whitelist. Its money grammar currently uses masculine cardinal forms;
feminine currency signs remain standalone symbols until that grammar supports
their agreement in amounts.
