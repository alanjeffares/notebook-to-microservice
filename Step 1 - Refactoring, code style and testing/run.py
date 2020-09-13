import importlib
import sys


module = importlib.import_module('src.main.' + sys.argv[1])
main = getattr(module, 'main')
main()
