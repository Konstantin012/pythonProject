from aqa.CaseParams import CaseParams

one_band = {
    'SettlType': 0,
    'MDEntryPx': '*',
    'MDEntryTime': '*',
    'MDEntryID': '*',
    'MDEntrySize': '1000000',
    'QuoteEntryID': '*',
    'MDOriginType': 1,
    'SettlDate': '',
    'MDQuoteType': 1,
    'MDEntryPositionNo': 1,
    'MDEntryDate': '*',
    'MDEntryType': 0
}
class Nert():
    test_var=None
    price=0
    def __init__(self,price,caseP=CaseParams):
        self.caseP=caseP
        self.price=price




    def case(self):
        self.test_var = self.caseP.side


    def case45(self):
        print(self.test_var)
        print(self.price)

    md_subscribe_response = {
        'MDReqID': '2',
        'Instrument': {
            'Symbol': ''
        },
        'LastUpdateTime': '*',
        'NoMDEntries': [
            {
                'SettlType': 0,
                'MDEntryPx': '*',
                'MDEntryTime': '*',
                'MDEntryID': '*',
                'MDEntrySize': '1000000',
                'QuoteEntryID': '*',
                'MDOriginType': 1,
                'SettlDate': '',
                'MDQuoteType': 1,
                'MDEntryPositionNo': 1,
                'MDEntryDate': '*',
                'MDEntryType': 0
            },
            {
                'SettlType': 0,
                'MDEntryPx': '*',
                'MDEntryTime': '*',
                'MDEntryID': '*',
                'MDEntrySize': '1000000',
                'QuoteEntryID': '*',
                'MDOriginType': 1,
                'SettlDate': '',
                'MDQuoteType': 1,
                'MDEntryPositionNo': 1,
                'MDEntryDate': '*',
                'MDEntryType': 1
            }

        ]
    }

    def prepare_md_for_verify(self, *args, published=True, priced=True, ):
        band_number=len(args)
        if len(args) > 0:
            band = 0
            self.md_subscribe_response['NoMDEntries'].clear()
            md_entry_position=1
            for qty in args:
                md_entry_type = 0
                while md_entry_type < 2:
                    # self.md_subscribe_response['NoMDEntries'].append(one_band)
                    self.md_subscribe_response['NoMDEntries'].append({
                        'SettlType': 0,
                        'MDEntryPx': '*',
                        'MDEntryTime': '*',
                        'MDEntryID': '*',
                        'MDEntrySize': '1000000',
                        'QuoteEntryID': '*',
                        'MDOriginType': 1,
                        'SettlDate': '',
                        'MDQuoteType': 1,
                        'MDEntryPositionNo': 1,
                        'MDEntryDate': '*',
                        'MDEntryType': 0
                    })
                    self.md_subscribe_response['NoMDEntries'][band]['MDEntrySize'] = qty
                    self.md_subscribe_response['NoMDEntries'][band]['MDEntryType'] = md_entry_type
                    self.md_subscribe_response['NoMDEntries'][band]['MDEntryPositionNo'] = md_entry_position
                    self.md_subscribe_response['NoMDEntries'][band]['SettlDate'] = '2021/05/08'
                    md_entry_type +=1
                    band +=1
                md_entry_position +=1
        print(self.md_subscribe_response)



# far = Nert()
# # far.change()
# far.prepare_md_for_verify(5555555)
