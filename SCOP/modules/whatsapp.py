def scan(phone):
    return {
        "platform": "whatsapp",
        "username": None,
        "country": phone[:3],
        "followers": [],
        "following": [],
        "comments": [],
        "metadata": {
            "phone": phone
        }
    }
