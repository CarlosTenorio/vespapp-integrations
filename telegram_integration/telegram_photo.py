class TelegramPhoto:

    IMAGE_TYPE = 'image/'

    @classmethod
    def is_photo(cls, update):
        if update.message.photo:
            return True
        elif update.message.document and cls.IMAGE_TYPE in update.message.document.mime_type:
            return True
        else:
            return False

    @classmethod
    def get_file_id(cls, update):
        if update.message.photo:
            photo_len = len(update.message.photo)
            return update.message.photo[photo_len-1].file_id
        elif update.message.document:
            return update.message.document.file_id
        else:
            return None

    @classmethod
    def get_file(cls, bot, file_id):
        return bot.getFile(file_id)
