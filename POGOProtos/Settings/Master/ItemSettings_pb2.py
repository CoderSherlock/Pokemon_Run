# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Settings/Master/ItemSettings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import ItemCategory_pb2 as POGOProtos_dot_Enums_dot_ItemCategory__pb2
from POGOProtos.Inventory.Item import ItemId_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2
from POGOProtos.Inventory.Item import ItemType_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemType__pb2
from POGOProtos.Settings.Master.Item import FoodAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_FoodAttributes__pb2
from POGOProtos.Settings.Master.Item import PotionAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_PotionAttributes__pb2
from POGOProtos.Settings.Master.Item import ReviveAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_ReviveAttributes__pb2
from POGOProtos.Settings.Master.Item import BattleAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_BattleAttributes__pb2
from POGOProtos.Settings.Master.Item import IncenseAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_IncenseAttributes__pb2
from POGOProtos.Settings.Master.Item import PokeballAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_PokeballAttributes__pb2
from POGOProtos.Settings.Master.Item import FortModifierAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_FortModifierAttributes__pb2
from POGOProtos.Settings.Master.Item import EggIncubatorAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_EggIncubatorAttributes__pb2
from POGOProtos.Settings.Master.Item import ExperienceBoostAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_ExperienceBoostAttributes__pb2
from POGOProtos.Settings.Master.Item import InventoryUpgradeAttributes_pb2 as POGOProtos_dot_Settings_dot_Master_dot_Item_dot_InventoryUpgradeAttributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Settings/Master/ItemSettings.proto',
  package='POGOProtos.Settings.Master',
  syntax='proto3',
  serialized_pb=_b('\n-POGOProtos/Settings/Master/ItemSettings.proto\x12\x1aPOGOProtos.Settings.Master\x1a#POGOProtos/Enums/ItemCategory.proto\x1a&POGOProtos/Inventory/Item/ItemId.proto\x1a(POGOProtos/Inventory/Item/ItemType.proto\x1a\x34POGOProtos/Settings/Master/Item/FoodAttributes.proto\x1a\x36POGOProtos/Settings/Master/Item/PotionAttributes.proto\x1a\x36POGOProtos/Settings/Master/Item/ReviveAttributes.proto\x1a\x36POGOProtos/Settings/Master/Item/BattleAttributes.proto\x1a\x37POGOProtos/Settings/Master/Item/IncenseAttributes.proto\x1a\x38POGOProtos/Settings/Master/Item/PokeballAttributes.proto\x1a<POGOProtos/Settings/Master/Item/FortModifierAttributes.proto\x1a<POGOProtos/Settings/Master/Item/EggIncubatorAttributes.proto\x1a?POGOProtos/Settings/Master/Item/ExperienceBoostAttributes.proto\x1a@POGOProtos/Settings/Master/Item/InventoryUpgradeAttributes.proto\"\xb5\x07\n\x0cItemSettings\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12\x36\n\titem_type\x18\x02 \x01(\x0e\x32#.POGOProtos.Inventory.Item.ItemType\x12\x30\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x1e.POGOProtos.Enums.ItemCategory\x12\x11\n\tdrop_freq\x18\x04 \x01(\x02\x12\x1a\n\x12\x64rop_trainer_level\x18\x05 \x01(\x05\x12\x45\n\x08pokeball\x18\x06 \x01(\x0b\x32\x33.POGOProtos.Settings.Master.Item.PokeballAttributes\x12\x41\n\x06potion\x18\x07 \x01(\x0b\x32\x31.POGOProtos.Settings.Master.Item.PotionAttributes\x12\x41\n\x06revive\x18\x08 \x01(\x0b\x32\x31.POGOProtos.Settings.Master.Item.ReviveAttributes\x12\x41\n\x06\x62\x61ttle\x18\t \x01(\x0b\x32\x31.POGOProtos.Settings.Master.Item.BattleAttributes\x12=\n\x04\x66ood\x18\n \x01(\x0b\x32/.POGOProtos.Settings.Master.Item.FoodAttributes\x12V\n\x11inventory_upgrade\x18\x0b \x01(\x0b\x32;.POGOProtos.Settings.Master.Item.InventoryUpgradeAttributes\x12L\n\x08xp_boost\x18\x0c \x01(\x0b\x32:.POGOProtos.Settings.Master.Item.ExperienceBoostAttributes\x12\x43\n\x07incense\x18\r \x01(\x0b\x32\x32.POGOProtos.Settings.Master.Item.IncenseAttributes\x12N\n\regg_incubator\x18\x0e \x01(\x0b\x32\x37.POGOProtos.Settings.Master.Item.EggIncubatorAttributes\x12N\n\rfort_modifier\x18\x0f \x01(\x0b\x32\x37.POGOProtos.Settings.Master.Item.FortModifierAttributesb\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_ItemCategory__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_Item_dot_ItemType__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_FoodAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_PotionAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_ReviveAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_BattleAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_IncenseAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_PokeballAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_FortModifierAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_EggIncubatorAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_ExperienceBoostAttributes__pb2.DESCRIPTOR,POGOProtos_dot_Settings_dot_Master_dot_Item_dot_InventoryUpgradeAttributes__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ITEMSETTINGS = _descriptor.Descriptor(
  name='ItemSettings',
  full_name='POGOProtos.Settings.Master.ItemSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Settings.Master.ItemSettings.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_type', full_name='POGOProtos.Settings.Master.ItemSettings.item_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='POGOProtos.Settings.Master.ItemSettings.category', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop_freq', full_name='POGOProtos.Settings.Master.ItemSettings.drop_freq', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop_trainer_level', full_name='POGOProtos.Settings.Master.ItemSettings.drop_trainer_level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokeball', full_name='POGOProtos.Settings.Master.ItemSettings.pokeball', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='potion', full_name='POGOProtos.Settings.Master.ItemSettings.potion', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='revive', full_name='POGOProtos.Settings.Master.ItemSettings.revive', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle', full_name='POGOProtos.Settings.Master.ItemSettings.battle', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='food', full_name='POGOProtos.Settings.Master.ItemSettings.food', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_upgrade', full_name='POGOProtos.Settings.Master.ItemSettings.inventory_upgrade', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xp_boost', full_name='POGOProtos.Settings.Master.ItemSettings.xp_boost', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incense', full_name='POGOProtos.Settings.Master.ItemSettings.incense', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubator', full_name='POGOProtos.Settings.Master.ItemSettings.egg_incubator', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_modifier', full_name='POGOProtos.Settings.Master.ItemSettings.fort_modifier', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=789,
  serialized_end=1738,
)

