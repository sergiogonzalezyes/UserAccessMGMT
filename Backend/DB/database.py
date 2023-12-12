from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
print('DB URL CONNECTION: ', database_url)

if database_url is None:
    raise ValueError("DATABASE URL env var is not set")

engine = create_engine(database_url, connect_args={'ssl': {'ssl_cert': None}})
Base = declarative_base()