# from CaseParams import CaseParams
#
#
# class SendMDRequst:
#     md_params=None
#     def __init__(self,subscription_request_type='1', market_depth='0', md_update_type='0',case_params=CaseParams):
#         self.subscription_request_type = subscription_request_type
#         self.market_depth=market_depth
#         self.md_update_type=md_update_type
#         self.case_params=case_params
#
#
#         self.md_params={
#         'SenderSubID': self.case_params.account,
#         'MDReqID': self.case_params.mdreqid,
#         'SubscriptionRequestType': self.subscription_request_type,
#         'MarketDepth': self.market_depth,
#         'MDUpdateType': self.md_update_type,
#         'NoMDEntryTypes': [{'MDEntryType': '0'}, {'MDEntryType': '1'}],
#         'NoRelatedSymbols': [
#             {
#                 'Instrument': {
#                     'Symbol': self.case_params.symbol,
#                     'SecurityType': self.case_params.securitytype,
#                     'Product': self.case_params.product
#                 },
#                 'SettlDate': self.case_params.settldate,
#                 'SettlType': self.case_params.settltype
#             }
#         ]
#         }
#        md_subscribe_response = {
#             'MDReqID': self.md_params['MDReqID'],
#             'Instrument': {
#                 'Symbol': self.case_params.symbol
#             },
#             'LastUpdateTime': '*',
#             'NoMDEntries': [
#                 {
#                     'SettlType': 0,
#                     'MDEntryPx': '*',
#                     'MDEntryTime': '*',
#                     'MDEntryID': '*',
#                     'MDEntrySize': '1000000',
#                     'QuoteEntryID': '*',
#                     'MDOriginType': 1,
#                     'SettlDate': self.case_params['SettlDate'].split(' ')[0],
#                     'MDQuoteType': 1,
#                     'MDEntryPositionNo': 1,
#                     'MDEntryDate': '*',
#                     'MDEntryType': 0
#                 },
#                 {
#                     'SettlType': 0,
#                     'MDEntryPx': '*',
#                     'MDEntryTime': '*',
#                     'MDEntryID': '*',
#                     'MDEntrySize': '1000000',
#                     'QuoteEntryID': '*',
#                     'MDOriginType': 1,
#                     'SettlDate': self.case_params['SettlDate'].split(' ')[0],
#                     'MDQuoteType': 1,
#                     'MDEntryPositionNo': 1,
#                     'MDEntryDate': '*',
#                     'MDEntryType': 1
#                 },
#                 {
#                     'SettlType': 0,
#                     'MDEntryPx': '*',
#                     'MDEntryTime': '*',
#                     'MDEntryID': '*',
#                     'MDEntrySize': '2000000',
#                     'QuoteEntryID': '*',
#                     'MDOriginType': 1,
#                     'SettlDate': self.case_params['SettlDate'].split(' ')[0],
#                     'MDQuoteType': 1,
#                     'MDEntryPositionNo': 2,
#                     'MDEntryDate': '*',
#                     'MDEntryType': 0
#                 },
#                 {
#                     'SettlType': 0,
#                     'MDEntryPx': '*',
#                     'MDEntryTime': '*',
#                     'MDEntryID': '*',
#                     'MDEntrySize': '2000000',
#                     'QuoteEntryID': '*',
#                     'MDOriginType': 1,
#                     'SettlDate': self.case_params['SettlDate'].split(' ')[0],
#                     'MDQuoteType': 1,
#                     'MDEntryPositionNo': 2,
#                     'MDEntryDate': '*',
#                     'MDEntryType': 1
#                 },
#             ]
#         }
#
#
#
#
#
#
#     def send_md_request(self):
#         print(self.md_params)
#
#
# params = CaseParams('Gold', '2021',securitytype='FXFWD')
# # SendMDRequst(case_params=params).send_md_request()
#
# caee = SendMDRequst(case_params=params)
# se = caee.case_params.account
# se2 = caee.case_params.settldate
# print(se)
# print(se2)
# print(caee.md_params)
# caee.send_md_request()
