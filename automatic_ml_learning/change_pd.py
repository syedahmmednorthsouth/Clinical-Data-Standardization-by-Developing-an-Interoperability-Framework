import pandas as pd
import numpy as np


df = pd.read_csv('final_for_ml4.csv')

df['test_name_with_attribute'] = df['test_name_with_attribute'].str.replace("(","")

df['test_name_with_attribute'] = df['test_name_with_attribute'].str.replace(")","")


df["test_name_with_attribute"] = df["test_name_with_attribute"].str.replace(",","")



df.to_csv('final_for_ml5.csv')