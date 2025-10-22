from typing import Optional
import requests
from functions.global_variables import microburbs_base_api_url
from models.environment_manager.environment_manager import EnvironmentManager


def fetch_suburb_market_insights(
    suburb: str,
    metric: Optional[str] = "price",
    property_type: Optional[str] = "house",
    growth_period: Optional[str] = "1y"
) -> dict:
    """
    Fetch market insights for a given suburb from the Microburbs API.

    Args:
        suburb (str): Name of the suburb.
        metric (Optional[str]): e.g. "price", "rent".
        property_type (Optional[str]): e.g. "house", "unit".
        growth_period (Optional[str]): e.g. "5y", "1y".

    Returns:
        dict: JSON response from the API or an error message.
    """
    environment_manager = EnvironmentManager()
    access_token = environment_manager.get_access_token()
    api_url = f"{microburbs_base_api_url}/suburb/market"

    # Base query params
    params = {"suburb": suburb}

    # Add optional params only if provided
    if metric:
        params["metric"] = metric
    if property_type:
        params["property_type"] = property_type
    if growth_period:
        params["growth_period"] = growth_period

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data: {str(e)}"}
