"""
запуск отдельных тестов
pytest tests/test_app.py::TestApi::test_get_payments

"""
from bill18 import create_app
import pytest
import json

test_data_builds = [
    'Барышникова',
    '30 лет Победы',
]

test_data_flats = [
    ('Барышникова', '3'),
    ('30 лет Победы', '33'),
]

test_data_lics = [
    ('Барышникова', '3', '1'),
    ('30 лет Победы', '33', '99'),
]

test_data_occ = [350033100, 33100]
test_data_occ_fail = [2345]


def response_json(response):
    return json.loads(response.get_data(as_text=True))


class TestApi:

    def setup(self):
        app = create_app('config.TestingConfig')
        app.testing = True
        self.client = app.test_client()
        self.api = app.config['API']

    def test_index(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_get_streets(self):
        response = self.client.get(f'{self.api}/streets')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
        response_body = response_json(response)  # response_body = response.json()
        print(len(response_body["dataStreets"]))
        assert len(response_body["dataStreets"]) > 0

    @pytest.mark.parametrize('street_name', test_data_builds)
    def test_get_builds(self, street_name):
        response = self.client.get(f'{self.api}/builds/{street_name}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
        response_body = response_json(response)
        assert len(response_body["dataBuilds"]) > 0

    @pytest.mark.parametrize('street_name, nom_dom', test_data_flats)
    def test_get_flats(self, street_name, nom_dom):
        response = self.client.get(f'{self.api}/flats/{street_name}/{nom_dom}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
        response_body = response_json(response)
        assert len(response_body["dataKvr"]) > 0

    @pytest.mark.parametrize('street_name, nom_dom, nom_kvr', test_data_lics)
    def test_get_lics(self, street_name, nom_dom, nom_kvr):
        response = self.client.get(f'{self.api}/lics/{street_name}/{nom_dom}/{nom_kvr}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
        response_body = response_json(response)
        assert len(response_body["dataKvrLic"]) > 0

    @pytest.mark.parametrize('lic', test_data_occ)
    def test_get_occ(self, lic):
        response = self.client.get(f'{self.api}/lic/{lic}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"

    @pytest.mark.parametrize('lic', test_data_occ)
    def test_get_pu(self, lic):
        response = self.client.get(f'{self.api}/infoDataCounter/{lic}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
        response_body = response_json(response)
        assert len(response_body["dataCounter"]) > 0

    @pytest.mark.parametrize('lic', test_data_occ)
    def test_get_ppu(self, lic):
        response = self.client.get(f'{self.api}/infoDataCounterValue/{lic}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
        response_body = response_json(response)
        assert len(response_body["dataCounterValue"]) > 0

    @pytest.mark.parametrize('lic', test_data_occ)
    def test_get_values(self, lic):
        response = self.client.get(f'{self.api}/infoDataValue/{lic}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
        response_body = response_json(response)
        assert len(response_body["dataValue"]) > 0

    @pytest.mark.xfail(strict=True)
    @pytest.mark.parametrize('lic', [2345])
    def test_get_values_fail(self, lic):
        response = self.client.get(f'{self.api}/infoDataValue/{lic}')
        response_body = response_json(response)
        assert len(response_body["dataValue"]) == 0

    @pytest.mark.parametrize('lic', test_data_occ)
    def test_get_payments(self, lic):
        response = self.client.get(f'{self.api}/infoDataPaym/{lic}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
        response_body = response_json(response)
        assert len(response_body["dataPaym"]) > 0

    @pytest.mark.parametrize('pu_id, value', [('65669', '300'), ('65669', '300.2')])
    def test_pu_add_value_get(self, pu_id, value):
        response = self.client.get(f'{self.api}/puAddValue/{pu_id}/{value}')
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"

    @pytest.mark.parametrize('pu_id, value', [('65669', '300')])
    def test_pu_add_value(self, pu_id, value):
        params = {"pu_id": pu_id, "value": value}
        response = self.client.post(f'{self.api}/puAddValue', json=params)
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"

    def teardown(self):
        pass
