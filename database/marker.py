from bson import ObjectId
from models.Marker import Marker
from models.Category import Category


async def retrieve_markers(category_ids: list[str] | None) -> list[Marker]:
    '''
    This function retrieves the markers from the database

    Args:
    category (list[str] | None): List of category ids to filter the markers, if None all markers are retrieved

    Returns:
    dict: The markers retrieved
        {
            name: str,
            lat: str,
            lng: str,
            category: str
        }
    '''
    
    if not category_ids:
        markers = await Marker.all().to_list()
        return markers
    
    # return await Marker.find({"category": {"$in": list(map(ObjectId, category_ids))}}).to_list()
    return await Marker.find({"category": ObjectId('65f5b153495352a2cce8c096')}).to_list()


async def add_marker(new_marker: Marker) -> Marker:
    marker = await new_marker.create()
    return marker
