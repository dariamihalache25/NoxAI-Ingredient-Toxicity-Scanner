# NoxAI: Ingredient Toxicity Scanner 🔬

NoxAI is an end-to-end machine learning solution that evaluates the safety of cosmetic products. By analyzing ingredient labels through Computer Vision and Predictive Modeling, the app identifies potentially harmful substances in real-time.

## Status:  Active Prototype / Educational Project
This project was developed during my first year to explore the intersection of Machine Learning and Chemical Informatics. While functional, it is a proof-of-concept and is currently being optimized for OCR accuracy and model precision.
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

## Limitations & Roadmap
OCR Sensitivity: Tesseract currently struggles with curved packaging, low lighting, or highly stylized branding fonts.

Nomenclature Gaps: Occasional mismatches between cosmetic (INCI) names and the PubChem chemical database.

Dosage Context: The model identifies molecular hazards but cannot account for the specific concentration (%) of an ingredient.

Synergy: Predictions are based on individual ingredients; the model does not yet evaluate how chemicals interact with one another.

Latency: Real-time API queries can cause delays; implementing a local cache (SQL/Redis) is a planned optimization.

##  Installation
1. `git clone https://github.com/dariamihalache25/NoxAI-Ingredient-Toxicity-Scanner.git`
2. `pip install -r requirements.txt`
3. `streamlit run app.py`
