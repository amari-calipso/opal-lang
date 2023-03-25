from distutils.dir_util   import copy_tree
from shutil               import rmtree
from pathlib              import Path
from os                   import chdir, path, getcwd, remove
from ianthe               import Ianthe

spath = str(Path(__file__).parent.absolute())
chdir(spath)

with open("opalrun.py", "w") as script:
    script.write("from subprocess import run\nfrom sys import argv\n")
    chdir("..")
    p = path.join(getcwd(), 'opalc.py').replace("\\", "\\\\")
    script.write(f"run(['python', '{p}'] + argv[1:])")

chdir(spath)

ianthe = Ianthe()
ianthe.config = {
    "source"     : "opalrun.py",
    "destination": "run",
    "onefile"    : True,
    "icon"       : "icon.ico"
}

ianthe.execute()

remove("opalrun.py")

chdir("..")
copy_tree(path.join(spath, "run"), getcwd())

chdir(spath)
rmtree("run")
