# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/Master/PokemonSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import PokemonId_pb2 as POGOProtos_dot_Enums_dot_PokemonId__pb2
from POGOProtos.Enums import PokemonRarity_pb2 as POGOProtos_dot_Enums_dot_PokemonRarity__pb2
from POGOProtos.Enums import PokemonType_pb2 as POGOProtos_dot_Enums_dot_PokemonType__pb2
from POGOProtos.Enums import PokemonMove_pb2 as POGOProtos_dot_Enums_dot_PokemonMove__pb2
from POGOProtos.Enums import PokemonFamilyId_pb2 as POGOProtos_dot_Enums_dot_PokemonFamilyId__pb2
from POGOProtos.Settings.Master.Pokemon import StatsAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_StatsAttributes__pb2
from POGOProtos.Settings.Master.Pokemon import CameraAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_CameraAttributes__pb2
from POGOProtos.Settings.Master.Pokemon import EncounterAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_EncounterAttributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Settings/Master/PokemonSettings.proto',
  package='POGOProtos.Settings.Master',
  syntax='proto3',
  serialized_pb=_b('\n0POGOProtos/Settings/Master/PokemonSettings.proto\x12\x1aPOGOProtos.Settings.Master\x1a POGOProtos/Enums/PokemonId.proto\x1a$POGOProtos/Enums/PokemonRarity.proto\x1a\"POGOProtos/Enums/PokemonType.proto\x1a\"POGOProtos/Enums/PokemonMove.proto\x1a&POGOProtos/Enums/PokemonFamilyId.proto\x1a\x38POGOProtos/Settings/Master/Pokemon/StatsAttributes.proto\x1a\x39POGOProtos/Settings/Master/Pokemon/CameraAttributes.proto\x1a<POGOProtos/Settings/Master/Pokemon/EncounterAttributes.proto\"\x94\x07\n\x0fPokemonSettings\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.POGOProtos.Enums.PokemonId\x12\x13\n\x0bmodel_scale\x18\x03 \x01(\x02\x12+\n\x04type\x18\x04 \x01(\x0e\x32\x1d.POGOProtos.Enums.PokemonType\x12-\n\x06type_2\x18\x05 \x01(\x0e\x32\x1d.POGOProtos.Enums.PokemonType\x12\x44\n\x06\x63\x61mera\x18\x06 \x01(\x0b\x32\x34.POGOProtos.Settings.Master.Pokemon.CameraAttributes\x12J\n\tencounter\x18\x07 \x01(\x0b\x32\x37.POGOProtos.Settings.Master.Pokemon.EncounterAttributes\x12\x42\n\x05stats\x18\x08 \x01(\x0b\x32\x33.POGOProtos.Settings.Master.Pokemon.StatsAttributes\x12\x32\n\x0bquick_moves\x18\t \x03(\x0e\x32\x1d.POGOProtos.Enums.PokemonMove\x12\x36\n\x0f\x63inematic_moves\x18\n \x03(\x0e\x32\x1d.POGOProtos.Enums.PokemonMove\x12\x16\n\x0e\x61nimation_time\x18\x0b \x03(\x02\x12\x32\n\revolution_ids\x18\x0c \x03(\x0e\x32\x1b.POGOProtos.Enums.PokemonId\x12\x16\n\x0e\x65volution_pips\x18\r \x01(\x05\x12/\n\x06rarity\x18\x0e \x01(\x0e\x32\x1f.POGOProtos.Enums.PokemonRarity\x12\x18\n\x10pokedex_height_m\x18\x0f \x01(\x02\x12\x19\n\x11pokedex_weight_kg\x18\x10 \x01(\x02\x12\x36\n\x11parent_pokemon_id\x18\x11 \x01(\x0e\x32\x1b.POGOProtos.Enums.PokemonId\x12\x16\n\x0eheight_std_dev\x18\x12 \x01(\x02\x12\x16\n\x0eweight_std_dev\x18\x13 \x01(\x02\x12\x1c\n\x14km_distance_to_hatch\x18\x14 \x01(\x02\x12\x34\n\tfamily_id\x18\x15 \x01(\x0e\x32!.POGOProtos.Enums.PokemonFamilyId\x12\x17\n\x0f\x63\x61ndy_to_evolve\x18\x16 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_PokemonId__pb2.DESCRIPTOR,POGOProtos_dot_Enums_dot_PokemonRarity__pb2.DESCRIPTOR,POGOProtos_dot_Enums_dot_PokemonType__pb2.DESCRIPTOR,POGOProtos_dot_Enums_dot_PokemonMove__pb2.DESCRIPTOR,POGOProtos_dot_Enums_dot_PokemonFamilyId__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_StatsAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_CameraAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_EncounterAttributes__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POKEMONSETTINGS = _descriptor.Descriptor(
  name='PokemonSettings',
  full_name='POGOProtos.Settings.Master.PokemonSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Settings.Master.PokemonSettings.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_scale', full_name='POGOProtos.Settings.Master.PokemonSettings.model_scale', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='POGOProtos.Settings.Master.PokemonSettings.type', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_2', full_name='POGOProtos.Settings.Master.PokemonSettings.type_2', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='camera', full_name='POGOProtos.Settings.Master.PokemonSettings.camera', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter', full_name='POGOProtos.Settings.Master.PokemonSettings.encounter', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='POGOProtos.Settings.Master.PokemonSettings.stats', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quick_moves', full_name='POGOProtos.Settings.Master.PokemonSettings.quick_moves', index=7,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cinematic_moves', full_name='POGOProtos.Settings.Master.PokemonSettings.cinematic_moves', index=8,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='animation_time', full_name='POGOProtos.Settings.Master.PokemonSettings.animation_time', index=9,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_ids', full_name='POGOProtos.Settings.Master.PokemonSettings.evolution_ids', index=10,
      number=12, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_pips', full_name='POGOProtos.Settings.Master.PokemonSettings.evolution_pips', index=11,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rarity', full_name='POGOProtos.Settings.Master.PokemonSettings.rarity', index=12,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_height_m', full_name='POGOProtos.Settings.Master.PokemonSettings.pokedex_height_m', index=13,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_weight_kg', full_name='POGOProtos.Settings.Master.PokemonSettings.pokedex_weight_kg', index=14,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_pokemon_id', full_name='POGOProtos.Settings.Master.PokemonSettings.parent_pokemon_id', index=15,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_std_dev', full_name='POGOProtos.Settings.Master.PokemonSettings.height_std_dev', index=16,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_std_dev', full_name='POGOProtos.Settings.Master.PokemonSettings.weight_std_dev', index=17,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='km_distance_to_hatch', full_name='POGOProtos.Settings.Master.PokemonSettings.km_distance_to_hatch', index=18,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family_id', full_name='POGOProtos.Settings.Master.PokemonSettings.family_id', index=19,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy_to_evolve', full_name='POGOProtos.Settings.Master.PokemonSettings.candy_to_evolve', index=20,
      number=22, type=5, cpp_type=1, label=1,
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
  serialized_start=444,
  serialized_end=1360,
)

