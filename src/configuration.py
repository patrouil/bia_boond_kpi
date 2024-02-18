import json
import logging

"""

"""


class Configuration:

    def __init__(self, filename='conf/config.json') -> None:
        self.config = None
        self.logger = logging.getLogger(__name__)

        with open(filename, "r") as file:
            self.config = json.load(file)
        self.logger.debug("config is  %s", self.config)
        self.check_validity()
        return

    # end constructor

    def check_validity(self) -> None:
        assert (self.config.get('boond_host') is not None)
        return

    @property
    def boond_host(self) -> str:
        return self.config.get("boond_host")

    @property
    def client_key(self) -> str:
        return self.config.get("client_key")

    @property
    def client_token(self) -> str:
        return self.config.get("client_token")

    @property
    def user_token(self) -> str:
        return self.config.get("user_token")

    @property
    def outdir(self) -> str:
        return self.config.get("outdir", ".")

    @property
    def basename(self) -> str:
        return self.config.get("basename")

    @property
    def template(self) -> str:
        return self.config.get("template")

    @property
    def smtp(self) -> str:
        return self.config.get('smtp_host')

    @property
    def sender(self) -> str:
        return self.config.get('sender')

    @property
    def sender_password(self) -> str:
        return self.config.get('sender_password')

    @property
    def recipient(self) -> str:
        return self.config.get('recipient')

    @property
    def pole_id(self) -> str:
        return self.config.get('pole-id')

    @property
    def flag(self) -> str:
        return self.config.get('flag')

# end class
