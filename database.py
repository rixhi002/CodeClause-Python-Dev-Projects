from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://username:password@localhost/dbname')
Session = sessionmaker(bind=engine)
session = Session()