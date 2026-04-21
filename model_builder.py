"""
model_builder.py

This script trains the predictive machine learning model for the NoxAI application.
It downloads the Tox21 dataset, processes SMILES chemical representations into
numerical Morgan fingerprints using RDKit, and trains a Random Forest Classifier
to predict toxicity (specifically targeting the SR-p53 stress response pathway).
"""
import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Fetch the raw Tox21 dataset from the cloud
url = "https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/tox21.csv.gz"

# Isolate the chemical structure (smiles) and our specific target toxicity metric (SR-p53).
# Drop any rows missing this specific toxicity data to ensure clean training.
dframe = pd.read_csv(url)
dframe = dframe[['smiles', 'SR-p53']].dropna()

def smiles_to_fingerprint(smiles):
    """
    Converts a SMILES string into a 2048-bit Morgan Fingerprint.
    Returns a numpy array representing the molecular structure, or None if invalid.
    """

    # Catch empty or poorly formatted data before it breaks the RDKit engine
    if not isinstance(smiles,str) or len(smiles) == 0:
        return None

    # Convert the text-based SMILES into a 2D molecule object
    molecule = Chem.MolFromSmiles(smiles)

    if molecule is None:
        return None

    # Generate a Morgan Fingerprint
    generate = AllChem.GetMorganGenerator(radius=2, fpSize=2048)
    fingerprint = generate.GetFingerprint(molecule)

    return np.array(fingerprint)

# Apply the feature engineering to the dataset
dframe['fingerprint'] = dframe['smiles'].apply(smiles_to_fingerprint)

# Drop any chemicals that RDKit failed to process into fingerprints
dframe = dframe.dropna(subset=['fingerprint'])

fp = np.stack(dframe['fingerprint'].values)
tox = dframe['SR-p53'].values
fp_train, fp_text, tox_train, tox_test = train_test_split(fp, tox, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model using 100 decision trees
clf = RandomForestClassifier(100, random_state=42)
clf.fit(fp_train, tox_train)

# Export the trained model pipeline so the Streamlit frontend can load it instantly
joblib.dump(clf, "toxicity_model.pkl")