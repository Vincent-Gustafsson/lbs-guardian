import json
import os


def get_cmd_prefix(client, message):
    return get_prefix(message.guild.id)


def get_prefix(guild_id):
    with open(os.getenv("PREFIXES_JSON_FILE"), "r") as f:
        prefixes = json.load(f)

    return prefixes[str(guild_id)]


def set_prefix(guild_id, prefix):
    # TODO Acts sus, Johannes pen test thing.
    if len(prefix) > 3:
        return False

    with open(os.getenv("PREFIXES_JSON_FILE"), "r") as f:
        prefixes = json.load(f)

        prefixes[str(guild_id)] = prefix

    with open(os.getenv("PREFIXES_JSON_FILE"), "w") as f:
        json.dump(prefixes, f, indent=4)

    return True


def remove_guild_prefix(guild_id):
    with open(os.getenv("PREFIXES_JSON_FILE"), "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild_id))

    with open(os.getenv("PREFIXES_JSON_FILE"), "w") as f:
        json.dump(prefixes, f, indent=4)
