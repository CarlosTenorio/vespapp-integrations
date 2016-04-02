import threading


class TelegramKeys:

    def __init__(self):
        self.keys = {}
        self.lock = threading.Lock()

    def add_photo(self, chat_id, file_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                self.keys[chat_id]['photos'] += [file_id]
                # self.keys[chat_id].update({'photos': [file_id]})
                return True
            else:
                self.keys[chat_id] = {'photos': [file_id]}
                return False
        finally:
            self.lock.release()

    def add_location(self, chat_id, latitude, longitude):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                self.keys[chat_id].update({'location': [latitude, longitude]})
                return True
            else:
                self.keys[chat_id] = {'location': [latitude, longitude]}
                return False
        finally:
            self.lock.release()

    def add_type(self, chat_id, type):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                self.keys[chat_id].update({'type': type})
                return True
            else:
                self.keys[chat_id] = {'type': type}
            return False
        finally:
            self.lock.release()

    def get_key_by_id(self, chat_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                return self.keys[chat_id]
            return None
        finally:
            self.lock.release()

    def remove_key(self, chat_id):
        self.lock.acquire()
        try:
            if chat_id in self.keys:
                del self.keys[chat_id]
                return True
            return None
        finally:
            self.lock.release()
