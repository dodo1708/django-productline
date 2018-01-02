from __future__ import unicode_literals

from django_productline.composer import Composer


def select(composer: Composer) -> None:
    """
    binds the django_productline base feature
    """
    # no introductions or refinements necessary -
    # django_productline acts as base feature
    pass
