# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
  name='planners',
  sources=['planners.py'],
  dependencies=[
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/base:file_system_project_tree',
    'src/python/pants/engine/exp:fs',
    'src/python/pants/engine/exp:graph',
    'src/python/pants/engine/exp:mapper',
    'src/python/pants/engine/exp:nodes',
    'src/python/pants/engine/exp:parsers',
    'src/python/pants/engine/exp:scheduler',
    'src/python/pants/engine/exp:selectors',
    'src/python/pants/engine/exp:sources',
    'src/python/pants/engine/exp:struct',
  ]
)

python_library(
  name='visualizer',
  sources=['visualizer.py'],
  dependencies=[
    ':planners',
    'src/python/pants/base:cmd_line_spec_parser',
    'src/python/pants/binaries:binary_util',
    'src/python/pants/build_graph',
    'src/python/pants/engine/exp:engine',
    'src/python/pants/engine/exp:scheduler',
    'src/python/pants/util:contextutil',
  ]
)

python_binary(
  name='viz',
  entry_point='pants.engine.exp.examples.visualizer:main_addresses',
  dependencies=[
    ':visualizer'
  ]
)

python_binary(
  name='viz-fs',
  entry_point='pants.engine.exp.examples.visualizer:main_filespecs',
  dependencies=[
    ':visualizer'
  ]
)
