# Travel Planner

An original multi-role travel-planning demo. Destination research, interest
matching, lodging/transport estimation, and budget review appear as explicit
planner handoffs over a small local sample guide.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Planner roles run locally over sample data; they are not live travel agents.
Activities and costs are illustrative—not live availability, advice,
reservations, or booking prices. Confirm details with providers.
Run tests with `python -m unittest discover -s tests -v`.
