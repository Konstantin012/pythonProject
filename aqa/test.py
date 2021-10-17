from aqa.CaseParams import CaseParams
from aqa.bands import Nert

depo = CaseParams('name','15','2021')
a=depo.case_id
# print(a)
depo2 = Nert(547,depo)
depo2.case()
depo2.case45()
# b =depo2.test_var
# print(b)
# depo2.case()
