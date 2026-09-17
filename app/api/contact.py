from fastapi import APIRouter

from app.schemas.contact import ContactRequest

router = APIRouter(
    prefix="/api/contact",
    tags=["Contact"],
)


@router.post("")
def submit_contact(request: ContactRequest):
    return {
        "message": "Inquiry received successfully",
        "data": request.model_dump(),
    }