_ITEMSETTINGS.fields_by_name['item_id'].enum_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2._ITEMID
_ITEMSETTINGS.fields_by_name['item_type'].enum_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemType__pb2._ITEMTYPE
_ITEMSETTINGS.fields_by_name['category'].enum_type = POGOProtos_dot_Enums_dot_ItemCategory__pb2._ITEMCATEGORY
_ITEMSETTINGS.fields_by_name['pokeball'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_PokeballAttributes__pb2._POKEBALLATTRIBUTES
_ITEMSETTINGS.fields_by_name['potion'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_PotionAttributes__pb2._POTIONATTRIBUTES
_ITEMSETTINGS.fields_by_name['revive'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_ReviveAttributes__pb2._REVIVEATTRIBUTES
_ITEMSETTINGS.fields_by_name['battle'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_BattleAttributes__pb2._BATTLEATTRIBUTES
_ITEMSETTINGS.fields_by_name['food'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_FoodAttributes__pb2._FOODATTRIBUTES
_ITEMSETTINGS.fields_by_name['inventory_upgrade'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_InventoryUpgradeAttributes__pb2._INVENTORYUPGRADEATTRIBUTES
_ITEMSETTINGS.fields_by_name['xp_boost'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_ExperienceBoostAttributes__pb2._EXPERIENCEBOOSTATTRIBUTES
_ITEMSETTINGS.fields_by_name['incense'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_IncenseAttributes__pb2._INCENSEATTRIBUTES
_ITEMSETTINGS.fields_by_name['egg_incubator'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_EggIncubatorAttributes__pb2._EGGINCUBATORATTRIBUTES
_ITEMSETTINGS.fields_by_name['fort_modifier'].message_type = POGOProtos_dot_Settings_dot_Master_dot_Item_dot_FortModifierAttributes__pb2._FORTMODIFIERATTRIBUTES
DESCRIPTOR.message_types_by_name['ItemSettings'] = _ITEMSETTINGS

ItemSettings = _reflection.GeneratedProtocolMessageType('ItemSettings', (_message.Message,), dict(
  DESCRIPTOR = _ITEMSETTINGS,
  __module__ = 'POGOProtos.Settings.Master.ItemSettings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Master.ItemSettings)
  ))
_sym_db.RegisterMessage(ItemSettings)


# @@protoc_insertion_point(module_scope)
