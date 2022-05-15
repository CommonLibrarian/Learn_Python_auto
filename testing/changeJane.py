#!/usr/bin/env python3

#changing the name of the files containing only "jane" to "jdoe"

import sys
import os
from pathlib import Path
with open (sys.argv[1], "r") as myfile:
   for line in myfile:
    data= line.replace("\n", "")
    base=os.path.basename(data)
    baseNew = base.replace("jane","jdoe")
    os.chdir('/my/directory/to/data/')
    os.rename(base, baseNew)
myfile.close()
