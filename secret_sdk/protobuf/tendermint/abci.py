# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/abci/types.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

import betterproto
import grpclib

from .tendermint import crypto
from .tendermint import types


class CheckTxType(betterproto.Enum):
    NEW = 0
    RECHECK = 1


class MisbehaviorType(betterproto.Enum):
    UNKNOWN = 0
    DUPLICATE_VOTE = 1
    LIGHT_CLIENT_ATTACK = 2


class ResponseOfferSnapshotResult(betterproto.Enum):
    UNKNOWN = 0
    ACCEPT = 1
    ABORT = 2
    REJECT = 3
    REJECT_FORMAT = 4
    REJECT_SENDER = 5


class ResponseApplySnapshotChunkResult(betterproto.Enum):
    UNKNOWN = 0
    ACCEPT = 1
    ABORT = 2
    RETRY = 3
    RETRY_SNAPSHOT = 4
    REJECT_SNAPSHOT = 5


class ResponseProcessProposalProposalStatus(betterproto.Enum):
    UNKNOWN = 0
    ACCEPT = 1
    REJECT = 2


class ResponseVerifyVoteExtensionVerifyStatus(betterproto.Enum):
    UNKNOWN = 0
    ACCEPT = 1
    REJECT = 2


@dataclass
class Request(betterproto.Message):
    echo: "RequestEcho" = betterproto.message_field(1, group="value")
    flush: "RequestFlush" = betterproto.message_field(2, group="value")
    info: "RequestInfo" = betterproto.message_field(3, group="value")
    init_chain: "RequestInitChain" = betterproto.message_field(5, group="value")
    query: "RequestQuery" = betterproto.message_field(6, group="value")
    check_tx: "RequestCheckTx" = betterproto.message_field(8, group="value")
    commit: "RequestCommit" = betterproto.message_field(11, group="value")
    list_snapshots: "RequestListSnapshots" = betterproto.message_field(
        12, group="value"
    )
    offer_snapshot: "RequestOfferSnapshot" = betterproto.message_field(
        13, group="value"
    )
    load_snapshot_chunk: "RequestLoadSnapshotChunk" = betterproto.message_field(
        14, group="value"
    )
    apply_snapshot_chunk: "RequestApplySnapshotChunk" = betterproto.message_field(
        15, group="value"
    )
    prepare_proposal: "RequestPrepareProposal" = betterproto.message_field(
        16, group="value"
    )
    process_proposal: "RequestProcessProposal" = betterproto.message_field(
        17, group="value"
    )
    extend_vote: "RequestExtendVote" = betterproto.message_field(18, group="value")
    verify_vote_extension: "RequestVerifyVoteExtension" = betterproto.message_field(
        19, group="value"
    )
    finalize_block: "RequestFinalizeBlock" = betterproto.message_field(
        20, group="value"
    )


@dataclass
class RequestEcho(betterproto.Message):
    message: str = betterproto.string_field(1)


@dataclass
class RequestFlush(betterproto.Message):
    pass


@dataclass
class RequestInfo(betterproto.Message):
    version: str = betterproto.string_field(1)
    block_version: int = betterproto.uint64_field(2)
    p2p_version: int = betterproto.uint64_field(3)
    abci_version: str = betterproto.string_field(4)


@dataclass
class RequestInitChain(betterproto.Message):
    time: datetime = betterproto.message_field(1)
    chain_id: str = betterproto.string_field(2)
    consensus_params: types.ConsensusParams = betterproto.message_field(3)
    validators: List["ValidatorUpdate"] = betterproto.message_field(4)
    app_state_bytes: bytes = betterproto.bytes_field(5)
    initial_height: int = betterproto.int64_field(6)


@dataclass
class RequestQuery(betterproto.Message):
    data: bytes = betterproto.bytes_field(1)
    path: str = betterproto.string_field(2)
    height: int = betterproto.int64_field(3)
    prove: bool = betterproto.bool_field(4)


