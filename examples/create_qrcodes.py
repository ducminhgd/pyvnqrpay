import segno
from pyvnqrpay import qr


def create_vnpay_qr_code():
    qr_code = qr.create_vnpayar_data(
        10000, qr.Merchant(id='1234567890', name='VNPAY'),
        qr.AdditionalData(purpose='test purpose')
    )
    content = qr.qr_to_str(qr_code)
    print(content)
    qrcode = segno.make(content, micro=False)
    qrcode.save('qrcode.png', kind='png', scale=10)


if __name__ == '__main__':
    create_vnpay_qr_code()
