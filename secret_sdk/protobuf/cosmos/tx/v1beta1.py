# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/tx/v1beta1/tx.proto, cosmos/tx/v1beta1/service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib

from .cosmos.base import v1beta1
from .cosmos.base.abci import v1beta1
from .cosmos.base.query import v1beta1
from .cosmos.crypto.multisig import v1beta1
from .cosmos.tx.signing import v1beta1
from .google import protobuf
from .tendermint import types


class OrderBy(betterproto.Enum):
    """OrderBy defines the sorting order"""

    # ORDER_BY_UNSPECIFIED specifies an unknown sorting order. OrderBy defaults
    # to ASC in this case.
    ORDER_BY_UNSPECIFIED = 0
    # ORDER_BY_ASC defines ascending order
    ORDER_BY_ASC = 1
    # ORDER_BY_DESC defines descending order
    ORDER_BY_DESC = 2


class BroadcastMode(betterproto.Enum):
    """
    BroadcastMode specifies the broadcast mode for the TxService.Broadcast RPC
    method.
    """

    # zero-value for mode ordering
    BROADCAST_MODE_UNSPECIFIED = 0
    # DEPRECATED: use BROADCAST_MODE_SYNC instead, BROADCAST_MODE_BLOCK is not
    # supported by the SDK from v0.47.x onwards.
    BROADCAST_MODE_BLOCK = 1
    # BROADCAST_MODE_SYNC defines a tx broadcasting mode where the client waits
    # for a CheckTx execution response only.
    BROADCAST_MODE_SYNC = 2
    # BROADCAST_MODE_ASYNC defines a tx broadcasting mode where the client
    # returns immediately.
    BROADCAST_MODE_ASYNC = 3


@dataclass
class Tx(betterproto.Message):
    """Tx is the standard type used for broadcasting transactions."""

    # body is the processable content of the transaction
    body: "TxBody" = betterproto.message_field(1)
    # auth_info is the authorization related content of the transaction,
    # specifically signers, signer modes and fee
    auth_info: "AuthInfo" = betterproto.message_field(2)
    # signatures is a list of signatures that matches the length and order of
    # AuthInfo's signer_infos to allow connecting signature meta information like
    # public key and signing mode by position.
    signatures: List[bytes] = betterproto.bytes_field(3)


@dataclass
class TxRaw(betterproto.Message):
    """
    TxRaw is a variant of Tx that pins the signer's exact binary representation
    of body and auth_info. This is used for signing, broadcasting and
    verification. The binary `serialize(tx: TxRaw)` is stored in Tendermint and
    the hash `sha256(serialize(tx: TxRaw))` becomes the "txhash", commonly used
    as the transaction ID.
    """

    # body_bytes is a protobuf serialization of a TxBody that matches the
    # representation in SignDoc.
    body_bytes: bytes = betterproto.bytes_field(1)
    # auth_info_bytes is a protobuf serialization of an AuthInfo that matches the
    # representation in SignDoc.
    auth_info_bytes: bytes = betterproto.bytes_field(2)
    # signatures is a list of signatures that matches the length and order of
    # AuthInfo's signer_infos to allow connecting signature meta information like
    # public key and signing mode by position.
    signatures: List[bytes] = betterproto.bytes_field(3)


@dataclass
class SignDoc(betterproto.Message):
    """
    SignDoc is the type used for generating sign bytes for SIGN_MODE_DIRECT.
    """

    # body_bytes is protobuf serialization of a TxBody that matches the
    # representation in TxRaw.
    body_bytes: bytes = betterproto.bytes_field(1)
    # auth_info_bytes is a protobuf serialization of an AuthInfo that matches the
    # representation in TxRaw.
    auth_info_bytes: bytes = betterproto.bytes_field(2)
    # chain_id is the unique identifier of the chain this transaction targets. It
    # prevents signed transactions from being used on another chain by an
    # attacker
    chain_id: str = betterproto.string_field(3)
    # account_number is the account number of the account in state
    account_number: int = betterproto.uint64_field(4)


