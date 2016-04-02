class Tweet:

	def __init__(self, api):
		self.api = api

	def write(self, message):
		self.api.update_status(message)

	def reply(self, nick_name, message, in_reply_to_status_id):
		self.api.update_status('@' + nick_name + ' ' + message, in_reply_to_status_id)