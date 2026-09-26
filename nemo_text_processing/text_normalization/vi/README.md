# Vietnamese symbol and emoji normalization

`data/whitelist/symbol.tsv` contains active Vietnamese (Northern) symbol and
emoji names from eSpeak-ng `dictsource/vi_emoji` at commit
`ba90c8e9f440ad544f674a790bb5f53878b6ffc5`. Commented entries are
excluded, keys are unique, and existing NeMo wording wins on collisions.
In particular, the standalone `€`, `₫`, `₹`, and `₣` entries use the names
already present in NeMo's money data.

Currency signs intentionally occur in both the symbol whitelist and the
active `data/money/currency.tsv`. The whitelist handles a standalone sign;
the money grammar handles amounts such as `100₿` and `₿100` with Vietnamese
number-before-currency speech order. Clock
emoji, arrows, and mathematical signs stay in the generic whitelist because
the active time, measure, and other classifiers do not consume them as
contextual symbol mappings. Vietnamese TN has no active electronic or math
classifier.
The minor-unit signs `₥` and `₰` remain standalone only because the active
currency TSV represents major units.

Some eSpeak names were adapted for natural TN wording: flag labels omit
the spoken colon, `🕤` says *chín giờ ba mươi phút* instead of the source's
*chính giờ ba mươi phút*, and several currency names were lowercased or
corrected (including source `₺` *Lia Thổ Nhĩ Kỳ*). Some historical currency
names remain as eSpeak labels because NeMo has no established alternatives.
The English source label for the minor-unit sign `₥` is rendered as
*một phần nghìn* rather than read as an English word.
Keycap and family/couple emoji names were changed from colon-separated source
annotations to spoken phrases, and digit-bearing descriptions spell out the
numbers.
