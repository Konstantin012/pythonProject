
from datetime import datetime

class CaseParams:

    connectivity = 'fix-ss-308-mercury-standard'
    # mdreqid = bca.client_orderid(10)
    # clordid = bca.client_orderid(9)
    mdreqid = '1234567890'
    clordid = '123456789'

    def __init__(self,account,case_id,settldate, handlinstr='1',
                 side='1',orderqty=1,ordtype='2',timeinforce='4',currency='EUR',settlcurrency='USD',
                 settltype=0, symbol='EUR/USD', securitytype='FXSPOT', securityidsource='8',
                 securityid='EUR/USD', securityexchange='XQFX', product=4):
        self.account=account
        self.case_id=case_id
        self.handlinstr=handlinstr
        self.side=side
        self.orderqty=orderqty
        self.ordtype=ordtype
        self.timeinforce=timeinforce
        self.currency=currency
        self.settlcurrency=settlcurrency
        self.settltype=settltype
        self.settldate=settldate
        self.symbol=symbol
        self.securitytype=securitytype
        self.securityidsource=securityidsource
        self.securityid=securityid
        self.securityexchange=securityexchange
        self.product=product

