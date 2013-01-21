#  from pysnip.snip import Snip, registered_snips
from pysnip.snip import Snip, registered_snips
from pysnip.management import commands
from straight.plugin import load
load("pysnip.collection", subclasses=Snip)



__version__ = '0.1'
