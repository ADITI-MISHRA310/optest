



class PexpectLogger:
    def __init__(self, logger):
        self.logger = logger

    def write(self, data):
        if isinstance(data, bytes):
            data = data.decode(errors="ignore")
        data = data.rstrip()
        if data:
            self.logger.debug(data)

    def flush(self):
        pass

