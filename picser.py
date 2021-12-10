#uses dominion csv feed to download pictures of all vehicles

import pandas as pd
import numpy as np
import requests
import os

df = pd.read_csv("feed2.csv")

cols = ['ID', 'Image URL'] 
df = df[cols]
df = df.replace(' --', np.nan)
df = df.dropna()

#print(df.head())

urllist = df['Image URL'].to_list()
vinlist = df['ID'].to_list()

x = 1 
picspercar = 0

for i in urllist:
    for j in vinlist:
        x += 1
        while picspercar <6:
            picspercar = +1
            pic = requests.get(i)
            open(str(j) + "-" + str(picspercar) +'.jpg', 'wb').write(pic.content)
