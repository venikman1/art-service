from app import app, db, User

db.create_all()
admin = User('admin', 'secret_pass')
db.session.add(admin)
db.session.commit()