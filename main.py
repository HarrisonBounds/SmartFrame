import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"sk-ht0xT3BQMMuesKhCeKBAHigToeqLpkYjSmHyEHdgQ0P9F40i",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "a camel smoking a cigarette",
        "output_format": "webp",
    },
)

if response.status_code == 200:
    with open("./lighthouse.webp", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))