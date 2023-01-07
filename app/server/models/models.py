

from pydantic import BaseModel

class SearchQuery(BaseModel):
    query: str
    max_results: int
