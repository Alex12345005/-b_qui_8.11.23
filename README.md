# -b_qui_8.11.23
API token qaH67KfdJCScoeK4pScbJYoFQQ0z

    response = requests.post(url, headers=headers, data=payload, verify=False)
    response_json = response.json()
    results = {}
    for varr, resp in zip(var, response_json):
        print(resp)
        results[varr["name"]] = resp["result"]