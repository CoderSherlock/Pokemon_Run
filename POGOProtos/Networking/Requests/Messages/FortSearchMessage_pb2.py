# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/FortSearchMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/FortSearchMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\n?POGOProtos/Networking/Requests/Messages/FortSearchMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"\x86\x01\n\x11\x46ortSearchMessage\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x17\n\x0fplayer_latitude\x18\x02 \x01(\x01\x12\x18\n\x10player_longitude\x18\x03 \x01(\x01\x12\x15\n\rfort_latitude\x18\x04 \x01(\x01\x12\x16\n\x0e\x66ort_longitude\x18\x05 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FORTSEARCHMESSAGE = _descriptor.Descriptor(
  name='FortSearchMessage',
  full_name='POGOProtos.Networking.Requests.Messages.FortSearchMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='POGOProtos.Networking.Requests.Messages.FortSearchMessage.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_latitude', full_name='POGOProtos.Networking.Requests.Messages.FortSearchMessage.player_latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_longitude', full_name='POGOProtos.Networking.Requests.Messages.FortSearchMessage.player_longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_latitude', full_name='POGOProtos.Networking.Requests.Messages.FortSearchMessage.fort_latitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_longitude', full_name='POGOProtos.Networking.Requests.Messages.FortSearchMessage.fort_longitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=243,
)

DESCRIPTOR.message_types_by_name['FortSearchMessage'] = _FORTSEARCHMESSAGE

FortSearchMessage = _reflection.GeneratedProtocolMessageType('FortSearchMessage', (_message.Message,), dict(
  DESCRIPTOR = _FORTSEARCHMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.FortSearchMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.FortSearchMessage)
  ))
_sym_db.RegisterMessage(FortSearchMessage)


# @@protoc_insertion_point(module_scope)
