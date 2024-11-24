import os
from pathlib import Path
from dotenv import load_dotenv


environment = os.environ.get('ENV', 'test')
os.environ['ENV'] = environment
env_path = Path('.') / f'.env.{environment}'
load_dotenv(dotenv_path=env_path, override=True)

BASE_URL = os.getenv('BASE_URL')
API_TOKEN = os.getenv('API_TOKEN')
ABSOLUTE_PATH = os.getenv('ABSOLUTE_PATH', '.')
