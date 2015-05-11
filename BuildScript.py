import os, shutil, sys

os.system('C:\Python27\Scripts\pyi-makespec -F -c "FretMemo.py"')
os.system('C:\Python27\Scripts\pyi-build "FretMemo.spec"')

os.mkdir("FretMemo")
shutil.copytree("Ressources", "FretMemo/Ressources")
shutil.copy("dist/FretMemo.exe", "FretMemo")

#--icon=Ressources/FretMemo.ico
#os.remove("FretMemo.spec")
#shutil.rmtree("build")
#shutil.rmtree("dist")