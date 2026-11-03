"""aftershock: finds the exact lines a library, API or config change breaks in other code."""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("aftershock")
except PackageNotFoundError:          # a source tree that was never installed
    __version__ = "0+unknown"
