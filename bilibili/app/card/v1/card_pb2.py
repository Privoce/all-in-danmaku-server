# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/app/card/v1/card.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilibili.app.card.v1 import single_pb2 as bilibili_dot_app_dot_card_dot_v1_dot_single__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bilibili/app/card/v1/card.proto',
  package='bilibili.app.card.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x62ilibili/app/card/v1/card.proto\x12\x14\x62ilibili.app.card.v1\x1a!bilibili/app/card/v1/single.proto\"\xe8\x04\n\x04\x43\x61rd\x12:\n\x0csmallCoverV5\x18\x01 \x01(\x0b\x32\".bilibili.app.card.v1.SmallCoverV5H\x00\x12:\n\x0clargeCoverV1\x18\x02 \x01(\x0b\x32\".bilibili.app.card.v1.LargeCoverV1H\x00\x12>\n\x0ethreeItemAllV2\x18\x03 \x01(\x0b\x32$.bilibili.app.card.v1.ThreeItemAllV2H\x00\x12\x38\n\x0bthreeItemV1\x18\x04 \x01(\x0b\x32!.bilibili.app.card.v1.ThreeItemV1H\x00\x12\x32\n\x08hotTopic\x18\x05 \x01(\x0b\x32\x1e.bilibili.app.card.v1.HotTopicH\x00\x12\x36\n\ndynamicHot\x18\x06 \x01(\x0b\x32 .bilibili.app.card.v1.DynamicHotH\x00\x12<\n\rmiddleCoverV3\x18\x07 \x01(\x0b\x32#.bilibili.app.card.v1.MiddleCoverV3H\x00\x12:\n\x0clargeCoverV4\x18\x08 \x01(\x0b\x32\".bilibili.app.card.v1.LargeCoverV4H\x00\x12\x46\n\x12popularTopEntrance\x18\t \x01(\x0b\x32(.bilibili.app.card.v1.PopularTopEntranceH\x00\x12\x38\n\x0brcmdOneItem\x18\n \x01(\x0b\x32!.bilibili.app.card.v1.RcmdOneItemH\x00\x42\x06\n\x04itemb\x06proto3'
  ,
  dependencies=[bilibili_dot_app_dot_card_dot_v1_dot_single__pb2.DESCRIPTOR,])




_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='bilibili.app.card.v1.Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='smallCoverV5', full_name='bilibili.app.card.v1.Card.smallCoverV5', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='largeCoverV1', full_name='bilibili.app.card.v1.Card.largeCoverV1', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threeItemAllV2', full_name='bilibili.app.card.v1.Card.threeItemAllV2', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threeItemV1', full_name='bilibili.app.card.v1.Card.threeItemV1', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hotTopic', full_name='bilibili.app.card.v1.Card.hotTopic', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dynamicHot', full_name='bilibili.app.card.v1.Card.dynamicHot', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='middleCoverV3', full_name='bilibili.app.card.v1.Card.middleCoverV3', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='largeCoverV4', full_name='bilibili.app.card.v1.Card.largeCoverV4', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='popularTopEntrance', full_name='bilibili.app.card.v1.Card.popularTopEntrance', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rcmdOneItem', full_name='bilibili.app.card.v1.Card.rcmdOneItem', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='item', full_name='bilibili.app.card.v1.Card.item',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=93,
  serialized_end=709,
)

_CARD.fields_by_name['smallCoverV5'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._SMALLCOVERV5
_CARD.fields_by_name['largeCoverV1'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._LARGECOVERV1
_CARD.fields_by_name['threeItemAllV2'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._THREEITEMALLV2
_CARD.fields_by_name['threeItemV1'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._THREEITEMV1
_CARD.fields_by_name['hotTopic'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._HOTTOPIC
_CARD.fields_by_name['dynamicHot'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._DYNAMICHOT
_CARD.fields_by_name['middleCoverV3'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._MIDDLECOVERV3
_CARD.fields_by_name['largeCoverV4'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._LARGECOVERV4
_CARD.fields_by_name['popularTopEntrance'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._POPULARTOPENTRANCE
_CARD.fields_by_name['rcmdOneItem'].message_type = bilibili_dot_app_dot_card_dot_v1_dot_single__pb2._RCMDONEITEM
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['smallCoverV5'])
_CARD.fields_by_name['smallCoverV5'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['largeCoverV1'])
_CARD.fields_by_name['largeCoverV1'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['threeItemAllV2'])
_CARD.fields_by_name['threeItemAllV2'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['threeItemV1'])
_CARD.fields_by_name['threeItemV1'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['hotTopic'])
_CARD.fields_by_name['hotTopic'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['dynamicHot'])
_CARD.fields_by_name['dynamicHot'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['middleCoverV3'])
_CARD.fields_by_name['middleCoverV3'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['largeCoverV4'])
_CARD.fields_by_name['largeCoverV4'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['popularTopEntrance'])
_CARD.fields_by_name['popularTopEntrance'].containing_oneof = _CARD.oneofs_by_name['item']
_CARD.oneofs_by_name['item'].fields.append(
  _CARD.fields_by_name['rcmdOneItem'])
_CARD.fields_by_name['rcmdOneItem'].containing_oneof = _CARD.oneofs_by_name['item']
DESCRIPTOR.message_types_by_name['Card'] = _CARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), {
  'DESCRIPTOR' : _CARD,
  '__module__' : 'bilibili.app.card.v1.card_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.app.card.v1.Card)
  })
_sym_db.RegisterMessage(Card)


# @@protoc_insertion_point(module_scope)
