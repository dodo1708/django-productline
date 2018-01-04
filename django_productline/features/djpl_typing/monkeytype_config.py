from typing import Iterator

from contextlib import contextmanager
from monkeytype.config import DefaultConfig


class DjplConfig(DefaultConfig):

    @contextmanager
    def cli_context(self, command: str) -> Iterator[None]:
        """
        Call monkeytype in cli like this:
            monkeytype -c django_productline.features.djpl_typing.monkeytype_config:CONFIG apply/stub some.module
        :param command:
        :return:
        """
        from django_productline import startup
        startup.select_product()
        yield


CONFIG = DjplConfig()
