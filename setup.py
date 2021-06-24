import sys
from cx_Freeze import setup, Executable

build_exe = {"packages":["pygame","time","random"],"excludes":["tkinter"],"include_files":["imagens"]}

if sys.platform == "Win32":
	base = "Win32GUI"
else:
	base = None
setup(
	name = "Jogo educacional",
	version="1.0",
	description="jogo",
	options = {"build_exe":build_exe},
	executables = [Executable("main.py",base=base)]
)
