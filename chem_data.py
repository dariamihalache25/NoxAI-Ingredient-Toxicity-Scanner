"""
chem_data.py

This utility script downloads the raw Tox21 dataset from DeepChem's public AWS S3 bucket.
It is used to get the initial chemical toxicity data needed to train the
Random Forest machine learning model for the NoxAI application.
"""
import pandas as pd

url = "https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/tox21.csv.gz"
dframe = pd.read_csv(url)

print(dframe.columns.tolist())
dframe.to_csv("tox21_chem_data.csv", index=False)
