# Cursor AI template

## Frontend

- Frontend using the mantine vite template:

``` bash
git clone --depth 1 git@github.com:mantinedev/vite-min-template.git client
```
Run frontend:

```
$ yarn install
$ yarn dev --host
```

## Backend

- Backend using this minimal template:

```
https://github.com/luchog01/minimalistic-fastapi-template
```

Run backend:

``` bash
$ uv sync
$ uv run uvicorn src.minimal_template.main:app --reload --host 0.0.0.0 --port 8000
```

## Cursor

To instruct cursor, change `.cursor/rules` and `requirements/tasks.md`
