#!/bin/bash

set -eux
sed -i '/xc11/d' CMakeLists.txt
sed -i '/xc17/d' CMakeLists.txt
sed -i '/xcpp17/d' CMakeLists.txt
sed -i '/xcpp20/d' CMakeLists.txt
sed -i '/xcpp23/d' CMakeLists.txt
sed -i 's@"display_name": "C23"@"display_name": "C"@' share/jupyter/kernels/xc23/wasm_kernel.json.in
mkdir -p build
cd build

# Set up the environment variables for cross-compiling to WASM
export SYSROOT_PATH=$EMSCRIPTEN_FORGE_EMSDK_DIR/upstream/emscripten/cache/sysroot

# Configure step with Emscripten's emcmake
emcmake cmake \
    -DCMAKE_BUILD_TYPE=Release                        \
    -DCMAKE_INSTALL_PREFIX=$PREFIX                    \
    -DXEUS_CPP_EMSCRIPTEN_WASM_BUILD=ON               \
    -DCMAKE_FIND_ROOT_PATH=$PREFIX                    \
    -DSYSROOT_PATH=$SYSROOT_PATH                      \
    -DXEUS_CPP_BUILD_TESTS=OFF                        \
    ..

# Build & Install step
emmake make -j8 install