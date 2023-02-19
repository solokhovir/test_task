from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///data.db')
Base = declarative_base()


class Data(Base):
    __tablename__ = 'queue_statuses'
    id = Column(Integer, primary_key=True)
    s_name = Column(String(512))
    c_name = Column(String(512))
    c_id = Column(String(32))
    a_type = Column(String(128))
    direction = Column(String(32))
    activation = Column(String(32))
    c_state = Column(String(32))
    control = Column(String(32))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def save_data(s_name, c_name, c_id, a_type, direction, activation, c_state, control):
    existing_data = session.query(Data).filter_by(s_name=s_name, c_name=c_name, c_id=c_id,
                                                  a_type=a_type, direction=direction,
                                                  activation=activation, c_state=c_state,
                                                  control=control).first()
    if existing_data:
        return
    data = Data(s_name=s_name, c_name=c_name, c_id=c_id, a_type=a_type,
                direction=direction, activation=activation, c_state=c_state, control=control)
    session.add(data)
    session.commit()
