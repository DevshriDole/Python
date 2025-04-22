from plugin_base import DateFormatterPlugin

class USDateFormatter(DateFormatterPlugin):
    def format(self, dt):
        return dt.strftime("%m/%d/%Y")
