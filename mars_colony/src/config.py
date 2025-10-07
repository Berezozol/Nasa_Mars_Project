# Configuration for Mars Colony project

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

NASA_API_KEY = os.getenv('NASA_API_KEY')
