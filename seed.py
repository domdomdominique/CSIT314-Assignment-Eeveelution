"""Generate test data: 100 records per data type, plus one known login per role.

Run:  python seed.py
"""
import random

from app import create_app
from app.entity.db import db
from app.entity.idp import IDP
from app.entity.user_account import UserAccount

CATEGORIES = ["Living Room", "Kitchen", "Bedroom", "Bathroom", "Office", "Retail", "Cafe"]
STYLES = ["Scandinavian", "Industrial", "Modern", "Minimalist", "Japandi", "Classic", "Tropical"]
PLACES = ["Loft", "HDB Flat", "Condo", "Landed House", "Studio", "Shophouse"]

random.seed(314)  # same data every run, so demos are repeatable
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # One known account per role for demos (password: password123)
    for role in UserAccount.ROLES:
        UserAccount.create(f"{role}@demo.com", "password123", role)

    for i in range(1, 101):
        UserAccount.create(f"customer{i}@test.com", "password123", "customer")
    designers = [UserAccount.create(f"designer{i}@test.com", "password123", "designer")
                 for i in range(1, 101)]

    for _ in range(100):
        db.session.add(IDP(
            title=f"{random.choice(STYLES)} {random.choice(PLACES)}",
            category=random.choice(CATEGORIES),
            designer_id=random.choice(designers).id,
            view_count=random.randint(0, 500),
            shortlist_count=random.randint(0, 50),
        ))
    db.session.commit()

    print(f"Accounts: {UserAccount.query.count()}, IDPs: {IDP.query.count()}")
    print("Demo logins: admin@demo.com / designer@demo.com / customer@demo.com / "
          "platform@demo.com  (password: password123)")
