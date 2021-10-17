

class CommonValue:

    connectivity = 'fix-ss-308-mercury-standard'
    # mdreqid = bca.client_orderid(10)
    # clordid = bca.client_orderid(9)
    mdreqid = '1234567890'
    clordid = '123456789'

    # def __init__(self,account,handlinstr,
    #              side,orderqty,ordtype,timeinforce,currency,settlcurrency,
    #              settdate, symbol, securitytype, securityidsource,
    #              securityid, securityexchange, product):
    #     self.account=account
    #     self.handlinstr=handlinstr
    #     self.side=side
    #     self.orderqty=orderqty
    #     self.ordtype=ordtype
    #     self.timeinforce=timeinforce
    #     self.currency=currency
    #     self.settlcurrency=settlcurrency
    #     self.settdate=settdate
    #     self.symbol=symbol
    #     self.securitytype=securitytype
    #     self.securityidsource=securityidsource
    #     self.securityid=securityid
    #     self.securityexchange=securityexchange
    #     self.product=product
    def __init__(self,account):
        self.account=account




new_report = CommonValue('name')
new_report.mdreqid='95874'
print(new_report.mdreqid)