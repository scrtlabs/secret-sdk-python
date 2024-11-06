# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/orm/query/v1alpha1/query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional

import betterproto
import grpclib

from .cosmos.base.query import v1beta1
from .google import protobuf


@dataclass
class GetRequest(betterproto.Message):
    """GetRequest is the Query/Get request type."""

    # message_name is the fully-qualified message name of the ORM table being
    # queried.
    message_name: str = betterproto.string_field(1)
    # index is the index fields expression used in orm definitions. If it is
    # empty, the table's primary key is assumed. If it is non-empty, it must
    # refer to an unique index.
    index: str = betterproto.string_field(2)
    # values are the values of the fields corresponding to the requested index.
    # There must be as many values provided as there are fields in the index and
    # these values must correspond to the index field types.
    values: List["IndexValue"] = betterproto.message_field(3)


@dataclass
class GetResponse(betterproto.Message):
    """GetResponse is the Query/Get response type."""

    # result is the result of the get query. If no value is found, the gRPC
    # status code NOT_FOUND will be returned.
    result: protobuf.Any = betterproto.message_field(1)


@dataclass
class ListRequest(betterproto.Message):
    """ListRequest is the Query/List request type."""

    # message_name is the fully-qualified message name of the ORM table being
    # queried.
    message_name: str = betterproto.string_field(1)
    # index is the index fields expression used in orm definitions. If it is
    # empty, the table's primary key is assumed.
    index: str = betterproto.string_field(2)
    # prefix defines a prefix query.
    prefix: "ListRequestPrefix" = betterproto.message_field(3, group="query")
    # range defines a range query.
    range: "ListRequestRange" = betterproto.message_field(4, group="query")
    # pagination is the pagination request.
    pagination: v1beta1.PageRequest = betterproto.message_field(5)


@dataclass
class ListRequestPrefix(betterproto.Message):
    """Prefix specifies the arguments to a prefix query."""

    # values specifies the index values for the prefix query. It is valid to
    # special a partial prefix with fewer values than the number of fields in the
    # index.
    values: List["IndexValue"] = betterproto.message_field(1)


@dataclass
class ListRequestRange(betterproto.Message):
    """Range specifies the arguments to a range query."""

    # start specifies the starting index values for the range query. It is valid
    # to provide fewer values than the number of fields in the index.
    start: List["IndexValue"] = betterproto.message_field(1)
    # end specifies the inclusive ending index values for the range query. It is
    # valid to provide fewer values than the number of fields in the index.
    end: List["IndexValue"] = betterproto.message_field(2)


@dataclass
class ListResponse(betterproto.Message):
    """ListResponse is the Query/List response type."""

    # results are the results of the query.
    results: List[protobuf.Any] = betterproto.message_field(1)
    # pagination is the pagination response.
    pagination: v1beta1.PageResponse = betterproto.message_field(5)


@dataclass
class IndexValue(betterproto.Message):
    """
    IndexValue represents the value of a field in an ORM index expression.
    """

    # uint specifies a value for an uint32, fixed32, uint64, or fixed64 index
    # field.
    uint: int = betterproto.uint64_field(1, group="value")
    # int64 specifies a value for an int32, sfixed32, int64, or sfixed64 index
    # field.
    int: int = betterproto.int64_field(2, group="value")
    # str specifies a value for a string index field.
    str: str = betterproto.string_field(3, group="value")
    # bytes specifies a value for a bytes index field.
    bytes: bytes = betterproto.bytes_field(4, group="value")
    # enum specifies a value for an enum index field.
    enum: str = betterproto.string_field(5, group="value")
    # bool specifies a value for a bool index field.
    bool: bool = betterproto.bool_field(6, group="value")
    # timestamp specifies a value for a timestamp index field.
    timestamp: datetime = betterproto.message_field(7, group="value")
    # duration specifies a value for a duration index field.
    duration: timedelta = betterproto.message_field(8, group="value")


class QueryStub(betterproto.ServiceStub):
    """Query is a generic gRPC service for querying ORM data."""

    async def get(
        self,
        *,
        message_name: str = "",
        index: str = "",
        values: List["IndexValue"] = [],
    ) -> GetResponse:
        """Get queries an ORM table against an unique index."""

        request = GetRequest()
        request.message_name = message_name
        request.index = index
        if values is not None:
            request.values = values

        return await self._unary_unary(
            "/cosmos.orm.query.v1alpha1.Query/Get",
            request,
            GetResponse,
        )

    async def list(
        self,
        *,
        message_name: str = "",
        index: str = "",
        prefix: Optional["ListRequestPrefix"] = None,
        range: Optional["ListRequestRange"] = None,
        pagination: Optional[v1beta1.PageRequest] = None,
    ) -> ListResponse:
        """List queries an ORM table against an index."""

        request = ListRequest()
        request.message_name = message_name
        request.index = index
        if prefix is not None:
            request.prefix = prefix
        if range is not None:
            request.range = range
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.orm.query.v1alpha1.Query/List",
            request,
            ListResponse,
        )
