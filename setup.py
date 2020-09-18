from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "single.py"}],
    zipfile = None,
)
cx_Freeze.setup(
	name = "Retro Snake"
	options ={"build_exe": {"packages":["pygame"] "include_files": ["apple.png", "snakeHead.png", "__color__.py", "icon.png", "Mincraftory.tff", "snakeTail.png"]}},

	desciption = "Retro Snake Game",
	executables = executables
	)