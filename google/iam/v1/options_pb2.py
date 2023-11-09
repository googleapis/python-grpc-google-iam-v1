# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/iam/v1/options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1bgoogle/iam/v1/options.proto\x12\rgoogle.iam.v1"4\n\x10GetPolicyOptions\x12 \n\x18requested_policy_version\x18\x01 \x01(\x05\x42}\n\x11\x63om.google.iam.v1B\x0cOptionsProtoP\x01Z)cloud.google.com/go/iam/apiv1/iampb;iampb\xf8\x01\x01\xaa\x02\x13Google.Cloud.Iam.V1\xca\x02\x13Google\\Cloud\\Iam\\V1b\x06proto3'
)


_GETPOLICYOPTIONS = DESCRIPTOR.message_types_by_name["GetPolicyOptions"]
GetPolicyOptions = _reflection.GeneratedProtocolMessageType(
    "GetPolicyOptions",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPOLICYOPTIONS,
        "__module__": "google.iam.v1.options_pb2"
        # @@protoc_insertion_point(class_scope:google.iam.v1.GetPolicyOptions)
    },
)
_sym_db.RegisterMessage(GetPolicyOptions)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\021com.google.iam.v1B\014OptionsProtoP\001Z)cloud.google.com/go/iam/apiv1/iampb;iampb\370\001\001\252\002\023Google.Cloud.Iam.V1\312\002\023Google\\Cloud\\Iam\\V1"
    _GETPOLICYOPTIONS._serialized_start = 46
    _GETPOLICYOPTIONS._serialized_end = 98
# @@protoc_insertion_point(module_scope)
