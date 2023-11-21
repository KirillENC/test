from fastapi import APIRouter

router = APIRouter(
    prefix="/api/identity",
    tags=["Identity"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)
