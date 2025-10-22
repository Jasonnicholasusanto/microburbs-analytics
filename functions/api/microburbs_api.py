import requests
from functions.global_variables import microburbs_base_api_url
from models.environment_manager.environment_manager import EnvironmentManager

def fetch_suburb_market_insights(suburb: str) -> dict:
    """Fetch market insights for a given suburb from an external API."""
    environment_manager = EnvironmentManager()
    access_token = environment_manager.get_access_token()
    api_url = f"{microburbs_base_api_url}/suburb/market"
    params = {
        "suburb": suburb
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(api_url, params=params, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}