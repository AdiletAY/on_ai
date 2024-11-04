#!/bin/bash

alembic upgrade head

uvicorn core.main:app --host 0.0.0.0 --port 8080 --reload
