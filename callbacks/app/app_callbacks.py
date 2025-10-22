from datetime import datetime
import dash_mantine_components as dmc
from dash import Input, Output
from components.avatar import avatar
from components.header import update_date
from functions.utils.date_formatter import date_formatter


def register_app_callbacks(callback_manager):
    """Register all app callbacks."""

    @callback_manager.callback(
        Output("header-date-content", "children"), Input("location-url", "pathname")
    )
    def update_header_date_component(pathname) -> dmc.Title:
        """Update the header component."""
        date = date_formatter(datetime.now().date())

        if pathname:
            return update_date(date=date, is_initial=False)
        else:
            return update_date(date=date, is_initial=True)

    @callback_manager.callback(
        Output("header-date-badge", "bg"),
        Input("color-scheme-toggle", "checked"),
    )
    def update_header_style(checked):
        if checked:
            return dmc.DEFAULT_THEME["colors"]["dark"][3]
        else:
            return "#e9ecef"

    @callback_manager.callback(
        Output("header-avatar-component", "children"),
        Input("location-url", "pathname"),
        Input("color-scheme-toggle", "checked"),
        prevent_initial_call="initial_duplicate",
    )
    def update_user_avatar(pathname: str, theme: bool) -> dmc.Avatar:
        """Update the user avatar component. For Authentication future use."""
        return avatar(
            name="",
            bg="#e9ecef" if not theme else dmc.DEFAULT_THEME["colors"]["dark"][3],
        )