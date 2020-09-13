import importlib
import sys
import logging
from src.utils.config import get_default

logging.basicConfig(filename=get_default('logger', 'filename'), 
                    level=get_default('logger', 'level'), 
                    format=get_default('logger', 'format'))

logging.info('Beginning process {}'.format(sys.argv[1]))
module = importlib.import_module('src.main.' + sys.argv[1])
main = getattr(module, 'main')
main()
