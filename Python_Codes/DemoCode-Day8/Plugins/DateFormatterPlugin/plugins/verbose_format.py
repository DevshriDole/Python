from plugin_base import DateFormatterPlugin

class VerboseDateFormatter(DateFormatterPlugin):
    def format(self, dt):
        return dt.strftime("%B %d, %Y")  # e.g., April 16, 2025
