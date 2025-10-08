import os, json, pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv; load_dotenv()
PG = f"postgresql+psycopg2://{os.getenv('PG_USER','postgres')}:{os.getenv('PG_PASSWORD','postgres')}@{os.getenv('PG_HOST','localhost')}:{os.getenv('PG_PORT','5432')}/{os.getenv('PG_DB','cloudflow')}"
engine = create_engine(PG, future=True)
with engine.begin() as c:
    for stmt in open('sql/schema.sql','r',encoding='utf-8').read().split(';'):
        if stmt.strip(): c.execute(text(stmt))
df = pd.read_json('data/processed/events.json')
df[['source']]=df[['source']].astype(str)
# load as raw JSON for demo
with engine.begin() as c:
    for _, r in df.iterrows():
        c.execute(text("INSERT INTO events(source, payload) VALUES (:s, :p)"), {'s': r['source'], 'p': json.loads(r.to_json())})
print('[load] inserted', len(df), 'rows')
