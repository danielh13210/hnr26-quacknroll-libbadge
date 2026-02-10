import builtins

from lib.libbadge.main import Hardware
builtins.libbadge=Hardware()

del builtins, Hardware
