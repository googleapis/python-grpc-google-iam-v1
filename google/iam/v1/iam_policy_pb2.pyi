from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import options_pb2 as _options_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetIamPolicyRequest(_message.Message):
    __slots__ = ("resource", "policy", "update_mask")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    resource: str
    policy: _policy_pb2.Policy
    update_mask: _field_mask_pb2.FieldMask
    def __init__(
        self,
        resource: _Optional[str] = ...,
        policy: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...,
        update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...,
    ) -> None: ...

class GetIamPolicyRequest(_message.Message):
    __slots__ = ("resource", "options")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    resource: str
    options: _options_pb2.GetPolicyOptions
    def __init__(
        self,
        resource: _Optional[str] = ...,
        options: _Optional[_Union[_options_pb2.GetPolicyOptions, _Mapping]] = ...,
    ) -> None: ...

class TestIamPermissionsRequest(_message.Message):
    __slots__ = ("resource", "permissions")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    resource: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        resource: _Optional[str] = ...,
        permissions: _Optional[_Iterable[str]] = ...,
    ) -> None: ...

class TestIamPermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, permissions: _Optional[_Iterable[str]] = ...) -> None: ...
