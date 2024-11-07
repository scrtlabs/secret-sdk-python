# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/orm/v1alpha1/schema.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class StorageType(betterproto.Enum):
    """StorageType"""

    STORAGE_TYPE_DEFAULT_UNSPECIFIED = 0
    """
    STORAGE_TYPE_DEFAULT_UNSPECIFIED indicates the persistent storage where all
    data is stored in the regular Merkle-tree backed KV-store.
    """

    STORAGE_TYPE_MEMORY = 1
    """
    STORAGE_TYPE_MEMORY indicates in-memory storage that will be reloaded every
    time an app restarts. Tables with this type of storage will by default be
    ignored when importing and exporting a module's state from JSON.
    """

    STORAGE_TYPE_TRANSIENT = 2
    """
    STORAGE_TYPE_TRANSIENT indicates transient storage that is reset at the end
    of every block. Tables with this type of storage will by default be ignored
    when importing and exporting a module's state from JSON.
    """


@dataclass(eq=False, repr=False)
class ModuleSchemaDescriptor(betterproto.Message):
    """ModuleSchemaDescriptor describe's a module's ORM schema."""

    schema_file: List["ModuleSchemaDescriptorFileEntry"] = betterproto.message_field(1)
    prefix: bytes = betterproto.bytes_field(2)
    """
    prefix is an optional prefix that precedes all keys in this module's store.
    """


@dataclass(eq=False, repr=False)
class ModuleSchemaDescriptorFileEntry(betterproto.Message):
    """FileEntry describes an ORM file used in a module."""

    id: int = betterproto.uint32_field(1)
    """
    id is a prefix that will be varint encoded and prepended to all the table
    keys specified in the file's tables.
    """

    proto_file_name: str = betterproto.string_field(2)
    """
    proto_file_name is the name of a file .proto in that contains table
    definitions. The .proto file must be in a package that the module has
    referenced using cosmos.app.v1.ModuleDescriptor.use_package.
    """

    storage_type: "StorageType" = betterproto.enum_field(3)
    """
    storage_type optionally indicates the type of storage this file's tables
    should used. If it is left unspecified, the default KV-storage of the app
    will be used.
    """