from typing import Optional
import dash_mantine_components as dmc


def loader_component(title: Optional[str]):
    """"""
    c = "#2274E8"
    children = []

    if title is None:
        children = [
            dmc.Loader(color=c, size="md", type="dots"),
        ]
    else:
        children = [
            dmc.Loader(color=c, size="md", type="dots"),
            dmc.Text(
                children=title,
                mt="xs",
            ),
        ]

    return dmc.Stack(
        align="center",
        justify="center",
        children=children,
        style={
            "zIndex": 999,
        },
    )