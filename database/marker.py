from beanie import PydanticObjectId
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

    all_markers = await Marker.all().to_list()
    markers = []

    for marker in all_markers:
        if str(dict(dict(marker)['category'])['id']) in category_ids:
            markers.append(marker)

    return markers
    # return await Marker.find({"category": {"$in": list(map(ObjectId, category_ids))}}).to_list()
    # TODO: make it query DB approperiately and filter by category's id


async def add_marker(new_marker: Marker) -> Marker:
    marker = await new_marker.create()
    return marker
