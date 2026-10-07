from app.entity.db import db


class IDP(db.Model):
    """Entity: an Interior Design Project in a designer's portfolio."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, default="")
    category = db.Column(db.String(50), nullable=False)
    designer_id = db.Column(db.Integer, db.ForeignKey("user_account.id"), nullable=False)
    view_count = db.Column(db.Integer, default=0)
    shortlist_count = db.Column(db.Integer, default=0)

    @classmethod
    def search(cls, keyword):
        """Case-insensitive search on title or category."""
        if not keyword:
            return cls.query.order_by(cls.id).all()
        pattern = f"%{keyword}%"
        return (
            cls.query.filter(db.or_(cls.title.ilike(pattern), cls.category.ilike(pattern)))
            .order_by(cls.id)
            .all()
        )
