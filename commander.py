from slugify import slugify


class Commander:
    # init method or constructor
    def __init__(self, name, colors, deck_url):
        self._name = name
        self._colors = colors
        self._deck_url = deck_url

    """
	name property
	"""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    """
	colors property
	"""

    @property
    def colors(self):
        return self._colors

    @colors.setter
    def colors(self, value):
        self._colors = value

    """
	deck_url property
	"""

    @property
    def deck_url(self):
        return self._deck_url

    @deck_url.setter
    def deck_url(self, value):
        self._deck_url = value

    """
	name_slug property
	"""

    @property
    def name_slug(self):
        return slugify(self.name)
