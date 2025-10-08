from pathlib import Path; import pandas as pd
RAW = Path('data/raw'); RAW.mkdir(parents=True, exist_ok=True)
df = pd.DataFrame([{'source':'seed','value':1},{'source':'seed','value':2}])
(df.assign(event_id=range(1, len(df)+1))).to_json(RAW/'seed.json', orient='records', indent=2)
print('[extract] wrote', RAW/'seed.json')
