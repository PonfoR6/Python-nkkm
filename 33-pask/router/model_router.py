from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repository import model_repo as repo
from database import get_db
import schemas
from typing import List

router = APIRouter(
    prefix='/api/models',
    tags=['Models']
)


@router.get('', response_model=List[schemas.ModelInfo])
def all(db: Session = Depends(get_db)):
    return repo.get(db)


@router.post('/create')
def model_create(request: schemas.ModelInfo, db: Session = Depends(get_db)):
    return repo.create_model(request, db)


@router.put('/update/{id}')
def model_update(id: int, request: schemas.ModelCreate, db: Session = Depends(get_db)):
    return repo.update_model(id, request, db)


@router.delete('/delete/{id}')
def model_delete(id: int, db: Session = Depends(get_db)):
    return repo.delete_model(id, db)
