"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['pokedb_gui.py']
DATA_FILES = ['pokedb.py']
OPTIONS = {'argv_emulation': True
			'iconfiles':'flygon.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
