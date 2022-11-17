prod:
	docker-compose -f docker-compose.yaml up -d --build
migrate:
	docker-compose -f docker-compose.yaml exec web alembic upgrade head
down:
	docker-compose -f docker-compose.yaml down