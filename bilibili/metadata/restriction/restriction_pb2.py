# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/metadata/restriction/restriction.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bilibili/metadata/restriction/restriction.proto',
  package='bilibili.metadata.restriction',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/bilibili/metadata/restriction/restriction.proto\x12\x1d\x62ilibili.metadata.restriction\"\x82\x01\n\x0bRestriction\x12\x16\n\x0eteenagers_mode\x18\x01 \x01(\x08\x12\x14\n\x0clessons_mode\x18\x02 \x01(\x08\x12\x35\n\x04mode\x18\x03 \x01(\x0e\x32\'.bilibili.metadata.restriction.ModeType\x12\x0e\n\x06review\x18\x04 \x01(\x08*2\n\x08ModeType\x12\n\n\x06NORMAL\x10\x00\x12\r\n\tTEENAGERS\x10\x01\x12\x0b\n\x07LESSONS\x10\x02\x62\x06proto3'
)

_MODETYPE = _descriptor.EnumDescriptor(
  name='ModeType',
  full_name='bilibili.metadata.restriction.ModeType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEENAGERS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LESSONS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=215,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_MODETYPE)

ModeType = enum_type_wrapper.EnumTypeWrapper(_MODETYPE)
NORMAL = 0
TEENAGERS = 1
LESSONS = 2



_RESTRICTION = _descriptor.Descriptor(
  name='Restriction',
  full_name='bilibili.metadata.restriction.Restriction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='teenagers_mode', full_name='bilibili.metadata.restriction.Restriction.teenagers_mode', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lessons_mode', full_name='bilibili.metadata.restriction.Restriction.lessons_mode', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='bilibili.metadata.restriction.Restriction.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='review', full_name='bilibili.metadata.restriction.Restriction.review', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  ],
  serialized_start=83,
  serialized_end=213,
)

_RESTRICTION.fields_by_name['mode'].enum_type = _MODETYPE
DESCRIPTOR.message_types_by_name['Restriction'] = _RESTRICTION
DESCRIPTOR.enum_types_by_name['ModeType'] = _MODETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Restriction = _reflection.GeneratedProtocolMessageType('Restriction', (_message.Message,), {
  'DESCRIPTOR' : _RESTRICTION,
  '__module__' : 'bilibili.metadata.restriction.restriction_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.metadata.restriction.Restriction)
  })
_sym_db.RegisterMessage(Restriction)


# @@protoc_insertion_point(module_scope)
