from fastapi import APIRouter, Body, Query
from typing import Annotated

from database.category import *
from schemas.student import Response, UpdateStudentModel


router = APIRouter()


@router.get("/", response_description="Categories retrieved", response_model=Response)
async def get_categories():
    categories = await retrieve_categories()
    if categories:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Category data retrieved successfully",
            "data": categories,
        }
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "No categories found",
            "data": categories,
        }
