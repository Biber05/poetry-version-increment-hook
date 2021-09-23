
PMP = python -m poetry run

fmt:
	$(PMP) black .

test:
	$(PMP) pytest .

build: test fmt
	 python -m poetry build