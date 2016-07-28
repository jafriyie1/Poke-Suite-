import pandas as pd


df = pd.read_json("poke_twitter_data.json")
data = pd.DataFrame(df)
print(data)
