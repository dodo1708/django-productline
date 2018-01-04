from __future__ import unicode_literals

from ape import tasks


@tasks.register
@tasks.requires_product_environment
def type_module(*args):
    """
    call monkeytypes apply stuff. As it imports the modules it applies the typing,
    the product should be already composed.
    """
    import subprocess
    subprocess.check_call([
                              'monkeytype',
                              '-c',
                              'django_productline.features.djpl_typing.monkeytype_config:CONFIG',
                              'apply'
                          ] + list(args))
