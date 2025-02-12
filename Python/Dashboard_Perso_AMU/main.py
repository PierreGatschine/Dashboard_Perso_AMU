import ton_script
import os
import sys

# Ajoute le dossier contenant main.py au début de sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)


if __name__ == "__main__":
    ton_script.main()
