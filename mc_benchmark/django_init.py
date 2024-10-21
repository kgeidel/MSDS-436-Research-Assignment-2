import os, sys
from django import setup

# derive location to your django project setting.py
proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
proj_path = f'{proj_path}/mc_benchmark'

# load your settings.py
os.chdir(proj_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mc_benchmark.settings")

# Append proj_path to PATH
sys.path.append(proj_path)

setup()