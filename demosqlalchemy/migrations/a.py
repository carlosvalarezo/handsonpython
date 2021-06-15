import os
import sys
# sys.path.append(os.getcwd())
path = os.path.join(os.path.dirname(".."), os.pardir)
sys.path.append(path)
#
from demosqlalchemy.demo import alembic as al
al.Base


print(al.Base)
