from dash import Input, Output
from functions.overview.overview import get_suburb_recent_growth, get_suburb_latest_median_price, get_suburb_rental_yield


def register_overview_callbacks(callback_manager):
    """Register all overview page callbacks."""
    
    @callback_manager.callback(
        Output("overview-suburb-market-insights-title", "children"), 
        Output("latest-median-price-suburb-overview", "children"),
        Output("recent-growth-suburb-overview", "children"),
        Output("rental-yield-suburb-overview", "children"),
        Input("suburb-selection-overview", "value")
    )
    def update_header_date_component(suburb_value):
        latest_median_price = get_suburb_latest_median_price(suburb_value)
        five_year_growth = get_suburb_recent_growth(suburb_value)
        rental_yield = get_suburb_rental_yield(suburb_value)

        return suburb_value, latest_median_price, five_year_growth, rental_yield