@dataclass
class SignDocDirectAux(betterproto.Message):
    """
    SignDocDirectAux is the type used for generating sign bytes for
    SIGN_MODE_DIRECT_AUX. Since: cosmos-sdk 0.46
    """

    # body_bytes is protobuf serialization of a TxBody that matches the
    # representation in TxRaw.
    body_bytes: bytes = betterproto.bytes_field(1)
    # public_key is the public key of the signing account.
    public_key: protobuf.Any = betterproto.message_field(2)
    # chain_id is the identifier of the chain this transaction targets. It
    # prevents signed transactions from being used on another chain by an
    # attacker.
    chain_id: str = betterproto.string_field(3)
    # account_number is the account number of the account in state.
    account_number: int = betterproto.uint64_field(4)
    # sequence is the sequence number of the signing account.
    sequence: int = betterproto.uint64_field(5)
    # tips have been depreacted and should not be used
    tip: "Tip" = betterproto.message_field(6)


@dataclass
class TxBody(betterproto.Message):
    """TxBody is the body of a transaction that all signers sign over."""

    # messages is a list of messages to be executed. The required signers of
    # those messages define the number and order of elements in AuthInfo's
    # signer_infos and Tx's signatures. Each required signer address is added to
    # the list only the first time it occurs. By convention, the first required
    # signer (usually from the first message) is referred to as the primary
    # signer and pays the fee for the whole transaction.
    messages: List[protobuf.Any] = betterproto.message_field(1)
    # memo is any arbitrary note/comment to be added to the transaction. WARNING:
    # in clients, any publicly exposed text should not be called memo, but should
    # be called `note` instead (see https://github.com/cosmos/cosmos-
    # sdk/issues/9122).
    memo: str = betterproto.string_field(2)
    # timeout is the block height after which this transaction will not be
    # processed by the chain
    timeout_height: int = betterproto.uint64_field(3)
    # extension_options are arbitrary options that can be added by chains when
    # the default options are not sufficient. If any of these are present and
    # can't be handled, the transaction will be rejected
    extension_options: List[protobuf.Any] = betterproto.message_field(1023)
    # extension_options are arbitrary options that can be added by chains when
    # the default options are not sufficient. If any of these are present and
    # can't be handled, they will be ignored
    non_critical_extension_options: List[protobuf.Any] = betterproto.message_field(2047)


@dataclass
class AuthInfo(betterproto.Message):
    """
    AuthInfo describes the fee and signer modes that are used to sign a
    transaction.
    """

    # signer_infos defines the signing modes for the required signers. The number
    # and order of elements must match the required signers from TxBody's
    # messages. The first element is the primary signer and the one which pays
    # the fee.
    signer_infos: List["SignerInfo"] = betterproto.message_field(1)
    # Fee is the fee and gas limit for the transaction. The first signer is the
    # primary signer and the one which pays the fee. The fee can be calculated
    # based on the cost of evaluating the body and doing signature verification
    # of the signers. This can be estimated via simulation.
    fee: "Fee" = betterproto.message_field(2)
    # Tip is the optional tip used for transactions fees paid in another denom.
    # This field is ignored if the chain didn't enable tips, i.e. didn't add the
    # `TipDecorator` in its posthandler. Since: cosmos-sdk 0.46
    tip: "Tip" = betterproto.message_field(3)


@dataclass
class SignerInfo(betterproto.Message):
    """
    SignerInfo describes the public key and signing mode of a single top-level
    signer.
    """

    # public_key is the public key of the signer. It is optional for accounts
    # that already exist in state. If unset, the verifier can use the required \
    # signer address for this position and lookup the public key.
    public_key: protobuf.Any = betterproto.message_field(1)
    # mode_info describes the signing mode of the signer and is a nested
    # structure to support nested multisig pubkey's
    mode_info: "ModeInfo" = betterproto.message_field(2)
    # sequence is the sequence of the account, which describes the number of
    # committed transactions signed by a given address. It is used to prevent
    # replay attacks.
    sequence: int = betterproto.uint64_field(3)


@dataclass
class ModeInfo(betterproto.Message):
    """
    ModeInfo describes the signing mode of a single or nested multisig signer.
    """

    # single represents a single signer
    single: "ModeInfoSingle" = betterproto.message_field(1, group="sum")
    # multi represents a nested multisig signer
    multi: "ModeInfoMulti" = betterproto.message_field(2, group="sum")


@dataclass
class ModeInfoSingle(betterproto.Message):
    """
    Single is the mode info for a single signer. It is structured as a message
    to allow for additional fields such as locale for SIGN_MODE_TEXTUAL in the
    future
    """

    # mode is the signing mode of the single signer
    mode: v1beta1.SignMode = betterproto.enum_field(1)


@dataclass
class ModeInfoMulti(betterproto.Message):
    """Multi is the mode info for a multisig public key"""

    # bitarray specifies which keys within the multisig are signing
    bitarray: v1beta1.CompactBitArray = betterproto.message_field(1)
    # mode_infos is the corresponding modes of the signers of the multisig which
    # could include nested multisig public keys
    mode_infos: List["ModeInfo"] = betterproto.message_field(2)


