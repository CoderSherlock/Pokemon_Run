# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/Capture/CaptureProbability.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Inventory.Item import ItemId_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Data/Capture/CaptureProbability.proto',
  package='POGOProtos.Data.Capture',
  syntax='proto3',
  serialized_pb=_b('\n0POGOProtos/Data/Capture/CaptureProbability.proto\x12\x17POGOProtos.Data.Capture\x1a&POGOProtos/Inventory/Item/ItemId.proto\"\x95\x01\n\x12\x43\x61ptureProbability\x12<\n\rpokeball_type\x18\x01 \x03(\x0e\x32!.POGOProtos.Inventory.Item.ItemIdB\x02\x10\x01\x12\x1f\n\x13\x63\x61pture_probability\x18\x02 \x03(\x02\x42\x02\x10\x01\x12 \n\x18reticle_difficulty_scale\x18\x0c \x01(\x01\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CAPTUREPROBABILITY = _descriptor.Descriptor(
  name='CaptureProbability',
  full_name='POGOProtos.Data.Capture.CaptureProbability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokeball_type', full_name='POGOProtos.Data.Capture.CaptureProbability.pokeball_type', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='capture_probability', full_name='POGOProtos.Data.Capture.CaptureProbability.capture_probability', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='reticle_difficulty_scale', full_name='POGOProtos.Data.Capture.CaptureProbability.reticle_difficulty_scale', index=2,
      number=12, type=1, cpp_type=5, label=1,
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
  serialized_start=118,
  serialized_end=267,
)

_CAPTUREPROBABILITY.fields_by_name['pokeball_type'].enum_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2._ITEMID
DESCRIPTOR.message_types_by_name['CaptureProbability'] = _CAPTUREPROBABILITY

CaptureProbability = _reflection.GeneratedProtocolMessageType('CaptureProbability', (_message.Message,), dict(
  DESCRIPTOR = _CAPTUREPROBABILITY,
  __module__ = 'POGOProtos.Data.Capture.CaptureProbability_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Capture.CaptureProbability)
  ))
_sym_db.RegisterMessage(CaptureProbability)


_CAPTUREPROBABILITY.fields_by_name['pokeball_type'].has_options = True
_CAPTUREPROBABILITY.fields_by_name['pokeball_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_CAPTUREPROBABILITY.fields_by_name['capture_probability'].has_options = True
_CAPTUREPROBABILITY.fields_by_name['capture_probability']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
