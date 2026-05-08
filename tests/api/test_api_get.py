
def test_api_get(playwright):
    request= playwright.request.new_context()
    response= request.get("https://reqres.in/api/users/1")
    
    assert response.status==200
    json_data = response.json()
    print(json_data)
    assert json_data["data"]["id"]==1
    print("API GET request successful and data verified.")
    