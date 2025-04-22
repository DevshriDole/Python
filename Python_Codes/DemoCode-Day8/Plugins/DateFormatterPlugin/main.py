import importlib
import pkgutil
from datetime import date
from plugin_base import DateFormatterPlugin

def load_plugins():
    plugins = []
    package = 'plugins'
    for _, module_name, _ in pkgutil.iter_modules([package]):
        module = importlib.import_module(f"{package}.{module_name}")
        for item_name in dir(module):
            item = getattr(module, item_name)
            if isinstance(item, type) and issubclass(item, DateFormatterPlugin) and item is not DateFormatterPlugin:
                plugins.append(item())
    print (plugins)
    return plugins

def main():
    today = date.today()
    print(f"Today's date is: {today}\nFormatted versions:")

    plugins = load_plugins()

    for plugin in plugins:
        print (plugin.__class__)
        print(f"- {plugin.__class__.__name__}: {plugin.format(today)}")

if __name__ == "__main__":
    main()