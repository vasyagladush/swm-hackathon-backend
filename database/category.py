from models.Category import Category

async def retrieve_categories() -> list[Category]:
    '''
    This function retrieves the categories from the database
    
    Args:
    q (list[str] | None): The query parameter
    
    Returns:
    dict: The categories retrieved
        {
            name: str,
            id: str
        }
    '''
    categories = await Category.all().to_list()
    return categories 

async def add_category(new_category: Category) -> Category:
    category = await new_category.create()
    return category

async def find_category_by_name(name: str):
    return await Category.find_one(Category.name == name)