@dataclass
class Fee(betterproto.Message):
    """
    Fee includes the amount of coins paid in fees and the maximum gas to be
    used by the transaction. The ratio yields an effective "gasprice", which
    must be above some miminum to be accepted into the mempool.
    """

    # amount is the amount of coins to be paid as a fee
    amount: List[v1beta1.Coin] = betterproto.message_field(1)
    # gas_limit is the maximum gas that can be used in transaction processing
    # before an out of gas error occurs
    gas_limit: int = betterproto.uint64_field(2)
    # if unset, the first signer is responsible for paying the fees. If set, the
    # specified account must pay the fees. the payer must be a tx signer (and
    # thus have signed this field in AuthInfo). setting this field does *not*
    # change the ordering of required signers for the transaction.
    payer: str = betterproto.string_field(3)
    # if set, the fee payer (either the first signer or the value of the payer
    # field) requests that a fee grant be used to pay fees instead of the fee
    # payer's own balance. If an appropriate fee grant does not exist or the
    # chain does not support fee grants, this will fail
    granter: str = betterproto.string_field(4)


@dataclass
class Tip(betterproto.Message):
    """Tip is the tip used for meta-transactions. Since: cosmos-sdk 0.46"""

    # amount is the amount of the tip
    amount: List[v1beta1.Coin] = betterproto.message_field(1)
    # tipper is the address of the account paying for the tip
    tipper: str = betterproto.string_field(2)


@dataclass
class AuxSignerData(betterproto.Message):
    """
    AuxSignerData is the intermediary format that an auxiliary signer (e.g. a
    tipper) builds and sends to the fee payer (who will build and broadcast the
    actual tx). AuxSignerData is not a valid tx in itself, and will be rejected
    by the node if sent directly as-is. Since: cosmos-sdk 0.46
    """

    # address is the bech32-encoded address of the auxiliary signer. If using
    # AuxSignerData across different chains, the bech32 prefix of the target
    # chain (where the final transaction is broadcasted) should be used.
    address: str = betterproto.string_field(1)
    # sign_doc is the SIGN_MODE_DIRECT_AUX sign doc that the auxiliary signer
    # signs. Note: we use the same sign doc even if we're signing with
    # LEGACY_AMINO_JSON.
    sign_doc: "SignDocDirectAux" = betterproto.message_field(2)
    # mode is the signing mode of the single signer.
    mode: v1beta1.SignMode = betterproto.enum_field(3)
    # sig is the signature of the sign doc.
    sig: bytes = betterproto.bytes_field(4)


@dataclass
class GetTxsEventRequest(betterproto.Message):
    """
    GetTxsEventRequest is the request type for the Service.TxsByEvents RPC
    method.
    """

    # events is the list of transaction event type. Deprecated post v0.47.x: use
    # query instead, which should contain a valid events query.
    events: List[str] = betterproto.string_field(1)
    # pagination defines a pagination for the request. Deprecated post v0.46.x:
    # use page and limit instead.
    pagination: v1beta1.PageRequest = betterproto.message_field(2)
    order_by: "OrderBy" = betterproto.enum_field(3)
    # page is the page number to query, starts at 1. If not provided, will
    # default to first page.
    page: int = betterproto.uint64_field(4)
    # limit is the total number of results to be returned in the result page. If
    # left empty it will default to a value to be set by each app.
    limit: int = betterproto.uint64_field(5)
    # query defines the transaction event query that is proxied to Tendermint's
    # TxSearch RPC method. The query must be valid. Since cosmos-sdk 0.50
    query: str = betterproto.string_field(6)


@dataclass
class GetTxsEventResponse(betterproto.Message):
    """
    GetTxsEventResponse is the response type for the Service.TxsByEvents RPC
    method.
    """

    # txs is the list of queried transactions.
    txs: List["Tx"] = betterproto.message_field(1)
    # tx_responses is the list of queried TxResponses.
    tx_responses: List[v1beta1.TxResponse] = betterproto.message_field(2)
    # pagination defines a pagination for the response. Deprecated post v0.46.x:
    # use total instead.
    pagination: v1beta1.PageResponse = betterproto.message_field(3)
    # total is total number of results available
    total: int = betterproto.uint64_field(4)


