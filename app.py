from dash import Dash, Input, Output, clientside_callback, dcc, page_container, html
import dash_mantine_components as dmc
from components.footer import footer
from components.header import header
from callbacks.callbacks import callback_manager


app = Dash(__name__, use_pages=True)
callback_manager.attach_to_app(app)


app.layout = dmc.MantineProvider(
    forceColorScheme="light",
    theme={
        "fontFamily": "'proxima-nova', sans-serif",
        "breakpoints": {
            "base": "0em",
            "xs": "48em",
            "sm": "62em",
            "md": "96em",
            "lg": "116em",
            "xl": "120em",
        },
    },
    children=[
        dmc.AppShell(
            id="appshell",
            children=[
                dcc.Location(id="location-url"),
                dcc.Store(id="theme-preference", data="light", storage_type="local"),
                html.Div(
                    id="notifications-container",
                ),
                header(),
                dmc.AppShellMain(
                    dmc.Box(
                        page_container,
                        id="app-page-container",
                        p={
                            "base": "20px",
                            "xs": "20px",
                            "sm": "50px",
                            "md": "75px",
                            "lg": "100px",
                            "xl": "100px",
                        },
                        pt={
                            "base": "180px",
                            "xs": "180px",
                            "sm": "120px",
                            "md": "120px",
                            "lg": "120px",
                            "xl": "120px",
                        },
                        h="100%",
                        w="100%",
                        style={
                            "marginX": "auto",
                        },
                    ),
                ),
                footer(),
            ],
            style={"transition": "all 0.2s linear"},
        )
    ],
)

clientside_callback(
    """ 
    (switchOn) => {
        document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');  
        return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-toggle", "checked"),
    Input("color-scheme-toggle", "checked"),
)

clientside_callback(
    """
    function() {
        const prefersDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return prefersDarkMode ? 'dark' : 'light';
    }
    """,
    Output("theme-preference", "data"),
    Input("location-url", "pathname"),
)

app.title = "Microburbs Analytics"


if __name__ == "__main__":
    app.run(debug=True, port=8000)