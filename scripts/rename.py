#!/usr/bin/env python3
import json
from pathlib import Path
import shutil  # Imported for directory removal functions

KERNEL_DIR = Path(".pixi/envs/kernel/share/jupyter/kernels")

# List of kernel directories to be deleted
kernels_to_delete = ["xcpp17", "xcpp20", "xcpp23", "xc11", "xc17"]

print("--- Deleting Unwanted Kernel Directories ---")
for kernel_name in kernels_to_delete:
    kernel_path = KERNEL_DIR / kernel_name
    if kernel_path.exists() and kernel_path.is_dir():
        print(f"Deleting directory: {kernel_path}")
        shutil.rmtree(kernel_path)
    else:
        print(f"Directory not found, skipping: {kernel_path}")

print("--- Deletion Complete ---\n")

# Original script logic to update remaining kernels
print("--- Updating Display Names for Remaining Kernels ---")
kernels_to_update = {
    "xpython": "Python",
    "xocaml": "OCaml",
    "xsqlite": "SQL",
    "xc23": "C",
    "xjavascript": "JavaScript",
}

for kernel, display_name in kernels_to_update.items():
    kernel_json = KERNEL_DIR / kernel / "kernel.json"
    
    # Check if the kernel.json file exists before trying to modify it
    if kernel_json.exists():
        try:
            data = json.loads(kernel_json.read_text())
            data["display_name"] = display_name
            kernel_json.write_text(json.dumps(data, indent=2))
            print(f"Updated display name for '{kernel}' to '{display_name}'")
        except Exception as e:
            print(f"Could not update {kernel}: {e}")
    else:
        print(f"Kernel '{kernel}' not found, skipping update.")