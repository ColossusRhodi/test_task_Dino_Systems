import pytest
import requests
from jsonschema import validate


@pytest.mark.parametrize('url', [('http://some_domain.com/company/777/users?name=Izergil')])
def test_http_response_200(requests_mock, url):
    requests_mock.get(url)
    response = requests.get(url)
    assert 200 == response.status_code

@pytest.mark.parametrize('url', [('http://some_domain.com/company/777/users?name=Maxim')])
def test_http_response_404(requests_mock, url):
    requests_mock.get(url, status_code=404)
    response = requests.get(url)
    assert 404 == response.status_code

schema = {'type': 'object',
          'properties': {'id': {'type': 'number'},
                         'first_name': {'type': 'string'},
                         'last_name': {'type': ['string', 'null']},
                         'office': {'type': ['string', 'null']},
                         'contact_info': {'type': 'array',
                                          'items': {'phone': {'type': 'number'},
                                                    'email': {'type': 'string', 'format': 'email'}
                                                    }
                                          }
                         }
          }

json = {'id': 1,
        'first_name': 'Izergil',
        'last_name': None,
        'office': 'IT',
        'contact_info': [{'phone': 3625550100,
                          'email': 'IT_Izergil@mail.com'}]
        }

@pytest.mark.parametrize('url, json, schema', [('http://some_domain.com/company/777/users?name=Izergil', json, schema)])
def test_correct_json_schema(requests_mock, url, json, schema):
    requests_mock.get(url=url, json=json)
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)

@pytest.mark.parametrize('url, json', [('http://some_domain.com/company/777/users?name=Izergil', json)])
def test_correct_json_data(requests_mock, url, json):
    requests_mock.get(url, json=json)
    response = requests.get('http://some_domain.com/company/777/users?name=Izergil')
    assert json == response.json()

headers = {'Server': 'some_domain.com',
           'Content-Type': 'application/json; charset=utf-8'
           }

@pytest.mark.parametrize('url, headers', [('http://some_domain.com/company/777/users?name=Izergil', headers)])
def test_correct_http_headers(requests_mock, url, headers):
    requests_mock.get(url, headers=headers)
    response = requests.get(url)
    assert headers == response.headers
