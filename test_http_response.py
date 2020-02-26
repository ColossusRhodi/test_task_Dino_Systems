import pytest
import requests
from jsonschema import validate

"""Tests to verify GET request.

Test 'test_http_response_200' verify that response 200 for correct url.
Test 'test_http_response_404' verify that response 404 for incorrect url.
Test 'test_correct_json_body' verify that response has json body like model in database.
Test 'test_correct_json_data' verify that json has necessary data.
Test 'test_correct_http_headers' verify that response has correct headers.

test_http_response_200(url) takes argument 'url', it must be string with existent url address in app.
test_http_response_404(url) takes argument 'url', it must be string with nonexistent url address in app.
test_correct_json_body(url, schema) takes two arguments 'url' and 'schema'.
'url' must be string with existent url address in app, 'schema' must be a dict constructed like a model in database.

test_correct_json_data(url, json) takes two arguments 'url' and 'json'.
'url' must be string with existent url address in app, 'json' must be a dict constructed like a model in database
with existent data that corresponded by given name in url (/users?name=Izergil).

test_correct_http_headers(url, headers) takes two arguments 'url' and 'headers'.
'url' must be string with existent url address in app, 'headers' must be a dict constructed by requirements.

Enter yours test data for all tests! Presented test data is a fake!
"""

@pytest.mark.parametrize('url', [('http://test.com/')])
def test_http_response_200(url):
    response = requests.get(url)
    assert 200 == response.status_code

@pytest.mark.parametrize('url', [('http://test.com/')])
def test_http_response_404(url):
    response = requests.get(url)
    assert 404 == response.status_code

@pytest.mark.parametrize('url, schema', [('http://test.com/', 'schema')])
def test_correct_json_body(url, schema):
    response = requests.get(url)
    validate(instance=response.json(), schema=schema)

@pytest.mark.parametrize('url, json', [('http://test.com/', 'json')])
def test_correct_json_data(url, json):
    response = requests.get('http://some_domain.com/company/777/users?name=Izergil')
    assert json == response.json()

@pytest.mark.parametrize('url, headers', [('http://test.com/', 'headers')])
def test_correct_http_headers(url, headers):
    response = requests.get(url)
    assert headers == response.headers
