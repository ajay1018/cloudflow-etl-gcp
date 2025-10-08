-- target tables (example)
CREATE TABLE IF NOT EXISTS events (
  event_id SERIAL PRIMARY KEY,
  source   TEXT,
  payload  JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);
