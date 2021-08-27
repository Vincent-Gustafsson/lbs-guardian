import json
import os

import discord


def get_schedule(uid=None, discord_id=None):
    if not uid:
        uid = get_shorthand(discord_id)
        if uid:
            return fetch_schedule_img(uid)

        return "Could not find shorthand."

    if is_valid_uid(uid):
        return fetch_schedule_img(uid)

    return "Invalid name."


def is_valid_uid(uid):
    # TODO I'm sorry, but I don't want to refactor this right now.
    schedules_folder = os.getenv("SCHEDULES_FOLDER")
    names = [name.lower() for name in os.listdir(schedules_folder)]
    return any(uid.lower() == name.split(".")[0] for name in names)


def fetch_schedule_img(uid):
    schedules_folder = os.getenv("SCHEDULES_FOLDER")
    with open(f"{schedules_folder}/{uid}.png", "rb") as img:
        return discord.File(img)


def get_shorthand(discord_id):
    shorthands_file = os.getenv("SHORTHANDS_JSON_FILE")
    with open(shorthands_file, 'r') as f:
        shorthands = json.load(f)

    if uid := shorthands.get(str(discord_id)):
        return uid

    return None
