from app.control.search_idp_controller import SearchIDPController
from app.entity.db import db
from app.entity.idp import IDP
from app.entity.user_account import UserAccount


def add_idps():
    designer = UserAccount.create("des@test.com", "pass123", "designer")
    db.session.add_all([
        IDP(title="Scandinavian Loft", category="Living Room", designer_id=designer.id),
        IDP(title="Modern Kitchen Revamp", category="Kitchen", designer_id=designer.id),
    ])
    db.session.commit()


def test_search_by_keyword_matches_title(app):
    add_idps()
    results = SearchIDPController().search("loft")
    assert [r.title for r in results] == ["Scandinavian Loft"]


def test_search_by_keyword_matches_category(app):
    add_idps()
    results = SearchIDPController().search("kitchen")
    assert len(results) == 1


def test_empty_keyword_returns_all(app):
    add_idps()
    assert len(SearchIDPController().search("")) == 2
