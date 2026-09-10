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

## Getting the data

The 2026 shared task distributes the official en-AU and en-UK splits through the
task website once you register:

- Website: <https://www.alta.asn.au/events/sharedtask2026/>
- Contact: <shared.task@alta.asn.au>

The public `BESSTIE` snapshot is also available on the Hugging Face Hub (you may
need to accept its license terms):

```bash
pip install 'alta-shared-task-2026[hf]'
python -c "from alta_shared_task_2026.data import load_huggingface; load_huggingface().to_csv('data/raw/besstie-train.csv', index=False)"
```

> Note: the Hub snapshot is distributed under **CC-BY-NC-4.0** — check the
> license before any redistribution.
