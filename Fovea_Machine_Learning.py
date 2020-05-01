import os
import pandas as pd

path2data="./data/"

path2labels=os.path.join(path2data,"Training400","Fovea_location.xlsx")

labels_df=pd.read_excel(path2labels,index_col="ID")

labels_df.head()
