from datetime import timedelta
from functions.api.microburbs_api import fetch_suburb_market_insights
import pandas as pd


def get_suburb_latest_median_price(suburb: str) -> str:
    """Get the latest median price for a given suburb."""
    if suburb is None:
        return "N/A"
    
    market_insights = fetch_suburb_market_insights(suburb, )
    # 1. Flatten the nested results
    records = market_insights["results"][0]        # first (and only) list of time series
    df = pd.DataFrame(records)

    # 2. Convert date strings to datetime so we can sort chronologically
    df["date"] = pd.to_datetime(df["date"])

    # 3. Sort and take the last (most recent) observation
    df = df.sort_values("date")
    latest_row = df.iloc[-1]

    # 4. Extract the suburb's latest median value
    latest_median_price = latest_row["value"]

    return f"${latest_median_price:,.2f}"

def get_suburb_recent_growth(suburb: str) -> str | None:
    """Calculate 5-year median price growth (in percent) for a suburb."""
    try:
        market_insights = fetch_suburb_market_insights(suburb)

        records = market_insights["results"][0]
        df = pd.DataFrame([
            {"date": pd.to_datetime(r["date"]), "value": r["value"]}
            for r in records
        ]).sort_values("date")

        # Define 5 years ago from latest date
        latest_date = df["date"].iloc[-1]
        five_years_ago = latest_date - timedelta(days=2 * 365)

        # Find the closest data point to 5 years ago
        past_df = df[df["date"] <= five_years_ago]
        if past_df.empty:
            return None  # not enough data

        past_value = past_df["value"].iloc[-1]
        latest_value = df["value"].iloc[-1]

        growth_pct = ((latest_value - past_value)/ past_value) * 100
        return f"{growth_pct:,.2f}%"

    except Exception:
        return None

def get_suburb_rental_yield(suburb: str):
    # --- 1. Get median sell price ---
    market_insights = fetch_suburb_market_insights(suburb, metric="price")
    sell_price = pd.DataFrame(market_insights["results"][0])
    sell_price["date"] = pd.to_datetime(sell_price["date"])
    sell_price = sell_price.sort_values("date")
    latest_price = sell_price["value"].iloc[-1]

    # --- 2. Get median rent ---
    market_insights = fetch_suburb_market_insights(suburb, metric="rent")
    rent_price = pd.DataFrame(market_insights["results"][0])
    rent_price["date"] = pd.to_datetime(rent_price["date"])
    rent_price = rent_price.sort_values("date")
    latest_rent = rent_price["value"].iloc[-1]

    # --- 3. Compute rental yield ---
    annual_rent = latest_rent * 52
    rental_yield = (annual_rent / latest_price) * 100

    return f"{rental_yield:,.2f}%", latest_price, latest_rent