@dataclass
class RequestCheckTx(betterproto.Message):
    tx: bytes = betterproto.bytes_field(1)
    type: "CheckTxType" = betterproto.enum_field(2)


@dataclass
class RequestCommit(betterproto.Message):
    pass


@dataclass
class RequestListSnapshots(betterproto.Message):
    """lists available snapshots"""

    pass


@dataclass
class RequestOfferSnapshot(betterproto.Message):
    """offers a snapshot to the application"""

    snapshot: "Snapshot" = betterproto.message_field(1)
    app_hash: bytes = betterproto.bytes_field(2)


@dataclass
class RequestLoadSnapshotChunk(betterproto.Message):
    """loads a snapshot chunk"""

    height: int = betterproto.uint64_field(1)
    format: int = betterproto.uint32_field(2)
    chunk: int = betterproto.uint32_field(3)


@dataclass
class RequestApplySnapshotChunk(betterproto.Message):
    """Applies a snapshot chunk"""

    index: int = betterproto.uint32_field(1)
    chunk: bytes = betterproto.bytes_field(2)
    sender: str = betterproto.string_field(3)


@dataclass
class RequestPrepareProposal(betterproto.Message):
    # the modified transactions cannot exceed this size.
    max_tx_bytes: int = betterproto.int64_field(1)
    # txs is an array of transactions that will be included in a block, sent to
    # the app for possible modifications.
    txs: List[bytes] = betterproto.bytes_field(2)
    local_last_commit: "ExtendedCommitInfo" = betterproto.message_field(3)
    misbehavior: List["Misbehavior"] = betterproto.message_field(4)
    height: int = betterproto.int64_field(5)
    time: datetime = betterproto.message_field(6)
    next_validators_hash: bytes = betterproto.bytes_field(7)
    # address of the public key of the validator proposing the block.
    proposer_address: bytes = betterproto.bytes_field(8)


@dataclass
class RequestProcessProposal(betterproto.Message):
    txs: List[bytes] = betterproto.bytes_field(1)
    proposed_last_commit: "CommitInfo" = betterproto.message_field(2)
    misbehavior: List["Misbehavior"] = betterproto.message_field(3)
    # hash is the merkle root hash of the fields of the proposed block.
    hash: bytes = betterproto.bytes_field(4)
    height: int = betterproto.int64_field(5)
    time: datetime = betterproto.message_field(6)
    next_validators_hash: bytes = betterproto.bytes_field(7)
    # address of the public key of the original proposer of the block.
    proposer_address: bytes = betterproto.bytes_field(8)


@dataclass
class RequestExtendVote(betterproto.Message):
    """Extends a vote with application-injected data"""

    # the hash of the block that this vote may be referring to
    hash: bytes = betterproto.bytes_field(1)
    # the height of the extended vote
    height: int = betterproto.int64_field(2)
    # info of the block that this vote may be referring to
    time: datetime = betterproto.message_field(3)
    txs: List[bytes] = betterproto.bytes_field(4)
    proposed_last_commit: "CommitInfo" = betterproto.message_field(5)
    misbehavior: List["Misbehavior"] = betterproto.message_field(6)
    next_validators_hash: bytes = betterproto.bytes_field(7)
    # address of the public key of the original proposer of the block.
    proposer_address: bytes = betterproto.bytes_field(8)


@dataclass
class RequestVerifyVoteExtension(betterproto.Message):
    """Verify the vote extension"""

    # the hash of the block that this received vote corresponds to
    hash: bytes = betterproto.bytes_field(1)
    # the validator that signed the vote extension
    validator_address: bytes = betterproto.bytes_field(2)
    height: int = betterproto.int64_field(3)
    vote_extension: bytes = betterproto.bytes_field(4)


