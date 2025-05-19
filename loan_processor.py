import json
import requests

# 👉 Replace this with your Azure Blob SAS URL
blob_url = "https://sebicompliancestorage.blob.core.windows.net/compliance-uploads/credit_data.json?sp=r&st=2025-05-19T07:01:55Z&se=2025-05-19T15:01:55Z&spr=https&sv=2024-11-04&sr=b&sig=xz9Q0f4zqldYdYQyUGsDAYBV%2BoFsCbJ91NXKbJHqdNY%3D"

# Step 1: Download the credit data
response = requests.get(blob_url)
data = response.json()

# Step 2: Process each record
results = []
for record in data:
    decision = "Approved" if record["credit_score"] >= 700 else "Rejected"
    results.append({
        "id": record["id"],
        "name": record["name"],
        "credit_score": record["credit_score"],
        "decision": decision
    })

# Step 3: Save results to file
with open("loan_decisions.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Loan decisions saved to loan_decisions.json")
s
