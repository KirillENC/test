from fastapi import Query
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import functions
from sqlalchemy import func
from Domain.patient import Patient
from Domain.Enums.roles import Permission
from Domain.user import User
from utils import get_db, get_current_user, check_permission, create_pagination_result,\
    FluentFilter
from ..Models.patientsDto import PatientDto
from ..router import router
from ...paginationResultModel import PaginationResultModel


@router.get("/list")
def patient_list(page: int,
                 fullTextSearch: str | None = None,
                 idFilter: list[str] = Query(None),
                 nameFilter: str | None = None,
                 dobFromFilter: str | None = None,
                 dobToFilter: str | None = None,
                 manFilter: bool | None = None,
                 womanFilter: bool | None = None,
                 sortType: str | None = None,
                 sortField: str | None = None,
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)
                 ) -> PaginationResultModel[PatientDto]:
    check_permission(current_user, Permission.Patients)
    if manFilter and womanFilter:
        womanFilter = False
        manFilter = False

    if nameFilter is not None and nameFilter != '':
        name_filter = nameFilter.lower()

    result_query = FluentFilter(sortType, sortField)\
        .use_filter(idFilter, lambda q: q.filter(Patient.QmsId.in_(idFilter)))\
        .use_filter(dobFromFilter, lambda q: q.filter(Patient.Dob >= dobFromFilter))\
        .use_filter(dobToFilter, lambda q: q.filter(Patient.Dob <= dobToFilter))\
        .use_filter(manFilter, lambda q: q.filter(Patient.Gender == 0))\
        .use_filter(womanFilter, lambda q: q.filter(Patient.Gender == 1))\
        .use_filter(fullTextSearch, lambda q: q.filter(Patient.QmsId.contains(fullTextSearch) |
                                   Patient.Name.contains(fullTextSearch) |
                                   Patient.Surname.contains(fullTextSearch) |
                                   Patient.Patronymic.contains(fullTextSearch) |
                                   (Patient.Name + ' ' + Patient.Surname).contains(fullTextSearch)))\
        .use_filter(nameFilter, lambda q: q.filter(func.lower(functions.concat(Patient.Surname, ' ', Patient.Name)).like('%' + nameFilter + '%') |
                    func.lower(functions.concat(Patient.Name, ' ', Patient.Surname)).like('%' + name_filter + '%')))\
        .use_sort('dob', Patient.Dob)\
        .build(Patient.Id)

    return create_pagination_result(db, Patient, PatientDto, page,
                                      lambda x: PatientDto(
                                          id=str(x.Id),
                                          qmsId=x.QmsId,
                                          name=x.Name,
                                          surname=x.Surname,
                                          patronymic='' if x.Patronymic is None else x.Patronymic,
                                          gender=x.Gender,
                                          dob=x.Dob,
                                          tasks=[]
                                      ), result_query)
