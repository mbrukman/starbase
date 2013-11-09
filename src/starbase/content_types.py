__title__ = 'starbase.content_types'
__version__ = '0.2.4'
__build__ = 0x000002
__author__ = 'Artur Barseghyan'

CONTENT_TYPE_JSON = 'json'
MEDIA_TYPE_JSON = 'application/json'
#CONTENT_TYPE_XML = 'xml'
#MEDIA_TYPE_XML = 'text/xml'
#CONTENT_TYPE_PROTOBUF = 'protobuf'
#MEDIA_TYPE_PROTOBUF = 'application/x-protobuf'
DEFAULT_CONTENT_TYPE = CONTENT_TYPE_JSON

CONTENT_TYPES_DICT = {
    CONTENT_TYPE_JSON: MEDIA_TYPE_JSON,
    #CONTENT_TYPE_XML: CONTENT_TYPE_XML,
    #CONTENT_TYPE_PROTOBUF: MEDIA_TYPE_PROTOBUF
}

CONTENT_TYPES = (
    CONTENT_TYPE_JSON,
    #CONTENT_TYPE_XML,
    #CONTENT_TYPE_PROTOBUF
)

DEFAULT_CONTENT_TYPE = CONTENT_TYPE_JSON