_POKEMONSETTINGS.fields_by_name['pokemon_id'].enum_type = POGOProtos_dot_Enums_dot_PokemonId__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['type'].enum_type = POGOProtos_dot_Enums_dot_PokemonType__pb2._POKEMONTYPE
_POKEMONSETTINGS.fields_by_name['type_2'].enum_type = POGOProtos_dot_Enums_dot_PokemonType__pb2._POKEMONTYPE
_POKEMONSETTINGS.fields_by_name['camera'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_CameraAttributes__pb2._CAMERAATTRIBUTES
_POKEMONSETTINGS.fields_by_name['encounter'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_EncounterAttributes__pb2._ENCOUNTERATTRIBUTES
_POKEMONSETTINGS.fields_by_name['stats'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Pokemon_dot_StatsAttributes__pb2._STATSATTRIBUTES
_POKEMONSETTINGS.fields_by_name['quick_moves'].enum_type = POGOProtos_dot_Enums_dot_PokemonMove__pb2._POKEMONMOVE
_POKEMONSETTINGS.fields_by_name['cinematic_moves'].enum_type = POGOProtos_dot_Enums_dot_PokemonMove__pb2._POKEMONMOVE
_POKEMONSETTINGS.fields_by_name['evolution_ids'].enum_type = POGOProtos_dot_Enums_dot_PokemonId__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['rarity'].enum_type = POGOProtos_dot_Enums_dot_PokemonRarity__pb2._POKEMONRARITY
_POKEMONSETTINGS.fields_by_name['parent_pokemon_id'].enum_type = POGOProtos_dot_Enums_dot_PokemonId__pb2._POKEMONID
_POKEMONSETTINGS.fields_by_name['family_id'].enum_type = POGOProtos_dot_Enums_dot_PokemonFamilyId__pb2._POKEMONFAMILYID
DESCRIPTOR.message_types_by_name['PokemonSettings'] = _POKEMONSETTINGS

PokemonSettings = _reflection.GeneratedProtocolMessageType('PokemonSettings', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONSETTINGS,
  __module__ = 'POGOProtos.Settings.Master.PokemonSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.PokemonSettings)
  ))
_sym_db.RegisterMessage(PokemonSettings)


# @@protoc_insertion_point(module_scope)
