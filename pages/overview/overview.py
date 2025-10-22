import dash
from dash import dcc
import dash_mantine_components as dmc
from components.loader import loader_component

dash.register_page(__name__, path="/", title="Microburbs | Overview", order=1)

layout = dcc.Loading(
    id="loading-overview-page",
    children=[
        dmc.Grid(
            children=[
                dmc.GridCol(
                    children=[
                        dmc.Text(
                            "Suburb Market Overview",
                            size="xl",
                            fw=700,
                        ),
                        dmc.Text(
                            "Welcome to the Microburbs Analytics platform. Here you can explore comprehensive market data and insights to make informed decisions.",
                            size="md",
                            c="dimmed",
                        ),
                    ],
                    span=10,
                ),
                dmc.GridCol(
                    children=[
                        dmc.Select(
                            id="suburb-selection-overview",
                            placeholder="Choose a suburb",
                            nothingFoundMessage="No suburbs found",
                            searchable=True,
                            maxDropdownHeight=300,
                            value="Belmont North",
                            data=[
                                {"value": "Belmont North", "label": "Belmont North"}
                            ],
                            style={"width": "100%"},
                            radius="md",
                        )
                    ],
                    span=2,
                ),
                dmc.GridCol(
                    children=[
                        dmc.Title(
                            "Please select a suburb to view market insights.",
                            id="overview-suburb-market-insights-title",
                            size="32px",
                            fw=700,
                        )
                    ],
                    span=12,
                    mt="50px",
                ),
                dmc.GridCol(
                    children=[
                        dmc.SimpleGrid(
                            cols=5,
                            spacing="lg",
                            children=[
                                dmc.Paper(
                                    dmc.Stack([
                                        dmc.Text("Latest Median Price", fw=500, c="dimmed"),
                                        dmc.Text("", id="latest-median-price-suburb-overview", fw=700, size="xl"),
                                    ]),
                                    withBorder=True,
                                    shadow="sm",
                                    p="md",
                                    radius="lg",
                                ),
                                dmc.Paper(
                                    dmc.Stack([
                                        dmc.Text("Recent Growth (2 year)", fw=500, c="dimmed"),
                                        dmc.Text("", id="recent-growth-suburb-overview", fw=700, size="xl", c="green"),
                                    ]),
                                    withBorder=True,
                                    shadow="sm",
                                    p="md",
                                    radius="lg",
                                ),
                                dmc.Paper(
                                    dmc.Stack([
                                        dmc.Text("Gross Rental Yield", fw=500, c="dimmed"),
                                        dmc.Text("", id="rental-yield-suburb-overview", fw=700, size="xl", c="blue"),
                                    ]),
                                    withBorder=True,
                                    shadow="sm",
                                    p="md",
                                    radius="lg",
                                ),
                                dmc.Paper(
                                    dmc.Stack([
                                        dmc.Text("Population", fw=500, c="dimmed"),
                                        dmc.Text("12,400", fw=700, size="xl"),
                                    ]),
                                    withBorder=True,
                                    shadow="sm",
                                    p="md",
                                    radius="lg",
                                ),
                                dmc.Paper(
                                    dmc.Stack([
                                        dmc.Text("Risk Factor", fw=500, c="dimmed"),
                                        dmc.Text("Low", fw=700, size="xl", c="green"),
                                    ]),
                                    withBorder=True,
                                    shadow="sm",
                                    p="md",
                                    radius="lg",
                                ),
                            ],
                        )
                    ],
                    span=12,
                ),
            ],
            gutter=20,
        ),
    ],
    overlay_style={
        "visibility": "visible",
        "opacity": 0.5,
        "backgroundColor": "white",
    },
    custom_spinner=loader_component(title=None),
)