from app import create_app


class TestApi:

    def setup(self):
        app = create_app('flask_test.cfg')
        app.testing = True
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_streets(self):
        response = self.client.get('/api/v1/streets')
        assert response.status_code == 200

    def test_builds(self):
        response = self.client.get('/api/v1/builds/Барышникова')
        assert response.status_code == 200

    def test_flats(self):
        response = self.client.get('/api/v1/flats/Барышникова/1')
        assert response.status_code == 200

    def teardown(self):
        pass
