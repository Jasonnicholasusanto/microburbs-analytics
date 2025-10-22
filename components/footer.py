import dash_mantine_components as dmc
from datetime import datetime
from functions.global_variables import app_version


def footer() -> dmc.AppShellFooter:
    current_year = datetime.now().year
    copyright_text = (
        f"© {current_year} Microburbs Analytics Dashboard. All Rights Reserved."
    )

    footer_text_color = "#B6C4D6"
    return dmc.AppShellFooter(
        children=[
            dmc.Stack(
                children=[
                    dmc.Text(
                        copyright_text,
                        mb={
                            "base": "20px",
                            "xs": "20px",
                            "sm": "0px",
                            "md": "0px",
                            "lg": "0px",
                            "xl": "0px",
                        },
                        ta={
                            "base": "center",
                            "xs": "center",
                            "sm": "start",
                            "md": "start",
                            "lg": "start",
                            "xl": "start",
                        },
                        w="100%",
                        style={
                            "fontSize": "13px",
                            "color": footer_text_color,
                        },
                    ),
                    dmc.Text(
                        f"Version {app_version}",
                        size="xs",
                    ),
                ],
                gap="5px",
            ),
            dmc.Anchor(
                dmc.Text(
                    "Support", style={"fontSize": "13px", "color": footer_text_color}
                ),
                href="/support",
            ),
        ],
        style={
            "zIndex": 3,
            "paddingLeft": "50px",
            "paddingRight": "50px",
            "paddingBottom": "20px",
            "paddingTop": "20px",
            "justifyContent": "space-between",
            "display": "flex",
            "alignItems": "center",
            "position": "relative",
            "backgroundColor": "#04264f",
        },
        w="100%",
    )