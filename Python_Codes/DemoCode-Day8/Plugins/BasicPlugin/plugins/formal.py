from plugin_base import GreetingPlugin

class FormalGreeting(GreetingPlugin):
    def greet(self, name: str) -> str:
        return f"Good day, {name}. It's a pleasure to meet you."
