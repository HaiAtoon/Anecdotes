from storage import Storage
from configuration import Configuration
from typing import Dict, Tuple


class Parser:
    """
    Parse of every evidence data
    """

    def __init__(self, payload: Dict) -> None:
        self.payload = payload  # Payload per one evidence

    def save_new_evidence(self) -> None:
        """
        This function does several operation:
        1. identification and parsing of the payload
        2. Storing the data in the DB
        MAY RAISE EXCEPTIONS
        :return: None
        """
        config, parsed_data = self._identify_and_parse()
        if not config:
            raise ValueError("Un-recognized evidence type")
        try:
            Storage.set(config.get("collection"), parsed_data)
        except Exception as e:
            raise e

    def _identify_and_parse(self) -> Tuple:
        """
        This function does 2 operation:
        1. Identify the evidence type by the configuration
        2. Parse the data from the Payload as it described in the configuration
        :return: Tuple(config,data) - configuration data per evidence type, data that was parsed
        or None - configuration was not found
        """
        if self.payload.get("user_details") and self.payload.get("security"):
            evidence_config = Configuration.evidence_type_1
            # Creating the 'full_name' member
            self.payload["user_details"]["full_name"] = \
                self.payload["user_details"].pop("first_name") + \
                " " + self.payload["user_details"].pop("last_name")
            user_details_data = self.parse_evidence(self.payload["user_details"],
                                                    evidence_config.get('fields').get('user_details'))
            security_data = self.parse_evidence(self.payload["security"],
                                                evidence_config.get('fields').get('security'))
            return evidence_config, {**user_details_data, **security_data}

        return None, None

    @staticmethod
    def parse_evidence(data: Dict, config_fields: Dict) -> Dict:
        """
        Returns the data as described in the configuration
        :param data: Payload data of the evidence
        :param config_fields: The required fields in the config data
        :return: Parsed data
        """
        return dict(item for item in data.items() if item[0] in config_fields)

