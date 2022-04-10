
import json
from csv import DictReader

with open("users.json", "r") as f:
    users = json.loads(f.read())

with open('books.csv', newline='') as f:
    reader = DictReader(f)
    iter_user = iter(users)
    for row in reader:
        try:
            current_user = next(iter_user)
        except StopIteration:
            iter_user = iter(users)
            current_user = next(iter_user)

        if "books" not in current_user:
            current_user["books"] = []

        current_user["books"].append({"title": row["Title"],
                                      "author": row["Author"],
                                      "pages": row["Pages"],
                                      "genre": row["Genre"]
                                      })

data = []
for user in users:
    data.append({
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": user["books"]
    })

with open("result.json", "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)
