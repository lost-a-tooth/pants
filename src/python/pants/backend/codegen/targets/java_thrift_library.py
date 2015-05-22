# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import collections

from pants.backend.jvm.targets.jvm_target import JvmTarget
from pants.base.exceptions import TargetDefinitionException
from pants.base.payload import Payload
from pants.base.payload_field import PrimitiveField


class JavaThriftLibrary(JvmTarget):
  """Generates a stub Java or Scala library from thrift IDL files."""

  # TODO(John Sirois): Tasks should register the values they support in a plugin-registration goal.
  # In general a plugin will contribute a target and a task, but in this case we have a shared
  # target that can be used by at least 2 tasks - ThriftGen and ScroogeGen.  This is likely not
  # uncommon (gcc & clang) so the arrangement needs to be cleaned up and supported well.
  ConfigInfo = collections.namedtuple('ConfigInfo', 'default valid_values')

  _COMPILERS = ConfigInfo(default='thrift', valid_values=frozenset(['thrift', 'scrooge']))
  _LANGUAGES = ConfigInfo(default='java', valid_values=frozenset(['java', 'scala']))
  _RPC_STYLES = ConfigInfo(default='sync', valid_values=frozenset(['sync', 'finagle', 'ostrich']))

  def __init__(self,
               compiler=None,
               language=None,
               rpc_style=None,
               namespace_map=None,
               thrift_linter_strict=None,
               **kwargs):
    """
    :param compiler: The compiler used to compile the thrift files. The default is defined in
      the global options under ``--thrift-default-compiler``.
    :param language: The language used to generate the output files. The default is defined in
      the global options under ``--thrift-default-language``.
    :param rpc_style: An optional rpc style to generate service stubs with. The default is defined
      in the global options under ``--thrift-default-rpc-style``.
    :param namespace_map: An optional dictionary of namespaces to remap {old: new}
    :param thrift_linter_strict: If True, fail if thrift linter produces any warnings.
    """
    def check_value_for_arg(arg, value, config):
      if not value:
        value = config.default
      if value not in config.valid_values:
        raise TargetDefinitionException(self, "{} may only be set to {} ('{}' not valid)"
                                        .format(arg, ', or '.join(map(repr, config.valid_values)),
                                        config.valid_values))
      return value

    self._compiler = check_value_for_arg('compiler', compiler, self._COMPILERS)
    self._language = check_value_for_arg('language', language, self._LANGUAGES)
    self._rpc_style = check_value_for_arg('rpc_style', rpc_style, self._RPC_STYLES)

    payload = Payload()
    payload.add_fields({
      'compiler': PrimitiveField(self._compiler),
      'language': PrimitiveField(self._language),
      'rpc_style': PrimitiveField(self._rpc_style),
    })

    super(JavaThriftLibrary, self).__init__(payload=payload, **kwargs)

    # TODO(Eric Ayers) As of 2/5/2015 this call is DEPRECATED and should be removed soon
    self.add_labels('codegen')

    self.namespace_map = namespace_map
    self.thrift_linter_strict = thrift_linter_strict

  @property
  def compiler(self):
    return self._compiler

  @property
  def language(self):
    return self._language

  @property
  def rpc_style(self):
    return self._rpc_style

  # TODO(Eric Ayers) As of 2/5/2015 this call is DEPRECATED and should be removed soon
  @property
  def is_thrift(self):
    return True
