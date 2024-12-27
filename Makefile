# Makefile
.PHONY: typing
typing:
	poetry run mypy . --disable-error-code=empty-body