# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authmethod.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='authmethod.proto',
  package='api',
  syntax='proto3',
  serialized_options=_b('\n\022com.northghost.apiB\017ProtoAuthmethod'),
  serialized_pb=_b('\n\x10\x61uthmethod.proto\x12\x03\x61pi*!\n\nAuthMethod\x12\x08\n\x04USER\x10\x00\x12\t\n\x05TOKEN\x10\x01\x42%\n\x12\x63om.northghost.apiB\x0fProtoAuthmethodb\x06proto3')
)

_AUTHMETHOD = _descriptor.EnumDescriptor(
  name='AuthMethod',
  full_name='api.AuthMethod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOKEN', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=25,
  serialized_end=58,
)
_sym_db.RegisterEnumDescriptor(_AUTHMETHOD)

AuthMethod = enum_type_wrapper.EnumTypeWrapper(_AUTHMETHOD)
USER = 0
TOKEN = 1


DESCRIPTOR.enum_types_by_name['AuthMethod'] = _AUTHMETHOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
