# md_subscribe_response = {
#     'MDReqID': '123',
#     'Instrument': {'Symbol': 'EUR'},
#     'NoMDEntries': [
#         {
#             'SettlType': 0,
#             'MDEntryPx': '*',
#             'MDEntryTime': '*',
#             'MDEntryID': '*',
#             'MDEntrySize': '1000000',
#             'QuoteEntryID': '*',
#             'MDOriginType': 1,
#             'SettlDate': 'df',
#             'MDQuoteType': 1,
#             'MDEntryPositionNo': 1,
#             'MDEntryDate': '*',
#             'MDEntryType': 0
#         }
#     ]
# }
# # print(md_subscribe_response)
# # new_t = md_subscribe_response['NoMDEntries']
# # print(md_subscribe_response)
# #
# # print(new_t)
# md_subscribe_response['NoMDEntries'][0]['SettlDate']='ffffff'
# print(md_subscribe_response)
