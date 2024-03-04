from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional
from .providers import VietQRStatus


@dataclass
class Bank:
    code: str
    name: str
    short_name: str
    bin: str
    vietqrstatus: VietQRStatus
    swift: str
    number: Optional[str] = None


class BankCode(Enum, str):
    ABBank = 'ABB'
    ACB = 'ACB'
    Agribank = 'AGRIBANK'
    BacABank = 'BAB'
    BaoVietBank = 'BAOVIETBANK'
    BIDC = 'BIDC'
    BIDV = 'BID'
    Cake = 'CAKE'
    CBBank = 'VNCB'
    CIMB = 'CIMB'
    COOPBank = 'COOPBANK'
    DBSBank = 'DBS'
    DongABank = 'DONGABANK'
    EXIMBank = 'EIB'
    GPBank = 'GPBANK'
    HDBank = 'HDB'
    HongLeongBank = 'HLB'
    HSBC = 'HSBC'
    IBKHCM = 'IBKHCM'
    IBKHN = 'IBKHN'
    IndovinaBank = 'IVB'
    KasikornBank = 'KBANK'
    KienLongBank = 'KLB'
    KookminBankHCM = 'KBHCM'
    KookminBankHN = 'KBHN'
    LienVietPostBank = 'LPB'
    MBBank = 'MBB'
    MSB = 'MSB'
    NamABank = 'NAB'
    NCB = 'NVB'
    NonghyupBankHN = 'NONGHYUP'
    OCB = 'OCB'
    OceanBank = 'OCEANBANK'
    PGBank = 'PGB'
    PublicBank = 'PBVN'
    PVCOMBank = 'PVCOMBANK'
    Sacombank = 'STB'
    SaigonBank = 'SGB'
    SCB = 'SCB'
    SEABank = 'SSB'
    SHB = 'SHB'
    ShinhanBank = 'SVB'
    StandardCharteredBank = 'SC'
    Techcombank = 'TCB'
    Timo = 'TIMO'
    TPBank = 'TPB'
    UBank = 'UBANK'
    UOB = 'UOB'
    VIB = 'VIB'
    VietABank = 'VAB'
    VietBank = 'VBB'
    VietCapitalBank = 'BVB'
    VCB = 'VCB'
    Vietinbank = 'CTG'
    VPBank = 'VPB'
    VRB = 'VRB'
    WooriBank = 'WRB'


