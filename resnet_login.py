import requests

def run_login(usr, pwd):
    login_url = 'http://securelogin.net.cuhk.edu.hk/cgi-bin/login'
    input_data = {'user' : usr , 'password' : pwd , 'cmd' : 'authenticate' , 'Login' : 'Log+In'}
    try:
        r = requests.post(login_url, input_data, allow_redirects=False)
    except Exception:
        return -1

    if 'Welcome' in r.text:
        return 0
    else:  
        return r.status_code

if __name__ == "__main__":
    from login_config import * #try to import user
    return_status = run_login(username, password)
    if return_status == 0:
        print("Login Success")
    elif return_status == -1:
        print("Request has some error")
    else:
        print("Login error")
        print("Respone code: "+str(return_status))
    