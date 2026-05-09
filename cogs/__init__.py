import os
import importlib

current_dir = os.path.dirname(os.path.abspath(__file__))
for file in os.listdir(os.path.join(current_dir, 'commands')):
    if file.endswith('.py') and not file.startswith('__'):
        importlib.import_module(f'commands.{file[:-3]}')