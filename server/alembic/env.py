import asyncio
import importlib
import os
import sys
from logging.config import fileConfig
from pathlib import Path

from sqlalchemy.engine import Connection
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context
from minimal_template.core.config import settings
from minimal_template.core.database import Base

# Automatically import all models
backend_root_dir = Path(__file__).parent.parent
src_path = backend_root_dir / "src" / "minimal_template" / "api"
print(src_path)

for path in src_path.rglob("*.py"):
    if not path.name.endswith("models.py"):
        continue

    full_path_with_dot = str(path.relative_to(backend_root_dir)).replace(
        os.sep, "."
    )
    # cut trailing .py
    module_path = full_path_with_dot[:-3]
    # cut leading src.
    module_path = module_path[4:]
    print("Scanning module: ", module_path)

    try:
        importlib.import_module(module_path)
    except Exception as e:
        print(f"Failed to import {module_path}: {e}")

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set sqlalchemy.url
def get_url():
    """Get database URL from settings."""
    return str(settings.SQLALCHEMY_DATABASE_URI)

# Add your model's MetaData object here for 'autogenerate' support
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """In this scenario we need to create an Engine
    and associate a connection with the context."""

    configuration = config.get_section(config.config_ini_section, {})
    if configuration is not None:
        configuration["sqlalchemy.url"] = get_url()

    connectable = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
