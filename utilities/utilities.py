# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot

import os
import json
from pathlib import Path
import signal
import sys
import os

MODULE_DIR = Path(__file__).resolve().parents[1]
MASTER_CRYPTO_FARM_BOT_DIR = Path(__file__).resolve().parents[3]
sys.path.append(str(MASTER_CRYPTO_FARM_BOT_DIR))

from utils.database import Database


def getConfig(key, default=None):
    json_file = os.path.join(MODULE_DIR, "bot_settings.json")

    if not os.path.exists(json_file):
        return default

    with open(json_file, "r") as f:
        data = json.load(f)
        if key in data:
            return data[key]
        else:
            return default


def is_module_disabled(bot_globals, log):
    db = Database(bot_globals["mcf_dir"] + "/database.db", log)
    module_name = bot_globals["module_name"]
    is_disabled = db.getSettings(f"{module_name}_disabled", "0") == "1"
    return is_disabled == True or is_disabled == "1"


def kill_process():
    try:
        os.kill(os.getpid(), signal.SIGINT)
    except Exception as e:
        pass
    try:
        os.kill(os.getpid(), signal.SIGTERM)
    except Exception as e:
        pass
    exit(0)
