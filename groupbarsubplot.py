
#imports
import pandas as pd
import numpy as np
# using seaborn for charts as group bar in subplots as it seems not possible in plotly
import seaborn as sb 
import matplotlib.pyplot as plt


# Read data from sample dummy

df = pd.read_csv('dummy.csv')
product="Spark Plugs"
df = df[df["Product_ID"]== product]

#Use GroupBy() to compute the sum
p = pd.DataFrame()
plant = pd.DataFrame()
p = df.groupby(['Plant', 'Date'])['Qty'].sum()
plant = p.to_frame()
plant.reset_index( inplace=True)
plant['Month'] = pd.to_datetime(plant['Date']).dt.strftime('%B-%Y')


dc = pd.DataFrame()
dc = df.groupby(['DC','Date'])['Qty'].sum()
dc = dc.to_frame()
dc.reset_index( inplace=True)
dc['Month'] = pd.to_datetime(dc['Date']).dt.strftime('%B-%Y')


r = pd.DataFrame()
r = df.groupby(['Retailer', 'Date'])['Qty'].sum()
r = r.to_frame()
r.reset_index( inplace=True)
r['Month'] = pd.to_datetime(r['Date']).dt.strftime('%B-%Y')


fig, axes = plt.subplots(1,3, figsize=(12, 5))

# plot barplot 
plnt= sb.barplot(x="Plant", y="Qty",  hue="Month", data=plant,ax=axes[0]) 
sb.barplot(x="DC", y="Qty",  hue="Month", data=dc, ax=axes[1]) 
sb.barplot(x="Retailer", y="Qty",  hue="Month", data=r, ax=axes[2]) 
axes[0].set_title("Plant",weight = 'bold')
axes[1].set_title("DC",weight = 'bold')
axes[2].set_title("Retailer",weight = 'bold')
fig.suptitle("Show me the inventory plan of all stocking locations for the next 3 months for product "+product, fontsize = 'x-large', 
             weight = 'bold') 
plt.show()
