from fastapi import FastAPI, Path

from services.easistent.data import School
from services.easistent.school import get_school_info

app = FastAPI()


@app.get("/easistent/school/{link_id}", response_model=School)
async def school(link_id: str = Path(default="", description="The ID located inside of the urnik link")):
	return get_school_info(link_id)
