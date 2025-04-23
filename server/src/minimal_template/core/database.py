from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from minimal_template.core.config import settings

# Create declarative base for models
Base = declarative_base()


async def get_session() -> AsyncSession:
    """Dependency for getting async database session.

    Yields:
        AsyncSession: Async database session
    """
    if not settings.SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL is not set")
    # Create async engine
    engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=False, future=True)

    # Create async session factory
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
