import importlib
import pkgutil
from plugin_base import GreetingPlugin

def load_plugins():
    plugins = []
    package = 'plugins'

    for _, module_name, _ in pkgutil.iter_modules([package]):
        module = importlib.import_module(f"{package}.{module_name}")
        print(module)
        for item_name in dir(module):
            item = getattr(module, item_name)
            if isinstance(item, type) and issubclass(item, GreetingPlugin) and item != GreetingPlugin:
                plugins.append(item())
    return plugins

def main():
    name = input("Enter your name: ")
    plugins = load_plugins()
    print(plugins)
    for plugin in plugins:
        print(plugin.greet(name))

if __name__ == "__main__":
    main()
