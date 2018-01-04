# refinement for django_productline.settings

from __future__ import unicode_literals
import django
from django_productline import compare_version


from typing import List
def refine_INSTALLED_APPS(original: List[str]) -> List[str]:
    return ['django_productline.features.djpladmin', 'django.contrib.admin', ] + list(original)


introduce_ADMIN_URL = 'admin/'


def refine_DJANGO_TEMPLATE_CONTEXT_PROCESSORS(original: List[str]) -> List[str]:
    return list(original) + ['django_productline.features.djpladmin.context_processors.django_admin']


introduce_AUTH_GROUPS = {
    # {
    #     'name': 'Operator',
    #     'permissions': [
    #         ('add_mymodel', 'myapp'),
    #         ('change_my_model', 'myapp')
    #     ]
    # }
}

introduce_INITIAL_SUPERUSERS = [
    # dict(
    #    first_name='Toni',
    #    last_name='Michel',
    #    email='toni@schnapptack.de'
    # ),
]
