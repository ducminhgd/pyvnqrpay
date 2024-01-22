from enum import Enum, IntEnum


class GUID(Enum, str):
    VNPAY = 'A000000775'
    VIETQR = 'A000000727'


class Field(Enum, str):
    GUID = '00'
    DATA = '01'
    SERVICE = '02'


class VietQRConsumerID(Enum, str):
    BANK_BIN = '00'
    BANK_NUMBER = '01'


class VietQRStatus(IntEnum):
    NOT_SUPPORTED = 0
    RECEIVE_ONLY = 1
    SUPPORTED = 2


class VietQRService(Enum, str):
    FAST_TRANSFER_BY_ACCOUNT_NUMBER = 'QRIBFTTA'
    FAST_TRANSFER_BY_CARD_NUMBER = 'QRIBFTTC'
