import json

pros = {"ceux-ci": {
    "genre": "m",
    "pl": True
  },
  "celles-ci": {
    "genre": "f",
    "pl": True
  },
  "celles-là": {
    "genre": "f",
    "pl": True
  },
  "celle-ci": {
    "genre": "f",
    "pl": False
  },
  "celle-là": {
    "genre": "f",
    "pl": False
  },
  "ceux-là": {
    "genre": "m",
    "pl": True
  },
  "celui-ci": {
    "genre": "m",
    "pl": False
  },
  "celui-là": {
    "genre": "m",
    "pl": False
  }
}

with open('../words/pronouns/demo.json', 'w', encoding='UTF-8') as f:
    json.dump(pros, f, indent=2)