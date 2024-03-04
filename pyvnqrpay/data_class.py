
from dataclasses import dataclass
from typing import Optional


@dataclass
class Provider:
    guid: str
    field_id: Optional[str] = ''
    name: Optional[str] = ''
    service: Optional[str] = ''


@dataclass
class Merchant:
    id: str
    name: str


@dataclass
class Consumer:
    bank_bin: str
    bank_number: str


@dataclass
class AdditionalData:
    store: Optional[str] = ''
    terminal: Optional[str] = ''
    bill_number: Optional[str] = ''
    mobile_number: Optional[str] = ''
    loyalty_number: Optional[str] = ''
    reference: Optional[str] = ''
    customer_label: Optional[str] = ''
    purpose: Optional[str] = ''
    data_request: Optional[str] = ''


@dataclass
class QRCode:
    is_valid: Optional[bool] = False
    version: Optional[str] = ''
    init_method: Optional[str] = ''
    provider: Optional[Provider] = None
    merchant: Optional[Merchant] = None
    consumer: Optional[Consumer] = None
    category: Optional[str] = ''
    currency: Optional[str] = ''
    amount: Optional[str] = ''
    tip_and_fee_type: Optional[str] = ''
    tip_and_fee_amount: Optional[str] = ''
    tip_and_fee_percent: Optional[str] = ''
    nation: Optional[str] = ''
    city: Optional[str] = ''
    zip_code: Optional[str] = ''
    additional_data: Optional[AdditionalData] = None
    crc: Optional[str] = ''
