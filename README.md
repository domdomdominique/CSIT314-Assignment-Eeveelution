# CSIT314-Assignment-Eeveelution
CSIT314 Software Development Methodology Group Assignment

Team Members: Jeremiah, Dominique, Bryan, Thiri, Xi Ze

An online platform matching renovation customers to interior designers, built with Python + Flask using the Boundary-Control-Entity (B-C-E) design.

## Run it locally (Windows PowerShell)

```powershell
python -m venv venv
venv\Scripts\activate          # Mac/Git Bash: source venv/bin/activate
pip install -r requirements.txt
python seed.py                 # creates test data (100 records per type)
python run.py                  # open http://127.0.0.1:5000
```

Demo logins (password `password123`): `admin@demo.com`, `designer@demo.com`, `customer@demo.com`, `platform@demo.com`.

Run tests: `pytest -v`

## Structure (B-C-E)

```
app/
├── boundary/      Pages and routes (one file per actor) + templates/
├── control/       One controller class per use case
└── entity/        Data classes (UserAccount, IDP, ...) that talk to the database
tests/             pytest unit tests (written first: TDD)
seed.py            Test data generator
```

Rule: boundary calls one controller; controller calls entities; only entities touch the database.
