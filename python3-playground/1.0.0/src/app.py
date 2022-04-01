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
    app_name = "python_playground"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        super().__init__(redis, logger, console_logger)

    def send_mail(self, json_data): 
	params = json_data
	if("sender_email" not in params or "sender_password" not in params or "msg" not in params or "dest_email" not in params or "subject" not in params): 
		return "ERROR: Missing required fields"

	message = """From: From Person <{0}>
To: To Person <{1}>
Subject: {2}

{3}
"""

	smtp_server = "smtp.gmail.com"
	port 587

	context = ssl.create_default_context()

	try:
		server = smtplib.SMTP(smtp_server, port)
		server.ehlo()
		server.starttls(context=context)
		server.ehlo()
		server.login(params["sender_email"], params["sender_password"])
		server.sendmail(params["sender_email"], params["dest_email"], message.format(params["sender_email"], params["dest_email"], params["subject"], params["msg"]))

	except Exception as e:
		return(e)
	finally:
		server.quit()

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
        switcher = {
            "Send_Mail" : self.send_mail
        }

        func = switcher.get(function_to_execute, lambda: "Invalid function")
        return func(json_data)

if __name__ == "__main__":
    PythonPlayground.run()
