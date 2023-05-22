import pandas as pd
from sqlalchemy import create_engine
from utils import calculate_duration

engine = create_engine('sqlite:///testDB.db')
query = "SELECT * FROM sources"
df = pd.read_sql(query, engine)

engine.dispose()

percents = calculate_duration(df)

# Const values for the left part of the dashboard

CLIENT_NAME = df['client_name'].iloc[0]
SHIFT_DAY = df['shift_day'].iloc[0]
ITEM = df['endpoint_name'].iloc[0]
PERIOD_START = df['calendar_day'].iloc[0]
PERIOD_END = df['calendar_day'].iloc[-1]
