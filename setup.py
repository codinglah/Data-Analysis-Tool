import sys
from cx_Freeze import setup, Executable
base = None
if sys.platform == 'Win32':
    base = 'Win32GUI'
setup(
    name = 'Data Analysis Tool',
    version = '1.0.0-a1',
    description = 'A tool that helps you to analyse data.',
    author = 'Wang Zhisheng',
    executables = [Executable('main.py', base = base)])
