# NoxAI: Ingredient Toxicity Scanner 🔬

NoxAI is an end-to-end machine learning solution that evaluates the safety of cosmetic products. By analyzing ingredient labels through Computer Vision and Predictive Modeling, the app identifies potentially harmful substances in real-time.

##  Key Features
* **OCR Extraction:** Uses Tesseract OCR and custom Regex to pull ingredient names from images.
* **Molecular Analysis:** Queries the PubChem API to map ingredients to SMILES strings.
* **AI Predictions:** Uses a Random Forest model and RDKit (Morgan Fingerprints) to predict toxicity.
* **Cloud Logging:** Automatically logs new ingredients to Google Sheets via GCP.

##  Tech Stack
* **Language:** Python (Pandas, NumPy, Scikit-Learn)
* **Science:** RDKit (Cheminformatics)
* **Vision:** Tesseract OCR
* **UI:** Streamlit & Custom CSS

##  Installation
1. `git clone https://github.com/dariamihalache25/NoxAI-Ingredient-Toxicity-Scanner.git`
2. `pip install -r requirements.txt`
3. `streamlit run app.py`
