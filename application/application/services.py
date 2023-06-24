from sqlalchemy import select
from sqlalchemy.sql import func
from starlette.requests import Request

from application.config import PAGINATION_SIZE


async def limit_offset(model: type, page: int = 1):
    query = select(model).limit(PAGINATION_SIZE).offset((page - 1) * PAGINATION_SIZE)
    return select(func.count(model.id).label("is_count")), query


async def get_result(request: Request, count: int, page: int, results) -> dict:
    """
    Составляет json ответ для пользователя в соответствии с требованиями.
    Составляет следующую, предыдущую и количество страниц для пагинации.
    """
    return {
        "count": count,
        "next": (
            str(request.url.replace_query_params(page=page + 1))
            if page * PAGINATION_SIZE < count
            else None
        ),
        "previous": str(request.url.replace_query_params(page=page - 1)) if page > 1 else None,
        "results": results,
    }
