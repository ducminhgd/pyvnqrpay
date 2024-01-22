from enum import Enum


class FieldID(Enum, str):
    VERSION = '00'
    INIT_METHOD = '01'
    VNPAY_QR = '26'
    VIET_QR = '38'
    CATEGORY = '52'
    CURRENCY = '53'
    AMOUNT = '54'
    TIP_AND_FEE_TYPE = '55'
    TIP_AND_FEE_AMOUNT = '56'
    TIP_AND_FEE_PERCENT = '57'
    NATION = '58'
    MERCHANT_NAME = '59'
    CITY = '60'
    ZIP_CODE = '61'
    ADDITIONAL_DATA = '62'
    CRC = '63'


class AdditionalDataID(Enum, str):
    BILL_NUMBER = '01'
    MOBILE_NUMBER = '02'
    STORE_LABEL = '03'
    LOYALTY_NUMBER = '04'
    REFERENCE_LABEL = '05'
    CUSTOMER_LABEL = '06'
    TERMINAL_LABEL = '07'
    PURPOSE_OF_TRANSACTION = '08'
    ADDITIONAL_CONSUMER_DATA_REQUEST = '09'
