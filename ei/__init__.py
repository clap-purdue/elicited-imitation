import os

try:
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    with open(version_file, 'r', encoding='utf-8') as version_f:
        __version__ = version_f.read().strip()
except Exception:  
    print("Failed to find version")