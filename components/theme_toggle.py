import dash_mantine_components as dmc
from dash_iconify import DashIconify


def theme_toggle():
    return dmc.Switch(
        offLabel=DashIconify(
            icon="material-symbols:wb-sunny-outline-rounded",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][8],
        ),
        onLabel=DashIconify(
            icon="material-symbols:nightlight-outline-rounded",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][5],
        ),
        id="color-scheme-toggle",
        persistence=True,
        color=dmc.DEFAULT_THEME["colors"]["dark"][3],
    )