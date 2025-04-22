from plugin_base import DateFormatterPlugin

class EUDateFormatter(DateFormatterPlugin):
    def format(self, dt):
        return dt.strftime("%d/%m/%Y")
