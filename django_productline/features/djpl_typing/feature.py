from __future__ import unicode_literals

from django_productline.composer import Composer


def select(composer: Composer) -> None:
    import django_productline.startup
    from . import startup
    composer.compose(startup, django_productline.startup)
