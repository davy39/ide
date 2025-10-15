#!/usr/bin/env python3
import json
from pathlib import Path
import subprocess

KERNEL_DIR = Path(".pixi/envs/kernel/share/jupyter/kernels")

kernels = {
    "xpython": "Python",
    "xocaml": "OCaml",
    "xsqlite": "SQL",
    "xc23": "C",
    "xjavascript": "JavaScript",
}

for kernel, display_name in kernels.items():
    kernel_json = KERNEL_DIR / kernel / "kernel.json"
    data = json.loads(kernel_json.read_text())
    data["display_name"] = display_name
    kernel_json.write_text(json.dumps(data, indent=2))