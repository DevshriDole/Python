from plugin_base import GreetingPlugin

class CasualGreeting(GreetingPlugin):
    def greet(self, name: str) -> str:
        return f"Hey {name}! What's up?"
