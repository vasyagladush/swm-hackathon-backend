from models.Marker import Marker

async def retrieve_markers(category) -> list[Marker]:
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
    markers = await Marker.all().to_list()
    return markers

async def add_marker(new_marker: Marker) -> Marker:
    marker = await new_marker.create()
    return marker