from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Film

class FilmController:
    def __init__(self):
        engine = create_engine('sqlite:///films.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_film(self, title, director, year):
        new_film = Film(title=title, director=director, year=year)
        self.session.add(new_film)
        self.session.commit()

    def get_all_films(self):
        return self.session.query(Film).all()