@dataclass
class RequestFinalizeBlock(betterproto.Message):
    txs: List[bytes] = betterproto.bytes_field(1)
    decided_last_commit: "CommitInfo" = betterproto.message_field(2)
    misbehavior: List["Misbehavior"] = betterproto.message_field(3)
    # hash is the merkle root hash of the fields of the decided block.
    hash: bytes = betterproto.bytes_field(4)
    height: int = betterproto.int64_field(5)
    time: datetime = betterproto.message_field(6)
    next_validators_hash: bytes = betterproto.bytes_field(7)
    # proposer_address is the address of the public key of the original proposer
    # of the block.
    proposer_address: bytes = betterproto.bytes_field(8)
    encrypted_random: types.EncryptedRandom = betterproto.message_field(9)
    commit: types.Commit = betterproto.message_field(10)


@dataclass
class Response(betterproto.Message):
    exception: "ResponseException" = betterproto.message_field(1, group="value")
    echo: "ResponseEcho" = betterproto.message_field(2, group="value")
    flush: "ResponseFlush" = betterproto.message_field(3, group="value")
    info: "ResponseInfo" = betterproto.message_field(4, group="value")
    init_chain: "ResponseInitChain" = betterproto.message_field(6, group="value")
    query: "ResponseQuery" = betterproto.message_field(7, group="value")
    check_tx: "ResponseCheckTx" = betterproto.message_field(9, group="value")
    commit: "ResponseCommit" = betterproto.message_field(12, group="value")
    list_snapshots: "ResponseListSnapshots" = betterproto.message_field(
        13, group="value"
    )
    offer_snapshot: "ResponseOfferSnapshot" = betterproto.message_field(
        14, group="value"
    )
    load_snapshot_chunk: "ResponseLoadSnapshotChunk" = betterproto.message_field(
        15, group="value"
    )
    apply_snapshot_chunk: "ResponseApplySnapshotChunk" = betterproto.message_field(
        16, group="value"
    )
    prepare_proposal: "ResponsePrepareProposal" = betterproto.message_field(
        17, group="value"
    )
    process_proposal: "ResponseProcessProposal" = betterproto.message_field(
        18, group="value"
    )
    extend_vote: "ResponseExtendVote" = betterproto.message_field(19, group="value")
    verify_vote_extension: "ResponseVerifyVoteExtension" = betterproto.message_field(
        20, group="value"
    )
    finalize_block: "ResponseFinalizeBlock" = betterproto.message_field(
        21, group="value"
    )


@dataclass
class ResponseException(betterproto.Message):
    """nondeterministic"""

    error: str = betterproto.string_field(1)


@dataclass
class ResponseEcho(betterproto.Message):
    message: str = betterproto.string_field(1)


@dataclass
class ResponseFlush(betterproto.Message):
    pass


@dataclass
class ResponseInfo(betterproto.Message):
    data: str = betterproto.string_field(1)
    version: str = betterproto.string_field(2)
    app_version: int = betterproto.uint64_field(3)
    last_block_height: int = betterproto.int64_field(4)
    last_block_app_hash: bytes = betterproto.bytes_field(5)


@dataclass
class ResponseInitChain(betterproto.Message):
    consensus_params: types.ConsensusParams = betterproto.message_field(1)
    validators: List["ValidatorUpdate"] = betterproto.message_field(2)
    app_hash: bytes = betterproto.bytes_field(3)


@dataclass
class ResponseQuery(betterproto.Message):
    code: int = betterproto.uint32_field(1)
    # bytes data = 2; // use "value" instead.
    log: str = betterproto.string_field(3)
    info: str = betterproto.string_field(4)
    index: int = betterproto.int64_field(5)
    key: bytes = betterproto.bytes_field(6)
    value: bytes = betterproto.bytes_field(7)
    proof_ops: crypto.ProofOps = betterproto.message_field(8)
    height: int = betterproto.int64_field(9)
    codespace: str = betterproto.string_field(10)


