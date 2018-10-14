#!/usr/bin/python3 -u

from datetime import datetime, timedelta
import time
from login_config import *
from resnet_login import run_login


try:
    while True:
        return_status = run_login(username, password)

        #Login not yet time out
        if return_status == 302:
            print("Login NOT yet timeout")
            #run next time

        #Login is successful
        elif return_status == 0:
            print("Login success")
            #run next time

        #cannot send request
        elif return_status == -1:
            print("Request ERROR")

        print("Start sleep for: "+str(login_freq )+" min")
        time.sleep(login_freq *60)
except KeyboardInterrupt:
    print('Stop process by user')




    