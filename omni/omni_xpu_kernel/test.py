import sys
from pathlib import Path
import os


 # Detect oneDNN (dnnl) installation
onednn_include = os.environ.get("ONEDNN_INCLUDE", "")
onednn_lib = os.environ.get("ONEDNN_LIB", "")

if not onednn_include or not onednn_lib:
    # Auto-detect from common oneAPI paths
    onednn_candidates = [
        "/opt/intel/oneapi/dnnl/2025.1",
        "/opt/intel/oneapi/dnnl/latest",
        "/opt/intel/oneapi/2025.1",
    ]
    for candidate in onednn_candidates:
        inc = os.path.join(candidate, "include")
        lib = os.path.join(candidate, "lib")
        if os.path.exists(os.path.join(inc, "oneapi", "dnnl", "dnnl.hpp")):
            if not onednn_include:
                onednn_include = inc
            if not onednn_lib:
                onednn_lib = lib
            break

has_onednn = bool(onednn_include and os.path.isdir(onednn_include))
if has_onednn:
    print(f"oneDNN include: {onednn_include}")
    print(f"oneDNN lib: {onednn_lib}")
else:
    print("WARNING: oneDNN not found. onednn_int4_gemm will not be available.")


import os
for k, v in sorted(os.environ.items()):
    print(f"{k}={v}")