@dataclass
class ResponseCheckTx(betterproto.Message):
    code: int = betterproto.uint32_field(1)
    data: bytes = betterproto.bytes_field(2)
    log: str = betterproto.string_field(3)
    info: str = betterproto.string_field(4)
    gas_wanted: int = betterproto.int64_field(5)
    gas_used: int = betterproto.int64_field(6)
    events: List["Event"] = betterproto.message_field(7)
    codespace: str = betterproto.string_field(8)


@dataclass
class ResponseCommit(betterproto.Message):
    retain_height: int = betterproto.int64_field(3)


@dataclass
class ResponseListSnapshots(betterproto.Message):
    snapshots: List["Snapshot"] = betterproto.message_field(1)


@dataclass
class ResponseOfferSnapshot(betterproto.Message):
    result: "ResponseOfferSnapshotResult" = betterproto.enum_field(1)


@dataclass
class ResponseLoadSnapshotChunk(betterproto.Message):
    chunk: bytes = betterproto.bytes_field(1)


@dataclass
class ResponseApplySnapshotChunk(betterproto.Message):
    result: "ResponseApplySnapshotChunkResult" = betterproto.enum_field(1)
    refetch_chunks: List[int] = betterproto.uint32_field(2)
    reject_senders: List[str] = betterproto.string_field(3)


@dataclass
class ResponsePrepareProposal(betterproto.Message):
    txs: List[bytes] = betterproto.bytes_field(1)


@dataclass
class ResponseProcessProposal(betterproto.Message):
    status: "ResponseProcessProposalProposalStatus" = betterproto.enum_field(1)


@dataclass
class ResponseExtendVote(betterproto.Message):
    vote_extension: bytes = betterproto.bytes_field(1)


@dataclass
class ResponseVerifyVoteExtension(betterproto.Message):
    status: "ResponseVerifyVoteExtensionVerifyStatus" = betterproto.enum_field(1)


@dataclass
class ResponseFinalizeBlock(betterproto.Message):
    # set of block events emmitted as part of executing the block
    events: List["Event"] = betterproto.message_field(1)
    # the result of executing each transaction including the events the
    # particular transction emitted. This should match the order of the
    # transactions delivered in the block itself
    tx_results: List["ExecTxResult"] = betterproto.message_field(2)
    # a list of updates to the validator set. These will reflect the validator
    # set at current height + 2.
    validator_updates: List["ValidatorUpdate"] = betterproto.message_field(3)
    # updates to the consensus params, if any.
    consensus_param_updates: types.ConsensusParams = betterproto.message_field(4)
    # app_hash is the hash of the applications' state which is used to confirm
    # that execution of the transactions was deterministic. It is up to the
    # application to decide which algorithm to use.
    app_hash: bytes = betterproto.bytes_field(5)


@dataclass
class CommitInfo(betterproto.Message):
    round: int = betterproto.int32_field(1)
    votes: List["VoteInfo"] = betterproto.message_field(2)


@dataclass
class ExtendedCommitInfo(betterproto.Message):
    """
    ExtendedCommitInfo is similar to CommitInfo except that it is only used in
    the PrepareProposal request such that CometBFT can provide vote extensions
    to the application.
    """

    # The round at which the block proposer decided in the previous height.
    round: int = betterproto.int32_field(1)
    # List of validators' addresses in the last validator set with their voting
    # information, including vote extensions.
    votes: List["ExtendedVoteInfo"] = betterproto.message_field(2)


@dataclass
class Event(betterproto.Message):
    """
    Event allows application developers to attach additional information to
    ResponseFinalizeBlock and ResponseCheckTx. Later, transactions may be
    queried using these events.
    """

    type: str = betterproto.string_field(1)
    attributes: List["EventAttribute"] = betterproto.message_field(2)


@dataclass
class EventAttribute(betterproto.Message):
    """EventAttribute is a single key-value pair, associated with an event."""

    key: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)
    index: bool = betterproto.bool_field(3)


