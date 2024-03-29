# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agent.proto',
  package='api',
  syntax='proto3',
  serialized_options=_b('\n\022com.northghost.apiB\nProtoAgent'),
  serialized_pb=_b('\n\x0b\x61gent.proto\x12\x03\x61pi\"Y\n\nAgentState\x12&\n\x08services\x18\x01 \x03(\x0b\x32\x14.api.VpnServiceState\x12#\n\x08sessions\x18\x02 \x03(\x0b\x32\x11.api.SessionState\",\n\x0fVpnServiceState\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"+\n\x0cSessionState\x12\x0b\n\x03uid\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\tB \n\x12\x63om.northghost.apiB\nProtoAgentb\x06proto3')
)




_AGENTSTATE = _descriptor.Descriptor(
  name='AgentState',
  full_name='api.AgentState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='api.AgentState.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessions', full_name='api.AgentState.sessions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=109,
)


_VPNSERVICESTATE = _descriptor.Descriptor(
  name='VpnServiceState',
  full_name='api.VpnServiceState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='api.VpnServiceState.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.VpnServiceState.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=155,
)


_SESSIONSTATE = _descriptor.Descriptor(
  name='SessionState',
  full_name='api.SessionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='api.SessionState.uid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='api.SessionState.parent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=200,
)

_AGENTSTATE.fields_by_name['services'].message_type = _VPNSERVICESTATE
_AGENTSTATE.fields_by_name['sessions'].message_type = _SESSIONSTATE
DESCRIPTOR.message_types_by_name['AgentState'] = _AGENTSTATE
DESCRIPTOR.message_types_by_name['VpnServiceState'] = _VPNSERVICESTATE
DESCRIPTOR.message_types_by_name['SessionState'] = _SESSIONSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgentState = _reflection.GeneratedProtocolMessageType('AgentState', (_message.Message,), dict(
  DESCRIPTOR = _AGENTSTATE,
  __module__ = 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.AgentState)
  ))
_sym_db.RegisterMessage(AgentState)

VpnServiceState = _reflection.GeneratedProtocolMessageType('VpnServiceState', (_message.Message,), dict(
  DESCRIPTOR = _VPNSERVICESTATE,
  __module__ = 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.VpnServiceState)
  ))
_sym_db.RegisterMessage(VpnServiceState)

SessionState = _reflection.GeneratedProtocolMessageType('SessionState', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONSTATE,
  __module__ = 'agent_pb2'
  # @@protoc_insertion_point(class_scope:api.SessionState)
  ))
_sym_db.RegisterMessage(SessionState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
