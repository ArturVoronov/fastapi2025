from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append('./')
from model.models import Base

db_user: str = 'postgres'
db_port: int = 5432
db_host: str = 'localhost'
db_password: str = 'c420av98'

uri:str = F'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/to-do-app'

engine = create_engine(uri)
Base.metadata.create_all(bind=engine)

session = sessionmaker(
    bind=engine, autoflush=True
)
db_session = session()

try: 
    connection = engine.connect()
    connection.commit()
    connection.close()
    print('ping, Connected')
except Exception as e:
    print(f'Error:{str(e)}')
