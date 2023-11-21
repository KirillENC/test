from fastapi import APIRouter

router = APIRouter(
    prefix="/api/profile",
    tags=["Profile"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)