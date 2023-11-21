from fastapi import Depends
from sqlalchemy.orm import Session
from Domain.Enums.roles import Permission
from Domain.patient import Patient
from Domain.record import Record
from Domain.user import User
from utils import get_db, get_current_user, check_permission, create_pagination_result, FluentFilter, \
    get_patient_full_name
from ..Models.recordDto import RecordDto
from ..router import router
from ...paginationResultModel import PaginationResultModel


@router.get("/list")
def user_list(page: int,
              sortType: str | None = None,
              sortField: str | None = None,
              db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)
              ) -> PaginationResultModel[RecordDto]:
    check_permission(current_user, Permission.Records)

    result_query = FluentFilter(sortType, sortField) \
        .use_join(lambda q: q.join(Patient, Record.PatientId == Patient.Id)
                  .join(User, Record.DoctorId == User.Id)
                  .with_entities(Record, Patient, User)) \
        .build(Record.DateTimeStart)

    return create_pagination_result(db, Record, RecordDto, page,
                                    lambda x: RecordDto(
                                        id=str(x.Record.Id),
                                        doctor=x.User.Name,
                                        patient=get_patient_full_name(x.Patient),
                                        start=str(x.Record.DateTimeStart)
                                    ), result_query)
