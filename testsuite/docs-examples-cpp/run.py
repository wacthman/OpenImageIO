#!/usr/bin/env python

# Copyright Contributors to the OpenImageIO project.
# SPDX-License-Identifier: Apache-2.0
# https://github.com/AcademySoftwareFoundation/OpenImageIO


if platform.system() == 'Windows' :
    prefix = ".\\build\\Release\\"
else :
    prefix = "./build/"

# Prep:
command += run_app("cmake -E copy ../common/grid-small.exr grid.exr")

# Build
command += run_app("cmake -S " + test_source_dir + " -B build -DCMAKE_BUILD_TYPE=Release >> build.txt 2>&1", silent=True)
command += run_app("cmake --build build --config Release >> build.txt 2>&1", silent=True)

# Run the examples for each chapter
for chapter in [ "imageioapi", "imageoutput", "imageinput", "writingplugins",
                 "imagecache", "texturesys", "imagebuf", "imagebufalgo" ] :
    command += run_app(prefix + "docs-examples-" + chapter)

# hashes merely check that the images don't change, but saves us the space
# of checking in a full copy of the image if it's not needed.
hashes = [
    # Outputs from the ImageBufAlgo chapter:
    "cshift.exr",
]
for file in hashes :
    command += info_command(file, verbose=False)

# outputs should contain all the images that need to be checked directly
# and need the images checked into the ref directory.
outputs = [
    # Outputs from the ImageOutput chapter:
    "simple.tif", "scanlines.tif",
    # Outputs from the ImageInput chapter:

    # ... etc ... other chapters ...

    # Last, we have the out.txt that captures console output of the test
    # programs.
    "out.txt"
    ]
