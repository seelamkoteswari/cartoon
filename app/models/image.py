from app.extensions import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200))
    filter_used = db.Column(db.String(100))   # ✅ NEW
    user_id = db.Column(db.Integer)