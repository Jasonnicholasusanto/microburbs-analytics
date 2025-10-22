import dash_mantine_components as dmc


def avatar(name: str, color="#67bed9", bg="rgba(255, 255, 255, 0.5)") -> dmc.Avatar:
    """Create the avatar component."""

    if name == "":
        return dmc.Tooltip(
            dmc.Avatar(
                id="header-avatar",
                radius="xl",
                color="gray",
                size="md",
                bg=bg,
            ),
            label="Not logged in",
            withArrow=True,
            arrowPosition="center",
            arrowSize=7,
            zIndex="1000",
            style={
                "transition": "all 0.2s linear",
            },
        )

    return dmc.Tooltip(
        dmc.Avatar(
            id="header-avatar",
            name=name,
            fw="800",
            radius="xl",
            color=color,
            size="md",
            bg=bg,
        ),
        label=name,
        withArrow=True,
        arrowPosition="center",
        arrowSize=7,
        zIndex="1000",
        style={
            "transition": "all 0.2s linear",
        },
    )