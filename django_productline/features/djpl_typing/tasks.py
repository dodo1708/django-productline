from __future__ import unicode_literals

import importlib
import os
from subprocess import CalledProcessError

from ape import tasks
from featuremonkey import get_features_from_equation_file


@tasks.register
@tasks.requires_product_environment
def type_module(*args):
    """
    Call this task from the same directory where the monkeytype.sqlite3 database is placed.
    Call monkeytypes apply/stub stuff. As it imports the modules it applies the typing,
    the product should be already composed.
    """
    import subprocess
    subprocess.check_call(
        [
            'monkeytype',
            '-c',
            'django_productline.features.djpl_typing.monkeytype_config:CONFIG'
        ] + list(args)
    )


def get_abs_module_path(module):
    return os.path.abspath(module.__file__).replace('__init__.py', '')


def has_submodules(module):
    abs_module_path = get_abs_module_path(module)
    return os.path.isdir(abs_module_path)


def type_submodules(module):
    abs_module_path = get_abs_module_path(module)
    for submod in os.listdir(abs_module_path):
        if submod != '__pycache__':
            submod = submod.replace('.py', '')
            print('\033[94mTyping ' + module.__name__ + '.' + submod + '\033[0m')
            try:
                tasks.type_module('apply', module.__name__ + '.' + submod)
            except CalledProcessError:
                pass


@tasks.register
@tasks.requires_product_environment
def type_apply_all():
    """
    Call this task from the same directory where the monkeytype.sqlite3 database is placed.
    Tries to apply types to all active features.
    For every feature the following common modules are checked and typed if available:
        - models (incl. sub-modules)
        - forms (incl. sub-modules)
        - views (incl. sub-modules)
        - urls
        - utils
        - feature
        - templatetags (incl. sub-modules)
        - settings
        - assets
        - blockconfig
        - api
        - block
        - blocks
        - auth
        - signals
        - decorators
        - styles
        - admin (incl. sub-modules)
    Sub-module-check is relevant in case models etc. are structured like:
        models/
            __init__.py
            mymodel.py
            mymodel2.py
    and not in a models.py
    """
    print('\033[93m####################################################\033[0m')
    print('\033[93m# Get yourself a coffee, this may take a while ... #\033[0m')
    print('\033[93m####################################################\033[0m')
    from django.conf import settings
    equation_file = os.environ['PRODUCT_EQUATION_FILENAME']
    features = get_features_from_equation_file(equation_file)
    for feature in features:
        try:
            feature_module = importlib.import_module(feature)
            for module_name in settings.TYPED_MODULES:
                if hasattr(feature_module, module_name):
                    module = getattr(feature_module, module_name)
                    if has_submodules(module):
                        type_submodules(module)
                    else:
                        print('\033[94mTyping ' + feature + '.' + module_name + '\033[0m')
                        try:
                            tasks.type_module('apply', feature + '.' + module_name)
                        except CalledProcessError:
                            pass
        except ImportError:
            pass
