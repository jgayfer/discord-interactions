# Normal libraries
from enum import IntEnum


class DefaultErrorType(IntEnum):
    """
    An enumerable object for the default errors that occur with interaction creation.

    ..note::
        This is a port from v3's errors, which basically delegate errors to a unique error code.
        This enum's purpose is to help remember error codes. Importing this class is not required.
        i.e.:
            raise InteractionException(1) == raise InteractionException(REQUEST_FAILURE)
    """

    BASE = 0
    REQUEST_FAILURE = 1
    INCORRECT_FORMAT = 2
    DUPLICATE_COMMAND = 3
    DUPLICATE_CALLBACK = 4
    DUPLICATE_SLASH_CLIENT = 5
    CHECK_FAILURE = 6
    INCORRECT_TYPE = 7
    INCORRECT_GUILD_ID_TYPE = 8
    INCORRECT_COMMAND_DATA = 9
    ALREADY_RESPONDED = 10


class OpCodeType(IntEnum):
    """
    An enumerable object for the Gateway's OPCODE result state.
    This is representative of the OPCodes generated by the WebSocket.

    .. note::
        Equivalent of `Gateway Opcodes <https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway-opcodes>`_ in the Discord API.
    """

    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE = 3
    VOICE_STATE = 4
    VOICE_PING = 5
    RESUME = 6
    RECONNECT = 7
    REQUEST_MEMBERS = 8
    INVALIDATE_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11
    GUILD_SYNC = 12


class WSCloseCodeType(IntEnum):
    """
    An enumerable object for the Gateway's closing connection codes.
    This is representative of the Gateway responses generated by the WebSocket.

    .. note::
        Equivalent of `Gateway Close Event Codes <https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway-gateway-close-event-codes>`_ in the Discord API.
    """

    UNKNOWN_ERROR = 4000
    UNKNOWN_OPCODE = 4001
    DECODE_ERROR = 4002
    NOT_AUTHENTICATED = 4003
    AUTHENTICATION_FAILED = 4004
    ALREADY_AUTHENTICATED = 4005
    INVALID_SEQ = 4007
    RATE_LIMITED = 4008
    SESSION_TIMED_OUT = 4009
    INVALID_SHARD = 4010
    SHARDING_REQUIRED = 4011
    INVALID_API_VERSION = 4012
    INVALID_INTENTS = 4013
    DISALLOWED_INTENTS = 4014


class HTTPResponseType(IntEnum):
    """
    An enumerable object for the HTTP response codes Discord gives out.

    ..note::
        This enumerable does not list the documented "5xx", as it may vary.
    """

    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_MODIFIED = 304
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    TOO_MANY_REQUESTS = 429
    GATEWAY_UNAVAILABLE = 502
