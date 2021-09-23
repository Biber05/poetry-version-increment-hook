
PMP = python -m poetry run

fmt:
	$(PMP) black .

test:
	$(PMP) pytest .
