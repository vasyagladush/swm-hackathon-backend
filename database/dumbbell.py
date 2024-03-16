from models.DumbBell import DumbBell

async def retrieve_dumbbells_by_marker(markerId: str) -> list[DumbBell]:
    dumbbells = await DumbBell.find({"markerId": markerId}).to_list()
    return dumbbells 

async def retrieve_dumbbells_by_marker_and_user(markerId: str, userId: str) -> list[DumbBell]:
    dumbbells = await DumbBell.find({"markerId": markerId, "userId": userId}).to_list()
    return dumbbells 

async def add_dumbbell(new_dumbbell: DumbBell) -> DumbBell:
    dumbbell = await new_dumbbell.create()
    return dumbbell

async def update_dumbbell(dumbbell: DumbBell) -> DumbBell:
    updated_dumbell = await dumbbell.save()
    return updated_dumbell


async def retrieve_rating(dumbbells: list[DumbBell], markerId: str) -> float:
    dumbbells = await retrieve_dumbbells_by_marker(markerId)
    count = 0
    rating = 0
    for dumbbell in dumbbells:
        if dumbbell.markerId == markerId:
            rating += dumbbell.rating
            count += 1
    if count == 0:
        return 0
    return rating/count