def get_banks() -> Dict[str, Bank]:
    return {
        # A
        BankCode.ABBank: Bank(
            code=BankCode.ABBank,
            name='Ngân hàng TMCP An Bình',
            short_name='ABB',
            bin='970425',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='ABBKVNVX'
        ),
        BankCode.ACB: Bank(
            code=BankCode.ACB,
            name='Ngân hàng TMCP Á Châu',
            short_name='ACB',
            bin='970416',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='ASCBVNVX'
        ),
        BankCode.Agribank: Bank(
            code=BankCode.Agribank,
            name='Ngân hàng Nông nghiệp và Phát triển Nông thôn Việt Nam',
            short_name='Agribank',
            bin='970405',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='VBAAVNVX'
        ),

        # B
        BankCode.BacABank: Bank(
            code=BankCode.BacABank,
            name='Ngân hàng TMCP Bắc Á',
            short_name='Bac A Bank',
            bin='970409',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='NASCVNVX'
        ),
        BankCode.BaoVietBank: Bank(
            code=BankCode.BaoVietBank,
            name='Ngân hàng TMCP Bảo Việt',
            short_name='Bao Viet Bank',
            bin='970438',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='BVBVVNVX'
        ),
        BankCode.BIDC: Bank(
            code=BankCode.BIDC,
            name='Ngân hàng TMCP Đầu tư và Phát triển Campuchia',
            short_name='BIDC',
            bin='',
            vietqrstatus=VietQRStatus.NOT_SUPPORTED,
            swift='IDBCKHPP'
        ),
        BankCode.BIDV: Bank(
            code=BankCode.BIDV,
            name='Ngân hàng TMCP Đầu tư và Phát triển Việt Nam',
            short_name='BIDV',
            bin='970418',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='BIDVVNVX'
        ),

        # C
        BankCode.Cake: Bank(
            code=BankCode.Cake,
            name='Ngân hàng số CAKE by VPBank - Ngân hàng TMCP Việt Nam Thịnh Vượng',
            short_name='CAKE by VPBank',
            bin='546034',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift=''
        ),
        BankCode.CBBank: Bank(
            code=BankCode.CBBank,
            name='Ngân hàng Thương mại TNHH MTV Xây dựng Việt Nam',
            short_name='CBBank',
            bin='970444',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='GTBAVNVX'
        ),
        BankCode.CIMB: Bank(
            code=BankCode.CIMB,
            name='Ngân hàng TNHH MTV CIMB Việt Nam',
            short_name='CIMB Bank',
            bin='422589',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='CIBBVNVN'
        ),
        BankCode.COOPBank: Bank(
            code=BankCode.COOPBank,
            name='Ngân hàng Hợp tác xã Việt Nam',
            short_name='Co-op Bank',
            bin='970446',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift=''
        ),

        # D
        BankCode.DBSBank: Bank(
            code=BankCode.DBSBank,
            name='NH TNHH MTV Phát triển Singapore - Chi nhánh TP. Hồ Chí Minh',
            short_name='DBS Bank',
            bin='796500',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='DBSSVNVX'
        ),
        BankCode.DongABank: Bank(
            code=BankCode.DongABank,
            name='Ngân hàng TMCP Đông Á',
            short_name='Dong A Bank',
            bin='970406',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='EACBVNVX'
        ),

        # E
        BankCode.EXIMBank: Bank(
            code=BankCode.EXIMBank,
            name='Ngân hàng TMCP Xuất Nhập khẩu Việt Nam',
            short_name='Eximbank',
            bin='970431',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='EBVIVNVX'
        ),

        # G
        BankCode.GPBank: Bank(
            code=BankCode.GPBank,
            name='Ngân hàng Thương mại TNHH MTV Dầu Khí Toàn Cầu',
            short_name='GPBank',
            bin='970408',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='GBNKVNVX'
        ),

        # H
        BankCode.HDBank: Bank(
            code=BankCode.HDBank,
            name='Ngân hàng TMCP Phát triển TP. Hồ Chí Minh',
            short_name='HDBank',
            bin='970437',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='HDBCVNVX'
        ),
        BankCode.HongLeongBank: Bank(
            code=BankCode.HongLeongBank,
            name='Ngân hàng TNHH MTV Hong Leong Việt Nam',
            short_name='HongLeong Bank',
            bin='970442',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='HLBBVNVX'
        ),
        BankCode.HSBC: Bank(
            code=BankCode.HSBC,
            name='Ngân hàng TNHH MTV HSBC (Việt Nam)',
            short_name='HSBC Vietnam',
            bin='458761',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='HSBCVNVX'
        ),

        # I
        BankCode.IBKHCM: Bank(
            code=BankCode.IBKHCM,
            name='Ngân hàng Công nghiệp Hàn Quốc - Chi nhánh TP. Hồ Chí Minh',
            short_name='IBK HCM',
            bin='970456',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift=''
        ),
        BankCode.IBKHN: Bank(
            code=BankCode.IBKHN,
            name='Ngân hàng Công nghiệp Hàn Quốc - Chi nhánh Hà Nội',
            short_name='IBK HN',
            bin='970455',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift=''
        ),
        BankCode.IndovinaBank: Bank(
            code=BankCode.IndovinaBank,
            name='Ngân hàng TNHH Indovina',
            short_name='Indovina Bank',
            bin='970434',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift=''
        ),

        # K
        BankCode.KasikornBank: Bank(
            code=BankCode.KasikornBank,
            name='Ngân hàng Đại chúng TNHH KASIKORNBANK - CN TP. Hồ Chí Minh',
            short_name='Kasikornbank',
            bin='668888',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='KASIVNVX'
        ),
        BankCode.KienLongBank: Bank(
            code=BankCode.KienLongBank,
            name='Ngân hang TMCP Kiên Long',
            short_name='Kien Long Bank',
            bin='970452',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='KLBKVNVX'
        ),
        BankCode.KookminBankHCM: Bank(
            code=BankCode.KookminBankHCM,
            name='Ngân hàng Kookmin - Chi nhánh TP. Hồ Chí Minh',
            short_name='Kookmin Bank HCM',
            bin='970463',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift=''
        ),
        BankCode.KookminBankHN: Bank(
            code=BankCode.KookminBankHN,
            name='Ngân hàng Kookmin - Chi nhánh Hà Nội',
            short_name='Kookmin Bank HN',
            bin='970462',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift=''
        ),

        # L
        BankCode.LienVietPostBank: Bank(
            code=BankCode.LienVietPostBank,
            name='Ngân hàng TMCP Bưu Điện Liên Việt',
            short_name='LienVietPostBank',
            bin='970449',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='LVBKVNVX'
        ),

        # M
        BankCode.MBBank: Bank(
            code=BankCode.MBBank,
            name='Ngân hàng TMCP Quân đội',
            short_name='MBBank',
            bin='970422',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='MSCBVNVX'
        ),
        BankCode.MSB: Bank(
            code=BankCode.MSB,
            name='Ngân hàng TMCP Hàng Hải',
            short_name='MSB',
            bin='970426',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='MCOBVNVX'
        ),

        # N
        BankCode.NamABank: Bank(
            code=BankCode.NamABank,
            name='Ngân hang TMCP Nam Á',
            short_name='Nam A Bank',
            bin='970428',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='NAMAVNVX'
        ),
        BankCode.NCB: Bank(
            code=BankCode.NCB,
            name='Ngân hàng TMCP Quốc Dân',
            short_name='NCB',
            bin='970419',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='NVBAVNVX'
        ),
        BankCode.NonghyupBankHN: Bank(
            code=BankCode.NonghyupBankHN,
            name='Ngân hàng Nonghyup - Chi nhánh Hà Nội',
            short_name='Nonghyup Bank',
            bin='801011',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift=''
        ),

        # O
        BankCode.OCB: Bank(
            code=BankCode.OCB,
            name='Ngân hàng TMCP Phương Đông',
            short_name='OCB Bank',
            bin='970448',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='ORCOVNVX'
        ),
        BankCode.OceanBank: Bank(
            code=BankCode.OceanBank,
            name='Ngân hàng Thương mại TNHH MTV Đại Dương',
            short_name='Ocean Bank',
            bin='970414',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='OCBKUS3M'
        ),

        # P
        BankCode.PGBank: Bank(
            code=BankCode.PGBank,
            name='Ngân hàng TMCP Xăng dầu Petrolimex',
            short_name='PG Bank',
            bin='970430',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='PGBLVNVX'
        ),
        BankCode.PublicBank: Bank(
            code=BankCode.PublicBank,
            name='Ngân hàng TNHH MTV Public Việt Nam',
            short_name='Public Bank Vietnam',
            bin='970439',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='VIDPVNVX'
        ),
        BankCode.PVCOMBank: Bank(
            code=BankCode.PVCOMBank,
            name='Ngân hàng TMCP Đại Chúng Việt Nam',
            short_name='PVComBank',
            bin='970412',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='WBVNVNVX'
        ),

        # S
        BankCode.Sacombank: Bank(
            code=BankCode.Sacombank,
            name='Ngân hàng TMCP Sài Gòn Thương Tín',
            short_name='Sacombank',
            bin='970403',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='SGTTVNVX'
        ),
        BankCode.SaigonBank: Bank(
            code=BankCode.SaigonBank,
            name='Ngân hàng TMCP Sài Gòn Công Thương',
            short_name='SaigonBank',
            bin='970400',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='SBITVNVX'
        ),
        BankCode.SCB: Bank(
            code=BankCode.SCB,
            name='Ngân hàng TMCP Sài Gòn',
            short_name='SCB',
            bin='970429',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='SACLVNVX'
        ),
        BankCode.SEABank: Bank(
            code=BankCode.SEABank,
            name='Ngân hàng TMCP Đông Nam Á',
            short_name='SeABank',
            bin='970440',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='SEAVVNVX'
        ),
        BankCode.SHB: Bank(
            code=BankCode.SHB,
            name='Ngân hàng TMCP Sài Gòn - Hà Nội',
            short_name='SHB',
            bin='970443',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='SHBAVNVX'
        ),
        BankCode.ShinhanBank: Bank(
            code=BankCode.ShinhanBank,
            name='Ngân hàng TNHH MTV Shinhan Việt Nam',
            short_name='ShinhanBank',
            bin='970424',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='SHBKVNVX'
        ),
        BankCode.StandardCharteredBank: Bank(
            code=BankCode.StandardCharteredBank,
            name='Ngân hàng TNHH MTV Standard Chartered Bank Việt Nam',
            short_name='Standard Chartered Vietnam',
            bin='970410',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift='SCBLVNV'
        ),

        # T
        BankCode.Techcombank: Bank(
            code=BankCode.Techcombank,
            name='Ngân hàng TMCP Kỹ thương Việt Nam',
            short_name='Techcombank',
            bin='970407',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='VTCBVNVX'
        ),
        BankCode.Timo: Bank(
            code=BankCode.Timo,
            name='Ngân hàng số Timo by Bản Việt Bank',
            short_name='Timo',
            bin='963388',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift=''
        ),
        BankCode.TPBank: Bank(
            code=BankCode.TPBank,
            name='Ngân hàng TMCP Tiên Phong',
            short_name='TPBank',
            bin='970423',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='TPBVVNVX'
        ),

        # U
        BankCode.UBank: Bank(
            code=BankCode.UBank,
            name='Ngân hàng số Ubank by VPBank - Ngân hàng TMCP Việt Nam Thịnh Vượng',
            short_name='Ubank by VPBank',
            bin='546035',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift=''
        ),
        BankCode.UOB: Bank(
            code=BankCode.UOB,
            name='Ngân hàng United Overseas Bank Việt Nam',
            short_name='United Overseas Bank Vietnam',
            bin='970458',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift=''
        ),

        # V
        BankCode.VIB: Bank(
            code=BankCode.VIB,
            name='Ngân hàng TMCP Quốc tế Việt Nam',
            short_name='VIB',
            bin='970441',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='VNIBVNVX'
        ),
        BankCode.VietABank: Bank(
            code=BankCode.VietABank,
            name='Ngân hàng TMCP Việt Á',
            short_name='VietABank',
            bin='970427',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='VNACVNVX'
        ),
        BankCode.VietBank: Bank(
            code=BankCode.VietBank,
            name='Ngân hàng TMCP Việt Nam Thương Tín',
            short_name='VietBank',
            bin='970433',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='VNTTVNVX'
        ),
        BankCode.VietCapitalBank: Bank(
            code=BankCode.VietCapitalBank,
            name='Ngân hàng TMCP Bản Việt',
            short_name='Viet Capital Bank',
            bin='970454',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='VCBCVNVX'
        ),
        BankCode.VCB: Bank(
            code=BankCode.VCB,
            name='Ngân hàng TMCP Ngoại Thương Việt Nam',
            short_name='Vietcombank',
            bin='970436',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='BFTVVNVX'
        ),
        BankCode.Vietinbank: Bank(
            code=BankCode.Vietinbank,
            name='Ngân hàng TMCP Công thương Việt Nam',
            short_name='VietinBank',
            bin='970415',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='ICBVVNVX'
        ),
        BankCode.VPBank: Bank(
            code=BankCode.VPBank,
            name='Ngân hàng TMCP Việt Nam Thịnh Vượng',
            short_name='VPBank',
            bin='970432',
            vietqrstatus=VietQRStatus.SUPPORTED,
            swift='VPBKVNVX'
        ),
        BankCode.VRB: Bank(
            code=BankCode.VRB,
            name='Ngân hàng Liên doanh Việt - Nga',
            short_name='Viet Nga Bank',
            bin='970421',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift=''
        ),

        # W
        BankCode.WooriBank: Bank(
            code=BankCode.WooriBank,
            name='Ngân hàng TNHH MTV Woori Việt Nam',
            short_name='Woori Bank',
            bin='970457',
            vietqrstatus=VietQRStatus.RECEIVE_ONLY,
            swift=''
        ),
    }


BANK_MAP = get_banks()
