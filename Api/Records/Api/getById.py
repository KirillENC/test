from fastapi import Depends
from sqlalchemy.orm import Session
from Domain.Enums.roles import Permission
from Domain.patient import Patient
from Domain.record import Record
from Domain.user import User
from utils import get_db, get_current_user, check_permission, get_patient_full_name
from ..Models.recordDto import RecordDto
from ..router import router


@router.get("/getById")
def get_user(id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> RecordDto:
    check_permission(current_user, Permission.Records)
    record = db.query(Record).filter(Record.Id == id).first()
    doctor = db.query(User).filter(User.Id == record.DoctorId).first()
    patient = db.query(Patient).filter(Patient.Id == record.PatientId).first()

    return RecordDto(
        id=str(record.Id),
        doctor=doctor.Name,
        patient=get_patient_full_name(patient)
    )
