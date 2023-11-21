from fastapi import APIRouter

router = APIRouter(
    prefix="/api/patients",
    tags=["Patients"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)
