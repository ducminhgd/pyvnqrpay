# pylint: disable=missing-module-docstring
import os
from decimal import Decimal
from enum import Enum
from typing import Tuple, Union
from pyvnqrpay import providers
from pyvnqrpay.data_class import Merchant, Provider, QRCode, AdditionalData, Consumer
from pyvnqrpay.utils import make_crc16


class FieldID(str, Enum):  # pylint: disable=missing-class-docstring
    PROVIDER_FIELD_GUID = '00'
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


class AdditionalDataID(str, Enum):  # pylint: disable=missing-class-docstring
    BILL_NUMBER = '01'
    MOBILE_NUMBER = '02'
    STORE_LABEL = '03'
    LOYALTY_NUMBER = '04'
    REFERENCE_LABEL = '05'
    CUSTOMER_LABEL = '06'
    TERMINAL_LABEL = '07'
    PURPOSE_OF_TRANSACTION = '08'
    ADDITIONAL_CONSUMER_DATA_REQUEST = '09'


def combine_field_data(field_id: str, data: str) -> str:
    """
    Combine the field ID and data into a single string.

    Args:
        field_id (str): The ID of the field.
        data (str): The data to be combined with the field ID.

    Returns:
        str: The combined string.
    """
    if len(field_id) != 2 or len(data) == 0:
        return ''
    return f'{str(field_id)}{len(data):0>2}{data}'


def slide_field_data(content: str) -> Tuple[str, str, str]:
    """
    A function to extract field data from the given content string.

    Args:
        content (str): The content string from which to extract the field data.

    Returns:
        Tuple[str, str, str]: A tuple containing the field ID, value, and the remaining content string.
    """
    field_id = content[:2]
    length = int(content[2:4])
    value = content[4:4 + length]
    return field_id, value, content[4 + length:]


def create_vietqr_data(amount: Union[int, float, Decimal], service: str, consumer: Consumer, addtional_data: AdditionalData) -> QRCode:
    """
    Create a VietQR code based on the provided amount, service, consumer, and additional data.

    Args:
        amount (Union[int, float, Decimal]): The amount for the QR code.
        service (str): The service type for the QR code.
        consumer (Consumer): The consumer information for the QR code.
        additional_data (AdditionalData): Additional data for the QR code.

    Returns:
        QRCode: The generated QR code.
    """
    if str(amount) != '':
        init_method = '12'
    else:
        init_method = '11'

    if service == '':
        service = providers.VietQRService.FAST_TRANSFER_BY_ACCOUNT_NUMBER.value

    return QRCode(
        init_method=init_method,
        provider=Provider(
            field_id=providers.VietQRProvider.FIELD_ID.value,
            guid=providers.VietQRProvider.GUID.value,
            name=providers.VietQRProvider.NAME.value,
            service=service,
        ),
        consumer=consumer,
        amount=amount,
        additional_data=AdditionalData(
            purpose=addtional_data.purpose,
        ),
    )


def create_vnpayar_data(amount: Union[int, float, Decimal], merchant: Merchant, addtional_data: AdditionalData) -> QRCode:
    """
    Create a VNPay QR code with the given amount, merchant, and additional data.

    Parameters:
        amount (Union[int, float, Decimal]): The amount for the QR code.
        merchant (Merchant): The merchant information.
        addtional_data (AdditionalData): Additional data for the QR code.

    Returns:
        QRCode: The generated QR code.
    """
    return QRCode(
        merchant=merchant,
        provider=Provider(
            field_id=providers.VNPayProvider.FIELD_ID.value,
            guid=providers.VNPayProvider.GUID.value,
            name=providers.VNPayProvider.NAME.value,
        ),
        amount=amount,
        additional_data=AdditionalData(
            purpose=addtional_data.purpose,
        ),
    )


