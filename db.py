from sqlalchemy import String, INT, create_engine

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

class Base(DeclarativeBase):
    pass

class LogBase(Base):
    __tablename__ = 'logs'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(INT())
    date_text: Mapped[str] = mapped_column(String(30))
    req_text: Mapped[str] = mapped_column(String(30))
    ans_text: Mapped[str] = mapped_column(String(30))

DB_URL = 'sqlite:///log_info.db'
engine = create_engine(DB_URL, echo=True)

async def add_log(log: LogBase):
    with Session(engine) as session:
        session.add(log)
        session.commit()
        session.refresh(log)

def get_all_logs():
    with Session(engine) as session:
        result = session.query(LogBase).all()
    return result

def get_log_by_user(user_id: int):
    with Session(engine) as session:
        result = session.query(LogBase).filter(LogBase.user_id == user_id).all()
    return result

def create_db_and_tables() -> None:
    Base.metadata.create_all(engine)