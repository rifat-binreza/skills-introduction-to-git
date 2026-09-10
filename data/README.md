# Data directory

Raw BESSTIE data, intermediate files and processed splits live here. Data files
are intentionally git-ignored (see `.gitignore`).

## Layout

```
data/
├── raw/         # original BESSTIE downloads (CSV/Parquet)
├── external/    # third-party data
├── interim/     # cleaned, pre-split data
└── processed/   # final train/dev/test splits
```

## Schema

The task schema is one row per text with columns:

| Column | Type | Description |
| --- | --- | --- |
| `text` | string | The review/comment to classify. |
| `sentiment` | int (0/1) | Binary sentiment label. |
| `sarcasm` | int (0/1) | Binary sarcasm label. |
| `variety` | string | `en-AU` or `en-UK` (optional). |
| `source` | string | `GOOGLE` or `REDDIT` (optional). |

## Getting the data

The 2026 shared task distributes the official en-AU and en-UK splits through the
task website once you register:

- Website: <https://www.alta.asn.au/events/sharedtask2026/>
- Contact: <shared.task@alta.asn.au>

The public `BESSTIE` snapshot is also available on the Hugging Face Hub (you may
need to accept its license terms). It exposes one config per variety
(`en_AU`, `en_IN`, `en_UK`) in wide format with columns `source`, `variety`,
`text`, `sentiment`, `sarcasm`:

```bash
pip install 'alta-shared-task-2026[hf]'
python -c "from alta_shared_task_2026.data import load_huggingface as l; l(config='en_AU').to_csv('data/raw/besstie-en-AU.csv', index=False)"
```

> Note: the Hub snapshot is distributed under **CC-BY-NC-4.0** — check the
> license before any redistribution.

## Resources

- [BESSTIE on the Hugging Face Hub](https://huggingface.co/datasets/unswnlporg/BESSTIE)
- [BESSTIE paper (ACL Anthology)](https://aclanthology.org/2025.findings-acl.441/)
- [ALTA 2026 Shared Task](https://www.alta.asn.au/events/sharedtask2026/)
