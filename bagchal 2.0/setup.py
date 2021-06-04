import sys
from cx_Freeze import setup, Executable

exe_options = {"packages": ["os"], "excludes": ["pygame"],"include_files":["blank.png","board.png","goat.png","goat_out.png","goat_selected.png","tiger.png", "tiger_selected.png","tiger_trapped.png","move.wav","jump.wav"]}

if sys.platform == "win32":
 base = "Win32GUI"

setup(
    name = "Bibash",
    version = "0.1",
    options = {"build_exe": exe_options},                    
    executables = [Executable("bagchal.py"),Executable("boardtoanimalconverter.py"),Executable("goatmovement.py"),Executable("movetypes.py"),Executable("position.py"),Executable("tigerjump.py"),Executable("tigermovement.py")]
)



