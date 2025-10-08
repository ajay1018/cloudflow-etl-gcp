from pathlib import Path; import pandas as pd
RAW, PROC = Path('data/raw'), Path('data/processed'); PROC.mkdir(parents=True, exist_ok=True)
df = pd.read_json(RAW/'seed.json')
df['value_x2'] = df['value']*2
df.to_json(PROC/'events.json', orient='records', indent=2)
print('[transform] wrote', PROC/'events.json')
