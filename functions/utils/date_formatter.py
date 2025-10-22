def date_formatter(date) -> str:
    return date.strftime("%d %b %Y")


def date_formatter_graphs(date) -> str:
    return date.strftime("%d_%m_%Y")


def datetime_formatter(date) -> str:
    return date.strftime("%d %b %Y %H:%M:%S")