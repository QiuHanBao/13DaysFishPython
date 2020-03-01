from fake_useragent import UserAgent
from urllib.request import Request, urlopen
from urllib.parse import urlencode

headers = {
    "User-Agent": UserAgent().chrome,
}
login_url = 'https://up.woozooo.com/account.php'

# action: login
# task: login
# ref: /mydisk.php
# setSessionId: 010B3TrWzwsdkM2Lqh18cIU-GByYfpgWtCRxvz9Js_ipA7ycnEueFjFo6tmsnA17zjMLdQAdS4AOh-C2RpBmD1PtILksAsi_jOiYiArUQCcwdB868MvOl8tcUwL1pP4Cne0OzDIEl0hulND2KabpyRVms5nesh5-QUA_aL8kY_7EMcWRnKswwdv0PUS40xBUhNnALcbseNIzyI6tVyQ-jUIA
# setToken: FFFF0N00000000000555:1583056636186:0.7651821447303349
# setSig: 05XqrtZ0EaFgmmqIQes-s-CCZtkM_GTnSrWIvJMi16TUzIRPPQIWMcguLlt2gPF_Kyz_wIyIvPXDuUNlqYbII1z9kWdBSurrEKalHmjdU8mW5c61lO4c5xF4cmdomh5dU6aUHn2Yg8Z-DzSx4xYFvpbPcIz3TxrxLUgchHluWFxzGqgfl08SHMnECHQuRyw0nSbrKHTH9s9SuJGrk0bPXSIjZ_zEntyWJhBXHQnLF7ts6J5qhY_MrcYaNOV0HVaB0v01Ar3YahFiLVfGqfBS59zo-EazdHa8l4wwQmNE8PwSOwskkYYZDQRhB9iGNOJyCachaRe21BHIjsbNcb73iMKQt15XfRDy-jFSafEaBrzCVcbpNyuH4sxpSAW6Vq8kgufT_q94FMy56AUu_HL_y1oz0ZFS1mz4z4HP5D9PkHdQQoL2yTttEl8iPlyFOOe6bvFJGNnlMgnX0zDUScd4-28Yf_jWNE1z97YEZneDYoyNo
# setScene: nc_login
# formhash: 5dc76a08
# username: 15808480904
# password: 20110531

form_data = {
    'username': '15808480904',
    'password': '20110531'
}
f_data=urlencode(form_data).encode()
request =Request(login_url,headers=headers,data=f_data)
response=urlopen(request)
print(response.read().decode())
#访问页面
