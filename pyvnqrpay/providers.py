from enum import Enum, IntEnum


class VietQRProvider(str, Enum):
    FIELD_ID = '38'
    GUID = 'A000000727'
    NAME = 'VIETQR'


class VNPayProvider(str, Enum):
    FIELD_ID = '26'
    GUID = 'A000000775'
    NAME = 'VNPAY'


class Field(str, Enum):
    GUID = '00'
    DATA = '01'
    SERVICE = '02'


class VietQRConsumerID(str, Enum):
    BANK_BIN = '00'
    BANK_NUMBER = '01'


class VietQRStatus(IntEnum):
    NOT_SUPPORTED = 0
    RECEIVE_ONLY = 1
    SUPPORTED = 2


class VietQRService(str, Enum):
    FAST_TRANSFER_BY_ACCOUNT_NUMBER = 'QRIBFTTA'
    FAST_TRANSFER_BY_CARD_NUMBER = 'QRIBFTTC'
