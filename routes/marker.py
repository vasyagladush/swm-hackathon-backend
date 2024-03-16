from fastapi import APIRouter, Body, Query
from typing import Annotated

from database.marker import *
from models.Marker import Marker
from schemas.student import Response


router = APIRouter()

@router.get("/markers", response_description="Markers retrieved", response_model=Response)
async def get_markers(categories: Annotated[list[str] | None, Query()] = None):
    markers = await retrieve_markers(categories)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Marker data retrieved successfully",
        "data": markers,
    }