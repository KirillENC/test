from fastapi import APIRouter

router = APIRouter(
    prefix="/api/definition",
    tags=["Definitions"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)