def qr_to_str(qr_code: QRCode) -> str:
    """
    Build a QR code string based on the provided QRCode object and its associated data fields.

    Args:
        qr_code (QRCode): The QRCode object containing the data for building the QR code.

    Returns:
        str: The complete QR code string including the CRC checksum.
    """
    version = combine_field_data(FieldID.VERSION.value, os.getenv('QRCODE_VERSION', '01'))
    init_method = combine_field_data(FieldID.INIT_METHOD.value, qr_code.init_method)
    guid = combine_field_data(FieldID.PROVIDER_FIELD_GUID.value, qr_code.provider.guid)

    if qr_code.provider.guid == providers.VietQRProvider.GUID.value:
        bank_bin = combine_field_data(providers.VietQRConsumerID.BANK_BIN.value, qr_code.consumer.bank_bin)
        bank_number = combine_field_data(providers.VietQRConsumerID.BANK_NUMBER.value, qr_code.consumer.bank_number)
        provider_content_data = bank_bin + bank_number
    elif qr_code.provider.guid == providers.VNPayProvider.GUID.value:
        # this may raise error, we can catch it outside
        provider_content_data = qr_code.merchant.id
    else:
        provider_content_data = ''
    provider = combine_field_data(providers.Field.DATA.value, provider_content_data)
    service = combine_field_data(providers.Field.SERVICE.value, qr_code.provider.service)
    provider_data = combine_field_data(qr_code.provider.field_id, guid + provider + service)

    category = combine_field_data(FieldID.CATEGORY.value, qr_code.category)
    # 704 is VND
    currency = combine_field_data(FieldID.CURRENCY.value, qr_code.currency or os.getenv('DEFAULT_CURRENCY', '704'))
    amount = combine_field_data(FieldID.AMOUNT.value, str(qr_code.amount))
    tip_and_fee_type = combine_field_data(FieldID.TIP_AND_FEE_TYPE.value, qr_code.tip_and_fee_type)
    tip_and_fee_amount = combine_field_data(FieldID.TIP_AND_FEE_AMOUNT.value, qr_code.tip_and_fee_amount)
    tip_and_fee_percent = combine_field_data(FieldID.TIP_AND_FEE_PERCENT.value, qr_code.tip_and_fee_percent)
    nation = combine_field_data(FieldID.NATION.value, qr_code.nation or 'VN')
    merchant_name = combine_field_data(FieldID.MERCHANT_NAME.value, qr_code.merchant.name)
    city = combine_field_data(FieldID.CITY.value, qr_code.city)
    zip_code = combine_field_data(FieldID.ZIP_CODE.value, qr_code.zip_code)

    bill_number = combine_field_data(AdditionalDataID.BILL_NUMBER, qr_code.additional_data.bill_number)
    mobile_number = combine_field_data(AdditionalDataID.MOBILE_NUMBER, qr_code.additional_data.mobile_number)
    store_label = combine_field_data(AdditionalDataID.STORE_LABEL, qr_code.additional_data.store)
    loyalty_number = combine_field_data(AdditionalDataID.LOYALTY_NUMBER, qr_code.additional_data.loyalty_number)
    reference = combine_field_data(AdditionalDataID.REFERENCE_LABEL, qr_code.additional_data.reference)
    customer_label = combine_field_data(AdditionalDataID.CUSTOMER_LABEL, qr_code.additional_data.customer_label)
    termial = combine_field_data(AdditionalDataID.TERMINAL_LABEL, qr_code.additional_data.terminal)
    purpose = combine_field_data(AdditionalDataID.PURPOSE_OF_TRANSACTION, qr_code.additional_data.purpose)
    data_request = combine_field_data(AdditionalDataID.ADDITIONAL_CONSUMER_DATA_REQUEST,
                                      qr_code.additional_data.data_request)

    additional_data_content = bill_number + mobile_number + store_label + \
        loyalty_number + reference + customer_label + termial + purpose + data_request
    additional_data = combine_field_data(FieldID.ADDITIONAL_DATA.value, additional_data_content)

    content = version + init_method + provider_data + category + currency + amount + tip_and_fee_type + tip_and_fee_amount + \
        tip_and_fee_percent + nation + merchant_name + city + zip_code + additional_data + FieldID.CRC.value + '04'
    crc = make_crc16(content)
    return content + crc
