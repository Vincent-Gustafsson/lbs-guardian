import pathlib
import shutil
import os


def init_schedules_folders():
    try:
        schedules_folder = pathlib.Path(os.getenv('SCHEDULES_FOLDER'))
        shutil.move(schedules_folder, str(schedules_folder) + "_tmp")
        os.mkdir(schedules_folder)

    except FileNotFoundError:
        os.mkdir(schedules_folder)


def cleanup_schedules_folders():
    SCHEDULES_FOLDER = os.getenv('SCHEDULES_FOLDER')
    shutil.rmtree(SCHEDULES_FOLDER + "_tmp")
