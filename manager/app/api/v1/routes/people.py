from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.person import Person

router = APIRouter(prefix="/people", tags=["people"])


class PersonCreate(BaseModel):
    display_name: str = Field(min_length=1, max_length=120)


class PersonOut(BaseModel):
    id: int
    display_name: str


@router.post("", response_model=PersonOut)
def create_person(payload: PersonCreate, db: Session = Depends(get_db)):
    person = Person(display_name=payload.display_name)
    db.add(person)
    db.commit()
    db.refresh(person)
    return {"id": person.id, "display_name": person.display_name}


@router.get("", response_model=list[PersonOut])
def list_people(db: Session = Depends(get_db)):
    people = db.query(Person).order_by(Person.id.asc()).all()
    return [{"id": p.id, "display_name": p.display_name} for p in people]
