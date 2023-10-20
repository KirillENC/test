from fastapi import APIRouter

router = APIRouter(
    prefix="/api/records",
    tags=["Records"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)
