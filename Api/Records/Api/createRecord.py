from fastapi import Depends
from Domain.patient import Patient
from Domain.record import Record
from Domain.user import User
from sqlalchemy.orm import Session
from utils import get_db

from datetime import datetime
import uuid
from ..router import router


@router.post("/createRecord")
def create_record(name: str,
                  surname: str,
                  patronymic: str,
                  gender: str,
                  dob: str,
                  doctorId: str,
                  time: str,
                  db: Session = Depends(get_db)):

    doctor = db.query(User).filter(User.Id == doctorId).first()
    patient = (db.query(Patient)
               .filter(Patient.Name == name)
               .filter(Patient.Surname == surname)
               .filter(Patient.Patronymic == patronymic)
               .filter(Patient.Gender == gender)
               .filter(Patient.Dob == dob)
               .first())
    if patient is None:
        patient = Patient(
            Id=str(uuid.uuid4()),
            Name=name,
            Surname=surname,
            Patronymic=patronymic,
            Gender=gender,
            Dob=datetime.strptime(dob, '%d.%m.%Y')
        )
        db.add(patient)

    db.add(Record(
        Id=str(uuid.uuid4()),
        DoctorId=doctor.Id,
        PatientId=patient.Id,
        DateTimeStart=datetime.strptime(time, '%d.%m.%Y %H:%M')
    ))
    db.commit()
    return 'created'
