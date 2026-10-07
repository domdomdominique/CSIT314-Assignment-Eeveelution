from app.entity.idp import IDP


class SearchIDPController:
    """Control: handles the Customer 'Search IDP' use case."""

    def search(self, keyword):
        return IDP.search(keyword)
