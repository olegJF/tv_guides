import os
from pathlib import Path

BASE_DIR = Path.cwd()
env_file = BASE_DIR.joinpath('.env')

if Path(env_file).exists():
    from dotenv import load_dotenv
    load_dotenv()

TOKEN = os.getenv("TOKEN")
admin_id = os.getenv("admin_id")
api_url = os.getenv("api_url")
