from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/health", tags=["health check"])

@router.get("/",status_code=200)
async def health_check():
    return JSONResponse(content={"status": "ok", "message": "Service is healthy"})