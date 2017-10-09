from cx_Freeze import setup, Executable

setup(
    name = 'Dirtybomb Simulator Beta',
    version = '0.3',
    description = 'Dirty Bomb Simulator test',
    author = 'pEppEr',
    executables = [Executable('02-7class_drill.py')])
