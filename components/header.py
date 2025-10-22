from datetime import datetime
import dash_mantine_components as dmc
from components.avatar import avatar
from components.theme_toggle import theme_toggle
from functions.utils.date_formatter import date_formatter


def update_date(date: str, is_initial: bool) -> dmc.Badge:
    """"""
    badge_color = "#1556B1"
    background_color = "#e9ecef"

    if is_initial:
        return dmc.Skeleton(
            h=20,
            w=120,
            radius="md",
            mt="2px",
            id="header-date-badge",
        )

    return dmc.Badge(
        date,
        color=badge_color,
        size="md",
        radius="xl",
        variant="dot",
        bd="none",
        bg=background_color,
        id="header-date-badge",
        style={
            "transition": "all 0.2s linear",
        },
    )


def header():
    """Create the header component."""

    return dmc.AppShellHeader(
        children=[
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.Image(
                                src="/assets/microburbs_logo.png",
                                alt="Microburbs Logo",
                                h="30px",
                                w="auto",
                            ),
                        ],
                        align="center",
                        justify="flex-start",
                        gap=0,
                    ),
                ],
                gap="5px",
                styles={
                    "root": {
                        "flexDirection": "row",
                        "alignItems": "baseline",
                    }
                },
            ),
            dmc.Group(
                children=[
                    dmc.Anchor(
                        "Overview",
                        href="/",
                        underline="hover",
                        style={"textDecoration": "none"},
                        fz="sm",
                    ),
                ],
                gap="xl",
                justify="flex-start",
                align="center",
                style={
                    "flexGrow": 1,
                },
            ),
            dmc.Group(
                children=[
                    theme_toggle(),
                    dmc.Flex(
                        children=[
                            update_date(
                                date=date_formatter(datetime.now().date()),
                                is_initial=True,
                            )
                        ],
                        id="header-date-content",
                    ),
                    dmc.Flex(
                        avatar(name=""),
                        id="header-avatar-component",
                    ),
                ]
            ),
        ],
        style={
            "position": "fixed",
            "backgroundPosition": "center",
            "backgroundSize": "cover",
            "transitionDelay": "0s, 0s, 0s, 0s",
            "transitionDuration": "0.25s, 0.25s, 0.25s, 0s",
            "transitionProperty": "box-shadow, background-color, filter, border",
            "transitionTimingFunction": "linear, linear, linear, linear",
            "alignItems": "center",
            "display": "flex",
            "minHeight": "75px",
            "height": "30px",
            "justifyContent": "space-between",
            "gap": "70px",
            "marginX": "auto",
            "paddingX": "15px",
            "zIndex": "999",
        },
        withBorder=True,
        pl={
            "base": "20px",
            "xs": "20px",
            "sm": "50px",
            "md": "75px",
            "lg": "100px",
            "xl": "100px",
        },
        pr={
            "base": "20px",
            "xs": "20px",
            "sm": "50px",
            "md": "75px",
            "lg": "100px",
            "xl": "100px",
        },
    )