import json
import os


def set_shorthand(discord_id, shorthand):
    with open(os.getenv("SHORTHANDS_JSON_FILE"), 'r') as f:
        shorthands = json.load(f)

    shorthands[str(discord_id)] = shorthand

    with open(os.getenv("SHORTHANDS_JSON_FILE"), 'w') as f:
        json.dump(shorthands, f, indent=4)


def get_shorthand(discord_id):
    with open(os.getenv("SHORTHANDS_JSON_FILE"), 'r') as f:
        shorthands = json.load(f)

    return shorthands.get(str(discord_id))
