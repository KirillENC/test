from fastapi import APIRouter

router = APIRouter(
    prefix="/api/users",
    tags=["Users"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)
