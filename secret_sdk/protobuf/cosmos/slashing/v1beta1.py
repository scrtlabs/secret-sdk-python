# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/slashing/v1beta1/slashing.proto, cosmos/slashing/v1beta1/tx.proto, cosmos/slashing/v1beta1/genesis.proto, cosmos/slashing/v1beta1/query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional

import betterproto
import grpclib

from .cosmos.base.query import v1beta1


@dataclass
class ValidatorSigningInfo(betterproto.Message):
    """
    ValidatorSigningInfo defines a validator's signing info for monitoring
    their liveness activity.
    """

    address: str = betterproto.string_field(1)
    # Height at which validator was first a candidate OR was un-jailed
    start_height: int = betterproto.int64_field(2)
    # Index which is incremented every time a validator is bonded in a block and
    # _may_ have signed a pre-commit or not. This in conjunction with the
    # signed_blocks_window param determines the index in the missed block bitmap.
    index_offset: int = betterproto.int64_field(3)
    # Timestamp until which the validator is jailed due to liveness downtime.
    jailed_until: datetime = betterproto.message_field(4)
    # Whether or not a validator has been tombstoned (killed out of validator
    # set). It is set once the validator commits an equivocation or for any other
    # configured misbehavior.
    tombstoned: bool = betterproto.bool_field(5)
    # A counter of missed (unsigned) blocks. It is used to avoid unnecessary
    # reads in the missed block bitmap.
    missed_blocks_counter: int = betterproto.int64_field(6)


@dataclass
class Params(betterproto.Message):
    """Params represents the parameters used for by the slashing module."""

    signed_blocks_window: int = betterproto.int64_field(1)
    min_signed_per_window: bytes = betterproto.bytes_field(2)
    downtime_jail_duration: timedelta = betterproto.message_field(3)
    slash_fraction_double_sign: bytes = betterproto.bytes_field(4)
    slash_fraction_downtime: bytes = betterproto.bytes_field(5)


@dataclass
class MsgUnjail(betterproto.Message):
    """MsgUnjail defines the Msg/Unjail request type"""

    validator_addr: str = betterproto.string_field(1)


@dataclass
class MsgUnjailResponse(betterproto.Message):
    """MsgUnjailResponse defines the Msg/Unjail response type"""

    pass


@dataclass
class MsgUpdateParams(betterproto.Message):
    """
    MsgUpdateParams is the Msg/UpdateParams request type. Since: cosmos-sdk
    0.47
    """

    # authority is the address that controls the module (defaults to x/gov unless
    # overwritten).
    authority: str = betterproto.string_field(1)
    # params defines the x/slashing parameters to update. NOTE: All parameters
    # must be supplied.
    params: "Params" = betterproto.message_field(2)


@dataclass
class MsgUpdateParamsResponse(betterproto.Message):
    """
    MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message. Since: cosmos-sdk 0.47
    """

    pass


@dataclass
class GenesisState(betterproto.Message):
    """GenesisState defines the slashing module's genesis state."""

    # params defines all the parameters of the module.
    params: "Params" = betterproto.message_field(1)
    # signing_infos represents a map between validator addresses and their
    # signing infos.
    signing_infos: List["SigningInfo"] = betterproto.message_field(2)
    # missed_blocks represents a map between validator addresses and their missed
    # blocks.
    missed_blocks: List["ValidatorMissedBlocks"] = betterproto.message_field(3)


@dataclass
class SigningInfo(betterproto.Message):
    """SigningInfo stores validator signing info of corresponding address."""

    # address is the validator address.
    address: str = betterproto.string_field(1)
    # validator_signing_info represents the signing info of this validator.
    validator_signing_info: "ValidatorSigningInfo" = betterproto.message_field(2)


@dataclass
class ValidatorMissedBlocks(betterproto.Message):
    """
    ValidatorMissedBlocks contains array of missed blocks of corresponding
    address.
    """

    # address is the validator address.
    address: str = betterproto.string_field(1)
    # missed_blocks is an array of missed blocks by the validator.
    missed_blocks: List["MissedBlock"] = betterproto.message_field(2)


@dataclass
class MissedBlock(betterproto.Message):
    """MissedBlock contains height and missed status as boolean."""

    # index is the height at which the block was missed.
    index: int = betterproto.int64_field(1)
    # missed is the missed status.
    missed: bool = betterproto.bool_field(2)


@dataclass
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method
    """

    pass


@dataclass
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method
    """

    params: "Params" = betterproto.message_field(1)


@dataclass
class QuerySigningInfoRequest(betterproto.Message):
    """
    QuerySigningInfoRequest is the request type for the Query/SigningInfo RPC
    method
    """

    # cons_address is the address to query signing info of
    cons_address: str = betterproto.string_field(1)


@dataclass
class QuerySigningInfoResponse(betterproto.Message):
    """
    QuerySigningInfoResponse is the response type for the Query/SigningInfo RPC
    method
    """

    # val_signing_info is the signing info of requested val cons address
    val_signing_info: "ValidatorSigningInfo" = betterproto.message_field(1)


@dataclass
class QuerySigningInfosRequest(betterproto.Message):
    """
    QuerySigningInfosRequest is the request type for the Query/SigningInfos RPC
    method
    """

    pagination: v1beta1.PageRequest = betterproto.message_field(1)


@dataclass
class QuerySigningInfosResponse(betterproto.Message):
    """
    QuerySigningInfosResponse is the response type for the Query/SigningInfos
    RPC method
    """

    # info is the signing info of all validators
    info: List["ValidatorSigningInfo"] = betterproto.message_field(1)
    pagination: v1beta1.PageResponse = betterproto.message_field(2)


class MsgStub(betterproto.ServiceStub):
    """Msg defines the slashing Msg service."""

    async def unjail(self, *, validator_addr: str = "") -> MsgUnjailResponse:
        """
        Unjail defines a method for unjailing a jailed validator, thus
        returning them into the bonded validator set, so they can begin
        receiving provisions and rewards again.
        """

        request = MsgUnjail()
        request.validator_addr = validator_addr

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Msg/Unjail",
            request,
            MsgUnjailResponse,
        )

    async def update_params(
        self, *, authority: str = "", params: Optional["Params"] = None
    ) -> MsgUpdateParamsResponse:
        """
        UpdateParams defines a governance operation for updating the x/slashing
        module parameters. The authority defaults to the x/gov module account.
        Since: cosmos-sdk 0.47
        """

        request = MsgUpdateParams()
        request.authority = authority
        if params is not None:
            request.params = params

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Msg/UpdateParams",
            request,
            MsgUpdateParamsResponse,
        )


class QueryStub(betterproto.ServiceStub):
    """Query provides defines the gRPC querier service"""

    async def params(self) -> QueryParamsResponse:
        """Params queries the parameters of slashing module"""

        request = QueryParamsRequest()

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/Params",
            request,
            QueryParamsResponse,
        )

    async def signing_info(self, *, cons_address: str = "") -> QuerySigningInfoResponse:
        """SigningInfo queries the signing info of given cons address"""

        request = QuerySigningInfoRequest()
        request.cons_address = cons_address

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/SigningInfo",
            request,
            QuerySigningInfoResponse,
        )

    async def signing_infos(
        self, *, pagination: Optional[v1beta1.PageRequest] = None
    ) -> QuerySigningInfosResponse:
        """SigningInfos queries signing info of all validators"""

        request = QuerySigningInfosRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.slashing.v1beta1.Query/SigningInfos",
            request,
            QuerySigningInfosResponse,
        )
