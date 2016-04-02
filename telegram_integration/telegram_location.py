class TelegramLocation:
    @classmethod
    def is_location(cls, update):
        if update.message.location:
            return True
        else:
            return False

    @classmethod
    def get_location(cls, update):
        if update.message.location:
            return update.message.location.latitude, update.message.location.longitude
        else:
            return None
