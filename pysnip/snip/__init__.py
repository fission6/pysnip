"""
Need to dynamically load all python modules
in the snips/ folder.
"""


from snip import registered_snips, Snip

from straight.plugin import load
load("collection", subclasses=Snip)

__all__ = ['registered_snips']

__version__ = '0.1'
