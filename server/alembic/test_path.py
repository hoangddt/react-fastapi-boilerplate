import os
import importlib
from pathlib import Path


two_parents = Path(__file__).parent.parent
print(two_parents)
src_path = two_parents / "src" / "minimal_template" / "api"
print(src_path)

for path in src_path.rglob("*.py"):
    
    if path.name != "__init__.py":
        
        if not path.name.endswith("models.py"):
            continue
        print("Scanning: ", path)
        print(path.relative_to(Path(__file__).parent.parent))
        
        full_path_with_dot = str(path.relative_to(Path(__file__).parent.parent)).replace(
            os.sep, "."
        )
        # cut trailing .py

        module_path = full_path_with_dot[:-3]
        module_path = module_path[4:]
        print(module_path)

        # try:
        #     importlib.import_module(module_path)
        # except Exception as e:
        #     print(f"Failed to import {module_path}: {e}")