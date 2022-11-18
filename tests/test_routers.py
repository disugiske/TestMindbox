import unittest
from httpx import AsyncClient

from routers.products_cat import router as prod_cat_router
from main import app

events = []

class TestUser(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        events.append("setUp")

    async def asyncSetUp(self):
        self.client = AsyncClient(app=app.include_router(prod_cat_router), base_url="http://localhost:8000")
        events.append("asyncSetUp")

    async def test_all(self):
        response = await self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'please add arguments like: /add?cat=5&prod=10')

    async def test_category(self):
        response = await self.client.get("/api/v1/category")
        self.assertEqual(response.status_code, 200)


    async def test_pair(self):
        response = await self.client.get("/api/v1/pair")
        self.assertEqual(response.status_code, 200)