@dataclass
class BroadcastTxRequest(betterproto.Message):
    """
    BroadcastTxRequest is the request type for the Service.BroadcastTxRequest
    RPC method.
    """

    # tx_bytes is the raw transaction.
    tx_bytes: bytes = betterproto.bytes_field(1)
    mode: "BroadcastMode" = betterproto.enum_field(2)


@dataclass
class BroadcastTxResponse(betterproto.Message):
    """
    BroadcastTxResponse is the response type for the Service.BroadcastTx
    method.
    """

    # tx_response is the queried TxResponses.
    tx_response: v1beta1.TxResponse = betterproto.message_field(1)


@dataclass
class SimulateRequest(betterproto.Message):
    """
    SimulateRequest is the request type for the Service.Simulate RPC method.
    """

    # tx is the transaction to simulate. Deprecated. Send raw tx bytes instead.
    tx: "Tx" = betterproto.message_field(1)
    # tx_bytes is the raw transaction. Since: cosmos-sdk 0.43
    tx_bytes: bytes = betterproto.bytes_field(2)


@dataclass
class SimulateResponse(betterproto.Message):
    """
    SimulateResponse is the response type for the Service.SimulateRPC method.
    """

    # gas_info is the information about gas used in the simulation.
    gas_info: v1beta1.GasInfo = betterproto.message_field(1)
    # result is the result of the simulation.
    result: v1beta1.Result = betterproto.message_field(2)


@dataclass
class GetTxRequest(betterproto.Message):
    """GetTxRequest is the request type for the Service.GetTx RPC method."""

    # hash is the tx hash to query, encoded as a hex string.
    hash: str = betterproto.string_field(1)


@dataclass
class GetTxResponse(betterproto.Message):
    """GetTxResponse is the response type for the Service.GetTx method."""

    # tx is the queried transaction.
    tx: "Tx" = betterproto.message_field(1)
    # tx_response is the queried TxResponses.
    tx_response: v1beta1.TxResponse = betterproto.message_field(2)


@dataclass
class GetBlockWithTxsRequest(betterproto.Message):
    """
    GetBlockWithTxsRequest is the request type for the Service.GetBlockWithTxs
    RPC method. Since: cosmos-sdk 0.45.2
    """

    # height is the height of the block to query.
    height: int = betterproto.int64_field(1)
    # pagination defines a pagination for the request.
    pagination: v1beta1.PageRequest = betterproto.message_field(2)


@dataclass
class GetBlockWithTxsResponse(betterproto.Message):
    """
    GetBlockWithTxsResponse is the response type for the
    Service.GetBlockWithTxs method. Since: cosmos-sdk 0.45.2
    """

    # txs are the transactions in the block.
    txs: List["Tx"] = betterproto.message_field(1)
    block_id: types.BlockID = betterproto.message_field(2)
    block: types.Block = betterproto.message_field(3)
    # pagination defines a pagination for the response.
    pagination: v1beta1.PageResponse = betterproto.message_field(4)


@dataclass
class TxDecodeRequest(betterproto.Message):
    """
    TxDecodeRequest is the request type for the Service.TxDecode RPC method.
    Since: cosmos-sdk 0.47
    """

    # tx_bytes is the raw transaction.
    tx_bytes: bytes = betterproto.bytes_field(1)


@dataclass
class TxDecodeResponse(betterproto.Message):
    """
    TxDecodeResponse is the response type for the Service.TxDecode method.
    Since: cosmos-sdk 0.47
    """

    # tx is the decoded transaction.
    tx: "Tx" = betterproto.message_field(1)


@dataclass
class TxEncodeRequest(betterproto.Message):
    """
    TxEncodeRequest is the request type for the Service.TxEncode RPC method.
    Since: cosmos-sdk 0.47
    """

    # tx is the transaction to encode.
    tx: "Tx" = betterproto.message_field(1)


@dataclass
class TxEncodeResponse(betterproto.Message):
    """
    TxEncodeResponse is the response type for the Service.TxEncode method.
    Since: cosmos-sdk 0.47
    """

    # tx_bytes is the encoded transaction bytes.
    tx_bytes: bytes = betterproto.bytes_field(1)


@dataclass
class TxEncodeAminoRequest(betterproto.Message):
    """
    TxEncodeAminoRequest is the request type for the Service.TxEncodeAmino RPC
    method. Since: cosmos-sdk 0.47
    """

    amino_json: str = betterproto.string_field(1)


@dataclass
class TxEncodeAminoResponse(betterproto.Message):
    """
    TxEncodeAminoResponse is the response type for the Service.TxEncodeAmino
    RPC method. Since: cosmos-sdk 0.47
    """

    amino_binary: bytes = betterproto.bytes_field(1)


