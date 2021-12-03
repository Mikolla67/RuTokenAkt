import time
import s_RuToken, s_eToken
timing = time.time()
rlib = s_RuToken.ini_lib_RuToken()
elib = s_eToken.ini_lib_eToken()
while True:
    if time.time() - timing > 1.0:
        timing = time.time()
        s_RuToken_SN = s_RuToken.survey_RuToken(rlib)
        s_eToken_SN = s_eToken.survey_eToken(elib)
        if s_RuToken_SN != '000000':
            print(f"RuToken: ",s_RuToken_SN)

        if s_eToken_SN != '000000':
            print(f"eToken: ",s_eToken_SN)