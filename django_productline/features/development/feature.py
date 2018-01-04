from django_productline.composer import Composer
def select(composer: Composer) -> None:
    # compose settings
    import django_productline.settings
    from . import settings
    composer.compose(settings, django_productline.settings)
