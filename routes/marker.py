from fastapi import APIRouter, Body, Query
from typing import Annotated

from database.marker import *
from models.Marker import Marker
from schemas.student import Response
from database.dumbbell import retrieve_dumbbells_by_marker


router = APIRouter()

@router.get("/", response_description="Markers retrieved", response_model=Response)
async def get_markers(categories: Annotated[list[str] | None, Query()] = None):
    markers = await retrieve_markers(categories)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Marker data retrieved successfully",
        "data": markers,
    }




@router.get("/{marker_Id}/dumbbells-average", response_description="Dumbbells retrieved", response_model=Response)
async def get_categories(marker_id: str):
    dumbbells = await retrieve_dumbbells_by_marker(marker_id)
    if dumbbells:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Dumbbell data retrieved successfully",
            "rating": dumbbells,
        }
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "No categories found",
            "rating": 0.0,
        }
