from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import APILog
    
    print("init_db", flush=True)
    
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
