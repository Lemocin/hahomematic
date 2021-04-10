"""
Constants used by hahomematic.
"""

VERSION = '0.0.2'

LOCALHOST = 'localhost'
IP_LOCALHOST_V4 = '127.0.0.1'
IP_LOCALHOST_V6 = '::1'
IP_ANY_V4 = '0.0.0.0'
IP_ANY_V6 = '::'
PORT_ANY = 0

PORT_REGAHSS = 1999
PORT_REGAHSS_TLS = 41999
PORT_HS485D = 2000
PORT_HS485D_TLS = 42000
PORT_RFD = 2001
PORT_RFD_TLS = 42001
PORT_HMIP = 2010
PORT_HMIP_TLS = 42010
PORT_GROUPS = 9292
PORT_GROUPS_TLS = 49292
PORT_JSONRPC = 80
PORT_JSONRPC_TLS = 443
PORT_REGA_SCRIPT = 8181
PORT_REGA_SCRIPT_TLS = 48181

JSONRPC_PATH = '/api/homematic.cgi'
PATH_JSON_RPC = '/api/homematic.cgi'
PATH_TCL_REGA = '/tclrega.exe'

FILE_DEVICES = None
FILE_DEVICES_RAW = None
FILE_PARAMSETS = None

RELEVANT_PARAMSETS = [
    'VALUES',
    #'MASTER',
]

HH_EVENT_DELETE_DEVICES = 'deleteDevices'
HH_EVENT_DEVICES_CREATED = 'devicesCreated'
HH_EVENT_ENTITIES_CREATED = 'entitiesCreated'
HH_EVENT_ENTITY_CREATED = 'entitiyCreated'
HH_EVENT_ERROR = 'error'
HH_EVENT_LIST_DEVICES = 'listDevices'
HH_EVENT_NEW_DEVICES = 'newDevices'
HH_EVENT_READDED_DEVICE = 'readdedDevice'
HH_EVENT_REPLACE_DEVICE = 'replaceDevice'
HH_EVENT_UPDATE_DEVICE = 'updateDevice'

# When CONFIG_PENDING turns from True to False (ONLY then!) we should refetch the paramsets.
# However, usually multiple of these events are fired, so we should only
# act on the last one. This also only seems to fire on channel 0.
EVENT_CONFIG_PENDING = 'CONFIG_PENDING'
EVENT_ERROR = 'ERROR'
# Only available on CCU
EVENT_PONG = 'PONG'
EVENT_PRESS = 'PRESS'
EVENT_PRESS_SHORT = 'PRESS_SHORT'
EVENT_PRESS_LONG = 'PRESS_LONG'
EVENT_PRESS_CONT = 'PRESS_CONT'
EVENT_PRESS_LONG_RELEASE = 'PRESS_LONG_RELEASE'
EVENT_UNREACH = 'UNREACH'
EVENT_SEQUENCE_OK = 'SEQUENCE_OK'
EVENT_STICKY_UNREACH = 'STICKY_UNREACH'

EVENTS_FORWARD = [
    EVENT_CONFIG_PENDING,
    EVENT_ERROR,
    EVENT_PRESS,
    EVENT_PRESS_SHORT,
    EVENT_PRESS_LONG,
    EVENT_PRESS_CONT,
    EVENT_PRESS_LONG_RELEASE,
    EVENT_UNREACH,
    EVENT_SEQUENCE_OK,
    EVENT_STICKY_UNREACH,
]

# Parameters within the paramsets for which we don't create entities.
IGNORED_PARAMETERS = [
    'DEVICE_IN_BOOTLOADER',
    'INSTALL_TEST',
    'STICKY_UNREACH'
]

BACKEND_UNKNOWN = 0
BACKEND_CCU = 1
BACKEND_HOMEGEAR = 2

PROXY_INIT_FAILED = 0
PROXY_INIT_SUCCESS = 1
PROXY_INIT_SKIPPED = 2

INTERFACE_ID = 'hahomematic'

