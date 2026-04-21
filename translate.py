"""
ranslate.py

This utility script acts as a bridge. It queries the PubChem API to translate
common names into standard SMILES, which are required for the RDKit fingerprinting pipeline.
"""
import pubchempy as pcp
from urllib.error import URLError


def ingredients_to_smiles(ingredient_list):
    """
    Takes a list of standard chemical names and queries the PubChem database.
    Returns a dictionary mapping the original name to its canonical SMILES string.
    Returns None for chemicals that are not found or cause network errors.
    """
    result = {}

    print(f"Starting Translation of {len(ingredient_list)} items")

    for name in ingredient_list:
        try:
            # Query PubChem for compounds matching the exact text name
            results = pcp.get_compounds(name, 'name')

            if results:

                # PubChem returns a list of matches; we assume the first result is the most relevant
                result[name] = results[0].smiles
            else:
                # Log missing compounds so the pipeline doesn't crash on null values
                result[name] = None

        # Catch API timeouts or HTTP errors without crashing the entire loop
        except (URLError, pcp.PubChemHTTPError):
            print(f"Issue while searching for {name}")
            result[name] = None
        except Exception:
            result[name] = None

    return result

# ==========================================
# TEST EXECUTION
# ==========================================

# Test batch including valid chemicals and an intentional fake ("IBIVLATE") to test error handling
scanned_ingredients = ["AQUA", "BETAINE", "CITRIC ACID", "IBIVLATE"]

results = ingredients_to_smiles(scanned_ingredients)

print("\n   Final report: ")
for name, smiles in results.items():
    print(f"{name} -> {smiles}")