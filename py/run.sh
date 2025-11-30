#!/bin/bash

# script
uv run python src/aoc2025/day1.py < ../inputs/day01.txt

# mypy
uv run mypy src

# ruff
uv run ruff check --fix srmt src
uv run ruff format src
