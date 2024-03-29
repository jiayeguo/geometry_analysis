"""
geometry_analysis
This is a python package for MolSSI Summer School 2019.
"""

# Add imports here
from .molecule import *
from .measure import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