@dataclass
class ExecTxResult(betterproto.Message):
    """
    ExecTxResult contains results of executing one individual transaction. *
    Its structure is equivalent to #ResponseDeliverTx which will be
    deprecated/deleted
    """

    code: int = betterproto.uint32_field(1)
    data: bytes = betterproto.bytes_field(2)
    log: str = betterproto.string_field(3)
    info: str = betterproto.string_field(4)
    gas_wanted: int = betterproto.int64_field(5)
    gas_used: int = betterproto.int64_field(6)
    events: List["Event"] = betterproto.message_field(7)
    codespace: str = betterproto.string_field(8)


@dataclass
class TxResult(betterproto.Message):
    """
    TxResult contains results of executing the transaction. One usage is
    indexing transaction results.
    """

    height: int = betterproto.int64_field(1)
    index: int = betterproto.uint32_field(2)
    tx: bytes = betterproto.bytes_field(3)
    result: "ExecTxResult" = betterproto.message_field(4)


@dataclass
class Validator(betterproto.Message):
    address: bytes = betterproto.bytes_field(1)
    # PubKey pub_key = 2 [(gogoproto.nullable)=false];
    power: int = betterproto.int64_field(3)


@dataclass
class ValidatorUpdate(betterproto.Message):
    pub_key: crypto.PublicKey = betterproto.message_field(1)
    power: int = betterproto.int64_field(2)


@dataclass
class VoteInfo(betterproto.Message):
    validator: "Validator" = betterproto.message_field(1)
    block_id_flag: types.BlockIDFlag = betterproto.enum_field(3)


@dataclass
class ExtendedVoteInfo(betterproto.Message):
    # The validator that sent the vote.
    validator: "Validator" = betterproto.message_field(1)
    # Non-deterministic extension provided by the sending validator's
    # application.
    vote_extension: bytes = betterproto.bytes_field(3)
    # Vote extension signature created by CometBFT
    extension_signature: bytes = betterproto.bytes_field(4)
    # block_id_flag indicates whether the validator voted for a block, nil, or
    # did not vote at all
    block_id_flag: types.BlockIDFlag = betterproto.enum_field(5)


@dataclass
class Misbehavior(betterproto.Message):
    type: "MisbehaviorType" = betterproto.enum_field(1)
    # The offending validator
    validator: "Validator" = betterproto.message_field(2)
    # The height when the offense occurred
    height: int = betterproto.int64_field(3)
    # The corresponding time where the offense occurred
    time: datetime = betterproto.message_field(4)
    # Total voting power of the validator set in case the ABCI application does
    # not store historical validators.
    # https://github.com/tendermint/tendermint/issues/4581
    total_voting_power: int = betterproto.int64_field(5)


@dataclass
class Snapshot(betterproto.Message):
    height: int = betterproto.uint64_field(1)
    format: int = betterproto.uint32_field(2)
    chunks: int = betterproto.uint32_field(3)
    hash: bytes = betterproto.bytes_field(4)
    metadata: bytes = betterproto.bytes_field(5)


