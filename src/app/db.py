# src/app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

# à adapter avec ton vrai user/mot de passe/port
DATABASE_URL = "postgresql+psycopg://user:password@localhost:5432/projet5"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
# create_db.py à la racine du projet (ou dans src/)
import pandas as pd
from sqlalchemy.orm import Session

from src.app.db import engine, init_db, SessionLocal
from src.app.models import Text


def load_dataset_to_db(csv_path: str):
    df = pd.read_csv(csv_path)

    with Session(engine) as session:
        for _, row in df.iterrows():
            text = Text(
                external_id=str(row["id"]),
                raw_text=row["text"],
                true_label=row["label"],
                source="dataset",
            )
            session.add(text)

        session.commit()
        print(f"{len(df)} lignes insérées dans la table texts.")


if __name__ == "__main__":
    # 1. Créer les tables
    init_db()
    # 2. Charger le dataset
    load_dataset_to_db("data/dataset_clean.csv")
