import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

nifty_bank = pd.read_csv("NIFTY BANK1.csv", parse_dates=["Date"])
nifty_fmcg = pd.read_csv("NIFTY FMCG1.csv", parse_dates=["Date"])
nifty_it = pd.read_csv("NIFTY IT1.csv", parse_dates=["Date"])
nifty_pharma = pd.read_csv("NIFTY PHARMA1.csv", parse_dates=["Date"])

print(nifty_bank)

nifty_bank = pd.read_csv("NIFTY BANK1.csv", parse_dates=["Date"])
nifty_fmcg = pd.read_csv("NIFTY FMCG1.csv", parse_dates=["Date"])
nifty_it = pd.read_csv("NIFTY IT1.csv", parse_dates=["Date"])
nifty_pharma = pd.read_csv("NIFTY PHARMA1.csv", parse_dates=["Date"])
nifty_bank_2019 = nifty_bank[nifty_bank["Date"] > "2019-12-31"]
nifty_fmcg_2019 = nifty_fmcg[nifty_fmcg["Date"] > "2019-12-31"]
nifty_it_2019 = nifty_it[nifty_it["Date"] > "2019-12-31"]
nifty_pharma_2019 = nifty_pharma[nifty_pharma["Date"] > "2019-12-31"]

d = {
     "Nifty Bank Index" : nifty_bank_2019["Close"].values,
     "Nifty FMCG Index" : nifty_fmcg_2019["Close"].values,
     "Nifty IT Index" : nifty_it_2019["Close"].values,
     "Nifty Pharma Index" : nifty_pharma_2019["Close"].values
}

df = pd.DataFrame(data=d)
df.index = nifty_it_2019['Date']
df.head()