@dataclass
class TxDecodeAminoRequest(betterproto.Message):
    """
    TxDecodeAminoRequest is the request type for the Service.TxDecodeAmino RPC
    method. Since: cosmos-sdk 0.47
    """

    amino_binary: bytes = betterproto.bytes_field(1)


@dataclass
class TxDecodeAminoResponse(betterproto.Message):
    """
    TxDecodeAminoResponse is the response type for the Service.TxDecodeAmino
    RPC method. Since: cosmos-sdk 0.47
    """

    amino_json: str = betterproto.string_field(1)


class ServiceStub(betterproto.ServiceStub):
    """Service defines a gRPC service for interacting with transactions."""

    async def simulate(
        self, *, tx: Optional["Tx"] = None, tx_bytes: bytes = b""
    ) -> SimulateResponse:
        """
        Simulate simulates executing a transaction for estimating gas usage.
        """

        request = SimulateRequest()
        if tx is not None:
            request.tx = tx
        request.tx_bytes = tx_bytes

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/Simulate",
            request,
            SimulateResponse,
        )

    async def get_tx(self, *, hash: str = "") -> GetTxResponse:
        """GetTx fetches a tx by hash."""

        request = GetTxRequest()
        request.hash = hash

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/GetTx",
            request,
            GetTxResponse,
        )

    async def broadcast_tx(
        self, *, tx_bytes: bytes = b"", mode: "BroadcastMode" = 0
    ) -> BroadcastTxResponse:
        """BroadcastTx broadcast transaction."""

        request = BroadcastTxRequest()
        request.tx_bytes = tx_bytes
        request.mode = mode

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/BroadcastTx",
            request,
            BroadcastTxResponse,
        )

    async def get_txs_event(
        self,
        *,
        events: List[str] = [],
        pagination: Optional[v1beta1.PageRequest] = None,
        order_by: "OrderBy" = 0,
        page: int = 0,
        limit: int = 0,
        query: str = "",
    ) -> GetTxsEventResponse:
        """GetTxsEvent fetches txs by event."""

        request = GetTxsEventRequest()
        request.events = events
        if pagination is not None:
            request.pagination = pagination
        request.order_by = order_by
        request.page = page
        request.limit = limit
        request.query = query

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/GetTxsEvent",
            request,
            GetTxsEventResponse,
        )

    async def get_block_with_txs(
        self, *, height: int = 0, pagination: Optional[v1beta1.PageRequest] = None
    ) -> GetBlockWithTxsResponse:
        """
        GetBlockWithTxs fetches a block with decoded txs. Since: cosmos-sdk
        0.45.2
        """

        request = GetBlockWithTxsRequest()
        request.height = height
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/GetBlockWithTxs",
            request,
            GetBlockWithTxsResponse,
        )

    async def tx_decode(self, *, tx_bytes: bytes = b"") -> TxDecodeResponse:
        """TxDecode decodes the transaction. Since: cosmos-sdk 0.47"""

        request = TxDecodeRequest()
        request.tx_bytes = tx_bytes

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/TxDecode",
            request,
            TxDecodeResponse,
        )

    async def tx_encode(self, *, tx: Optional["Tx"] = None) -> TxEncodeResponse:
        """TxEncode encodes the transaction. Since: cosmos-sdk 0.47"""

        request = TxEncodeRequest()
        if tx is not None:
            request.tx = tx

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/TxEncode",
            request,
            TxEncodeResponse,
        )

    async def tx_encode_amino(self, *, amino_json: str = "") -> TxEncodeAminoResponse:
        """
        TxEncodeAmino encodes an Amino transaction from JSON to encoded bytes.
        Since: cosmos-sdk 0.47
        """

        request = TxEncodeAminoRequest()
        request.amino_json = amino_json

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/TxEncodeAmino",
            request,
            TxEncodeAminoResponse,
        )

    async def tx_decode_amino(
        self, *, amino_binary: bytes = b""
    ) -> TxDecodeAminoResponse:
        """
        TxDecodeAmino decodes an Amino transaction from encoded bytes to JSON.
        Since: cosmos-sdk 0.47
        """

        request = TxDecodeAminoRequest()
        request.amino_binary = amino_binary

        return await self._unary_unary(
            "/cosmos.tx.v1beta1.Service/TxDecodeAmino",
            request,
            TxDecodeAminoResponse,
        )
