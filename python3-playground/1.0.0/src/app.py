import socket
import asyncio
import time
import random
import json
import smtplib
import ssl

from walkoff_app_sdk.app_base import AppBase

class PythonPlayground(AppBase):
    __version__ = "1.0.0"
    app_name = "Secuora email test"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    def send_mail(self, json_data): 
        return "Success"

    def run_me_2(self, json_data): 
        return "Ran function 2"

    def run_me_3(self, json_data): 
        return "Ran function 3"

    # Write your data inside this function
    def run_python_script(self, json_data, function_to_execute):
        # It comes in as a string, so needs to be set to JSON
        if not isinstance(json_data, list) and not isinstance(json_data, object) and not isinstance(json_data, dict):
            try:
                json_data = json.loads(json_data)
            except json.decoder.JSONDecodeError as e:
                return "Couldn't decode json: %s" % e

        # These are functions
        return this.send_mail(json_data)

if __name__ == "__main__":
    PythonPlayground.run()