class ABCIStub(betterproto.ServiceStub):
    async def echo(self, *, message: str = "") -> ResponseEcho:
        request = RequestEcho()
        request.message = message

        return await self._unary_unary(
            "/tendermint.abci.ABCI/Echo",
            request,
            ResponseEcho,
        )

    async def flush(self) -> ResponseFlush:
        request = RequestFlush()

        return await self._unary_unary(
            "/tendermint.abci.ABCI/Flush",
            request,
            ResponseFlush,
        )

    async def info(
        self,
        *,
        version: str = "",
        block_version: int = 0,
        p2p_version: int = 0,
        abci_version: str = "",
    ) -> ResponseInfo:
        request = RequestInfo()
        request.version = version
        request.block_version = block_version
        request.p2p_version = p2p_version
        request.abci_version = abci_version

        return await self._unary_unary(
            "/tendermint.abci.ABCI/Info",
            request,
            ResponseInfo,
        )

    async def check_tx(
        self, *, tx: bytes = b"", type: "CheckTxType" = 0
    ) -> ResponseCheckTx:
        request = RequestCheckTx()
        request.tx = tx
        request.type = type

        return await self._unary_unary(
            "/tendermint.abci.ABCI/CheckTx",
            request,
            ResponseCheckTx,
        )

    async def query(
        self, *, data: bytes = b"", path: str = "", height: int = 0, prove: bool = False
    ) -> ResponseQuery:
        request = RequestQuery()
        request.data = data
        request.path = path
        request.height = height
        request.prove = prove

        return await self._unary_unary(
            "/tendermint.abci.ABCI/Query",
            request,
            ResponseQuery,
        )

    async def commit(self) -> ResponseCommit:
        request = RequestCommit()

        return await self._unary_unary(
            "/tendermint.abci.ABCI/Commit",
            request,
            ResponseCommit,
        )

    async def init_chain(
        self,
        *,
        time: Optional[datetime] = None,
        chain_id: str = "",
        consensus_params: Optional[types.ConsensusParams] = None,
        validators: List["ValidatorUpdate"] = [],
        app_state_bytes: bytes = b"",
        initial_height: int = 0,
    ) -> ResponseInitChain:
        request = RequestInitChain()
        if time is not None:
            request.time = time
        request.chain_id = chain_id
        if consensus_params is not None:
            request.consensus_params = consensus_params
        if validators is not None:
            request.validators = validators
        request.app_state_bytes = app_state_bytes
        request.initial_height = initial_height

        return await self._unary_unary(
            "/tendermint.abci.ABCI/InitChain",
            request,
            ResponseInitChain,
        )

    async def list_snapshots(self) -> ResponseListSnapshots:
        request = RequestListSnapshots()

        return await self._unary_unary(
            "/tendermint.abci.ABCI/ListSnapshots",
            request,
            ResponseListSnapshots,
        )

    async def offer_snapshot(
        self, *, snapshot: Optional["Snapshot"] = None, app_hash: bytes = b""
    ) -> ResponseOfferSnapshot:
        request = RequestOfferSnapshot()
        if snapshot is not None:
            request.snapshot = snapshot
        request.app_hash = app_hash

        return await self._unary_unary(
            "/tendermint.abci.ABCI/OfferSnapshot",
            request,
            ResponseOfferSnapshot,
        )

    async def load_snapshot_chunk(
        self, *, height: int = 0, format: int = 0, chunk: int = 0
    ) -> ResponseLoadSnapshotChunk:
        request = RequestLoadSnapshotChunk()
        request.height = height
        request.format = format
        request.chunk = chunk

        return await self._unary_unary(
            "/tendermint.abci.ABCI/LoadSnapshotChunk",
            request,
            ResponseLoadSnapshotChunk,
        )

    async def apply_snapshot_chunk(
        self, *, index: int = 0, chunk: bytes = b"", sender: str = ""
    ) -> ResponseApplySnapshotChunk:
        request = RequestApplySnapshotChunk()
        request.index = index
        request.chunk = chunk
        request.sender = sender

        return await self._unary_unary(
            "/tendermint.abci.ABCI/ApplySnapshotChunk",
            request,
            ResponseApplySnapshotChunk,
        )

    async def prepare_proposal(
        self,
        *,
        max_tx_bytes: int = 0,
        txs: List[bytes] = [],
        local_last_commit: Optional["ExtendedCommitInfo"] = None,
        misbehavior: List["Misbehavior"] = [],
        height: int = 0,
        time: Optional[datetime] = None,
        next_validators_hash: bytes = b"",
        proposer_address: bytes = b"",
    ) -> ResponsePrepareProposal:
        request = RequestPrepareProposal()
        request.max_tx_bytes = max_tx_bytes
        request.txs = txs
        if local_last_commit is not None:
            request.local_last_commit = local_last_commit
        if misbehavior is not None:
            request.misbehavior = misbehavior
        request.height = height
        if time is not None:
            request.time = time
        request.next_validators_hash = next_validators_hash
        request.proposer_address = proposer_address

        return await self._unary_unary(
            "/tendermint.abci.ABCI/PrepareProposal",
            request,
            ResponsePrepareProposal,
        )

    async def process_proposal(
        self,
        *,
        txs: List[bytes] = [],
        proposed_last_commit: Optional["CommitInfo"] = None,
        misbehavior: List["Misbehavior"] = [],
        hash: bytes = b"",
        height: int = 0,
        time: Optional[datetime] = None,
        next_validators_hash: bytes = b"",
        proposer_address: bytes = b"",
    ) -> ResponseProcessProposal:
        request = RequestProcessProposal()
        request.txs = txs
        if proposed_last_commit is not None:
            request.proposed_last_commit = proposed_last_commit
        if misbehavior is not None:
            request.misbehavior = misbehavior
        request.hash = hash
        request.height = height
        if time is not None:
            request.time = time
        request.next_validators_hash = next_validators_hash
        request.proposer_address = proposer_address

        return await self._unary_unary(
            "/tendermint.abci.ABCI/ProcessProposal",
            request,
            ResponseProcessProposal,
        )

    async def extend_vote(
        self,
        *,
        hash: bytes = b"",
        height: int = 0,
        time: Optional[datetime] = None,
        txs: List[bytes] = [],
        proposed_last_commit: Optional["CommitInfo"] = None,
        misbehavior: List["Misbehavior"] = [],
        next_validators_hash: bytes = b"",
        proposer_address: bytes = b"",
    ) -> ResponseExtendVote:
        request = RequestExtendVote()
        request.hash = hash
        request.height = height
        if time is not None:
            request.time = time
        request.txs = txs
        if proposed_last_commit is not None:
            request.proposed_last_commit = proposed_last_commit
        if misbehavior is not None:
            request.misbehavior = misbehavior
        request.next_validators_hash = next_validators_hash
        request.proposer_address = proposer_address

        return await self._unary_unary(
            "/tendermint.abci.ABCI/ExtendVote",
            request,
            ResponseExtendVote,
        )

    async def verify_vote_extension(
        self,
        *,
        hash: bytes = b"",
        validator_address: bytes = b"",
        height: int = 0,
        vote_extension: bytes = b"",
    ) -> ResponseVerifyVoteExtension:
        request = RequestVerifyVoteExtension()
        request.hash = hash
        request.validator_address = validator_address
        request.height = height
        request.vote_extension = vote_extension

        return await self._unary_unary(
            "/tendermint.abci.ABCI/VerifyVoteExtension",
            request,
            ResponseVerifyVoteExtension,
        )

    async def finalize_block(
        self,
        *,
        txs: List[bytes] = [],
        decided_last_commit: Optional["CommitInfo"] = None,
        misbehavior: List["Misbehavior"] = [],
        hash: bytes = b"",
        height: int = 0,
        time: Optional[datetime] = None,
        next_validators_hash: bytes = b"",
        proposer_address: bytes = b"",
        encrypted_random: Optional[types.EncryptedRandom] = None,
        commit: Optional[types.Commit] = None,
    ) -> ResponseFinalizeBlock:
        request = RequestFinalizeBlock()
        request.txs = txs
        if decided_last_commit is not None:
            request.decided_last_commit = decided_last_commit
        if misbehavior is not None:
            request.misbehavior = misbehavior
        request.hash = hash
        request.height = height
        if time is not None:
            request.time = time
        request.next_validators_hash = next_validators_hash
        request.proposer_address = proposer_address
        if encrypted_random is not None:
            request.encrypted_random = encrypted_random
        if commit is not None:
            request.commit = commit

        return await self._unary_unary(
            "/tendermint.abci.ABCI/FinalizeBlock",
            request,
            ResponseFinalizeBlock,
        )
