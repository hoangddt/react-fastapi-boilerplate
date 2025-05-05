from fastapi import Request
from datetime import datetime
from minimal_template.api.users.schemas import UserResponse


async def get_current_user(request: Request) -> UserResponse:
    fake_user = UserResponse(
        id="1",
        email="test@test.com",
        username="test",
        full_name="Test User",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    return fake_user