ATTR_ADDRESS = 'address'
ATTR_CALLBACK_IP = 'callbackip'
ATTR_CALLBACK_PORT = 'callbackport'
ATTR_CHANNELS = 'channels'
ATTR_CONNECT = 'connect'
ATTR_ERROR = 'error'
ATTR_HOSTNAME = 'hostname'
ATTR_ID = 'id'
ATTR_INTERFACE = 'interface'
ATTR_IP = 'ip'
ATTR_JSON = 'json'
ATTR_JSONPORT = 'jsonport'
ATTR_METADATA = 'metadata'
ATTR_NAME = 'name'
ATTR_PASSWORD = 'password'
ATTR_PATH = 'path'
ATTR_PORT = 'port'
ATTR_RESOLVENAMES = 'resolvenames'
ATTR_RESULT = 'result'
ATTR_SESSION_ID = '_session_id_'
ATTR_SSL = 'ssl'
ATTR_TYPE = 'type'
ATTR_USERNAME = 'username'
ATTR_VALUE = 'value'
ATTR_VERIFY_SSL = 'verify_ssl'

ATTR_HM_ADDRESS = 'ADDRESS'
ATTR_HM_CONTROL = 'CONTROL'
ATTR_HM_OPERATIONS = 'OPERATIONS'
ATTR_HM_PARAMSETS = 'PARAMSETS'
ATTR_HM_TYPE = 'TYPE'
ATTR_HM_PARENT_TYPE = 'PARENT_TYPE'
ATTR_HM_VERSION = 'VERSION'
ATTR_HM_LIST = 'LIST'
ATTR_HM_LOGIC = 'LOGIC'
ATTR_HM_NAME = 'NAME'
ATTR_HM_NUMBER = 'NUMBER'
ATTR_HM_FLAGS = 'FLAGS'
ATTR_HM_UNIT = 'UNIT'
ATTR_HM_MAX = 'MAX'
ATTR_HM_MIN = 'MIN'
ATTR_HM_DEFAULT = 'DEFAULT'
# Optional member for TYPE: FLOAT, INTEGER
ATTR_HM_SPECIAL = 'SPECIAL' # Which has the following keys
ATTR_HM_ID = 'ID' # String
ATTR_HM_VALUE = 'VALUE' # Float or integer, depending on TYPE
# Members for ENUM
ATTR_HM_VALUE_LIST = 'VALUE_LIST'

OPERATION_NONE = 0
OPERATION_READ = 1
OPERATION_WRITE = 2
OPERATION_EVENT = 4

TYPE_FLOAT = 'FLOAT'
TYPE_INTEGER = 'INTEGER'
TYPE_BOOL = 'BOOL'
TYPE_ENUM = 'ENUM'
TYPE_STRING = 'STRING'
TYPE_ACTION = 'ACTION' # Usually buttons, send Boolean to trigger

FLAG_VISIBLE = 1
FLAG_INTERAL = 2
FLAG_TRANSFORM = 4
FLAG_SERVICE = 8
FLAG_STICKY = 10 # This might be wrong. Documentation says 0x10

DEFAULT_ADMIN = 'Admin'
DEFAULT_CALLBACK_HOSTNAME = None
DEFAULT_CALLBACK_PORT = None
DEFAULT_CONNECT = True
DEFAULT_INTERFACE_ID = 'hahomematic'
DEFAULT_JSONPORT = 80
DEFAULT_LOCAL_PORT = None
DEFAULT_LOCAL_SERVER = None
DEFAULT_NAME = 'default'
DEFAULT_PASSWORD = None
DEFAULT_PATH = None
DEFAULT_USER = 'Admin'
DEFAULT_REMOTE = 'default'
DEFAULT_RESOLVENAMES = False
DEFAULT_SSL = False
DEFAULT_TIMEOUT = 5
DEFAULT_INIT_TIMEOUT = 90
DEFAULT_TLS = False
DEFAULT_VERIFY_SSL = False
DEFAULT_VERIFY_TLS = False

DEFAULT_REMOTES = {
    DEFAULT_REMOTE: {
        ATTR_HOSTNAME: IP_LOCALHOST_V4,
        ATTR_PORT: PORT_RFD,
        ATTR_PATH: DEFAULT_PATH,
        ATTR_USERNAME: DEFAULT_ADMIN,
        ATTR_PASSWORD: DEFAULT_PASSWORD,
        ATTR_JSONPORT: DEFAULT_JSONPORT,
        ATTR_RESOLVENAMES: DEFAULT_RESOLVENAMES,
        ATTR_CONNECT: DEFAULT_CONNECT,
}}
