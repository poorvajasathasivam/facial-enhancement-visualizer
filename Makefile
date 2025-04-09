echo "# Makefile for common tasks

.PHONY: setup-conda setup-frontend start-backend start-model start-frontend docker-build docker-up docker-down

# Setup conda environment
setup-conda:
	conda env create -f environment.yml

# Setup frontend
setup-frontend:
	cd frontend && npm install

# Start backend
start-backend:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Start model service
start-model:
	cd model && python api.py

# Start frontend
start-frontend:
	cd frontend && npm start

# Docker commands
docker-build:
	docker-compose build

docker-up:
	docker-compose up

docker-down:
	docker-compose down

# Clean up
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
