import sys
import os

sys.path.append(os.path.abspath(".."))

project = 'hw12'
copyright = '2026, Andrii Didukh'
author = 'Andrii Didukh'

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
