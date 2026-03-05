up:
	docker compose up -d

down:
	docker compose down -v

logs:
	docker compose logs -f

test:
	pytest tests/