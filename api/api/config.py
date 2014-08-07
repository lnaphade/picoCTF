"""
CTF API Configuration File

Note this is just a python script. It does config things.
"""

import api
import datetime

competition_name = "picoCTF"
competition_url = "127.0.0.1:8080"

""" FLASK """

api.app.session_cookie_domain = "127.0.0.1"
api.app.session_cookie_path = "/"
api.app.session_cookie_name = "flask"

# KEEP THIS SECRET
api.app.secret_key = "5XVbne3AjPH35eEH8yQI"

""" SECURITY """

api.common.allowed_protocols = ["https", "http"]
api.common.allowed_ports = [8080]

""" MONGO """

api.common.mongo_db_name = "pico"
api.common.mongo_addr = "127.0.0.1"
api.common.mongo_port = 27017

""" CTF SETTINGS """

# Max users on any given team
api.team.max_team_users = 5

# Teams to display on scoreboard graph
api.stats.top_teams = 5

# start and end times!
class EST(datetime.tzinfo):
    def __init__(self, utc_offset):
        self.utc_offset = utc_offset

    def utcoffset(self, dt):
      return datetime.timedelta(hours=-self.utc_offset)

    def dst(self, dt):
        return datetime.timedelta(0)

start_time = datetime.datetime(2014, 8, 4, 12, 13, 0, tzinfo=EST(4))
end_time = datetime.datetime(2014, 11, 7, 23, 59, 59, tzinfo=EST(5))

# Root directory of all problem graders
api.problem.grader_base_path = "./graders"

""" EMAIL (SMTP) """

api.utilities.enable_email = False
api.utilities.smtp_url = ""
api.utilities.email_username = ""
api.utilities.email_password = ""
api.utilities.from_addr = ""
api.utilities.from_name = ""

""" AUTOGENERATED PROBLEMS """

api.autogen.seed = "0413688f8ef14e96b0afe25e2f662fef"

""" LOGGING """

# Will be emailed any severe internal exceptions!
# Requires email block to be setup.
api.logger.admin_emails = ["ben@example.com", "joe@example.com"]
