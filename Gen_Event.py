import time
import s_RuToken, s_eToken
timing = time.time()
rlib = s_RuToken.ini_lib_RuToken()
elib = s_eToken.ini_lib_eToken()
while True:
    if time.time() - timing > 1.0:
        timing = time.time()
        print("RuToken: " + s_RuToken.survey_RuToken(rlib))
        print("eToken: " + s_eToken.survey_eToken(elib))
        #print("10 seconds")