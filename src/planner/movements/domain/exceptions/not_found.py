from src.shared.domain.exceptions.not_found import NotFound


class MovementNotFound(NotFound):
    def __init__(self):
        # TODO: Use I18n To translations
        super().__init__("Movement not found.")
