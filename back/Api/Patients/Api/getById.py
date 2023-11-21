from fastapi import Depends
from sqlalchemy.orm import Session
from Domain.patient import Patient
from Domain.Enums.roles import Permission
from Domain.user import User
from utils import get_db, get_current_user, check_permission
from ..Models.patientModalDto import PatientModalDto
from ..router import router


@router.get("/getById")
def get_user(id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> PatientModalDto:
    check_permission(current_user, Permission.Patients)
    patient = db.query(Patient).filter(Patient.Id == id).first()

    return PatientModalDto(
        id=str(patient.Id),
        qmsId=patient.QmsId,
        name=patient.Name,
        surname=patient.Surname,
        patronymic='' if patient.Patronymic is None else patient.Patronymic,
        gender=patient.Gender,
        dob=patient.Dob,
    )
