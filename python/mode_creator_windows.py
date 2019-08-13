import os
from easygui import *

title = "Mode Creator"

msg = "Please enter mode name"
field_names = ["Mode Name"]
mode_name = multenterbox(msg,title, field_names)[0].replace(" ", "_")

msg = "Please enter paths"
field_names = ["Path", "Path", "Path", "Path", "Path"]
paths = multenterbox(msg,title, field_names)

paths = list(filter(None, paths))
for i in range(len(paths)):
    paths[i] =  'start "" "' + paths[i] + '"\n'

mode_filepath = os.path.join(os.getcwd(),mode_name) + ".bat"
if(os.path.isfile(mode_filepath)):
    f = open(mode_filepath,"a")
else:
    f = open(mode_filepath, "x")

f.writelines(paths)
