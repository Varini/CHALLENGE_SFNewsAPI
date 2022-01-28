from operator import index
from fastapi.testclient import TestClient
from index import app

client = TestClient(app)


def test_get_item():
    response = client.get("/articles/13766")
    assert response.status_code == 200
    assert response.json() == {
        "id": 13766,
        "title": "No commercial crew test flights expected this year",
        "url": "https://spaceflightnow.com/2018/10/06/no-commercial-crew-test-flights-expected-this-year/",
        "imageUrl": "https://mk0spaceflightnoa02a.kinstacdn.com/wp-content/uploads/2018/10/ccp-countdown-header-326x245.jpg",
        "newsSite": "Spaceflight Now",
        "summary": "",
        "publishedAt": "2018-10-05T22:00:00.000Z",
        "updatedAt": "2021-05-18T13:43:19.589Z",
        "featured": False,
        "launches": [],
        "events": []
    }


def test_get_invalid_id():
    id = 9999999999
    response = client.get(f"/articles/{id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Article ID: {id} not found"}


def test_get_non_integer_id():
    response = client.get("/articles/abc")
    assert response.status_code == 422
    assert response.json()[
        "detail"][0]["msg"] == "value is not a valid integer"


def test_create_item():
    response = client.post("/articles/",
                           json={
                               "title": "No commercial crew test flights expected this year",
                               "url": "https://spaceflightnow.com/2018/10/06/no-commercial-crew-test-flights-expected-this-year/",
                               "imageUrl": "https://mk0spaceflightnoa02a.kinstacdn.com/wp-content/uploads/2018/10/ccp-countdown-header-326x245.jpg",
                               "newsSite": "Spaceflight Now",
                               "summary": "",
                               "publishedAt": "2018-10-05T22:00:00.000Z",
                               "updatedAt": "2021-05-18T13:43:19.589Z",
                               "featured": False,
                               "launches": [],
                               "events": []
                           }
                           )
    request = client.get("/articles/?page_size=1")
    id = request.json()[0]["id"]
    assert response.status_code == 201
    assert response.json() == {
        "id": id,
        "title": "No commercial crew test flights expected this year",
        "url": "https://spaceflightnow.com/2018/10/06/no-commercial-crew-test-flights-expected-this-year/",
        "imageUrl": "https://mk0spaceflightnoa02a.kinstacdn.com/wp-content/uploads/2018/10/ccp-countdown-header-326x245.jpg",
        "newsSite": "Spaceflight Now",
        "summary": "",
        "publishedAt": "2018-10-05T22:00:00.000Z",
        "updatedAt": "2021-05-18T13:43:19.589Z",
        "featured": False,
        "launches": [],
        "events": []
    }


def test_update_item():
    request = client.get("/articles/?page_size=1")
    id = request.json()[0]["id"]
    response = client.put(f"/articles/{id}",
                          json={
                              "title": "Altered Title",
                              "url": "www.domain.com",
                              "imageUrl": "IMAGE.img",
                              "newsSite": "",
                              "summary": "",
                              "publishedAt": "2018-10-05T22:00:00.000Z",
                              "updatedAt": "2021-05-18T13:43:19.589Z",
                              "featured": True,
                              "launches": [
                                  {
                                       "id": "Altered",
                                       "provider": "Altered Launch"
                                  }
                              ],
                              "events": [
                                  {
                                      "id": 1037,
                                      "provider": "Altered Provider"
                                  }
                              ]
                          }
                          )
    assert response.status_code == 200
    assert response.json() == {
        "id": id,
        "title": "Altered Title",
        "url": "www.domain.com",
        "imageUrl": "IMAGE.img",
        "newsSite": "",
        "summary": "",
        "publishedAt": "2018-10-05T22:00:00.000Z",
        "updatedAt": "2021-05-18T13:43:19.589Z",
        "featured": True,
        "launches": [
            {
                "id": "Altered",
                "provider": "Altered Launch"
            }
        ],
        "events": [
            {
                "id": 1037,
                "provider": "Altered Provider"
            }
        ]
    }


def test_update_invalid_id():
    id = 9999999999
    response = client.put(f"/articles/{id}",
                          json={
                              "title": "Altered Title"
                          }
                          )
    assert response.status_code == 404
    assert response.json() == {"detail": f"Article ID: {id} not found"}


def test_update_non_integer_id():
    response = client.put("/articles/abc")
    assert response.status_code == 422
    assert response.json()[
        "detail"][0]["msg"] == "value is not a valid integer"

def test_delete_item():
    request = client.get("/articles/?page_size=1")
    id = request.json()[0]["id"]
    response = client.delete(f"/articles/{id}")
    assert response.status_code == 200
    assert response.json() == f"Article ID: {id} was deleted."

def test_delete_invalid_id():
    id = 9999999999
    response = client.delete(f"/articles/{id}")
    assert response.status_code == 404
    assert response.json() == {"detail": f"Article ID: {id} not found"}


def test_delete_non_integer_id():
    response = client.delete("/articles/abc")
    assert response.status_code == 422
    assert response.json()[
        "detail"][0]["msg"] == "value is not a valid integer"    
