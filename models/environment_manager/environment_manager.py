import os
from dotenv import load_dotenv


class EnvironmentManager:
    def __init__(self):
        load_dotenv()
        self.environment = os.environ.get("ENVIRONMENT")
        self.access_token = os.environ.get("API_ACCESS_TOKEN")

    def get_environment(self):
        env = (
            "nprd"
            if self.environment == "nprd" or self.environment == "local"
            else "prod"
        )
        return env

    def get_is_local(self):
        return True if self.environment == "local" else False
    
    def get_access_token(self):
        return self.access_token