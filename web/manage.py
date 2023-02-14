from flask.cli import FlaskGroup

from app import app, db
from app.models.contact import Contact
from app.models.blog_entries import BlogEntry

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(
        Contact(firstname='สมชาย', lastname='ทรงแบด', phone='081-111-1111'))
    db.session.commit()
    
@cli.command("seed_microblog_db")
def seed_microblog_db():
    db.session.add(
        BlogEntry(name='ทรงแบด แซดบ่อย', message='แบดจริงไม่เถียง', email='HelloWorld@gmail.com'))
    db.session.commit()
    

if __name__ == "__main__":
    cli()