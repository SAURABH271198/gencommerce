import importlib
import pkgutil

__all__ = []

# Automatically load all submodules (v1, v2, etc.)
for _, module_name, _ in pkgutil.iter_modules(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    __all__.append(module_name)
