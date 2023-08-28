def filter_custom_fields(answers):
    """Filtra las respuestas basadas en el campo custom_field."""
    return [answer for answer in answers if answer["custom_field"] not in [None, '']]
