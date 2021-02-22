import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status != 200:
        raise RuntimeError(f'Error : {res.status_code}, try again')
    return res

def pwned_api_check(password):
    hashedpassword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_chars, tail = hashedpassword[:5], hashedpassword[5:] 
    print(f'{first_chars}, {tail}')
    return hashedpassword


pwned_api_check('123')