# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

base = None
targetName = 'satiedbf'

if sys.platform == 'win32':
    base = 'Win32GUI'
    targetName = 'satiedbf.exe'

options = {
    'build_exe': {
        'includes': ['atexit', 'pdb'],
        'packages': ['os'],
        # Sometimes a little fine-tuning is needed
        # exclude all backends except wx
        'excludes': ['gtk', 'PyQt4', 'Tkinter'],
        'optimize': 2,
        'path': sys.path + ['Images'],
        'include_files': ['Images']
    }

}

executables = [
    Executable('Main.py', base=base,
               targetName=targetName)
]

setup(name='SatieDbf',
      version='1.0.0',
      description='Satie DBF Convert is a portable DBF database table viewer.',
      options=options,
      executables=executables
      )
