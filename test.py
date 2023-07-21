
# import hashlib

# hsobj = hashlib.sha256()
# secret = 'RP4XkEtvy3a60ZCwIzUn'
# platform = 'MINI-INVOICE'

# ent_code = 'EC3N4H0DO8KSBC'
# user_id = 'lincd,15013592176,null'
# timestamp='1689043449019'

# value = secret + ':' + platform + ':' + ent_code + ':' + user_id + '::' + timestamp
# hsobj.update(value.encode("utf-8"))
# token = hsobj.hexdigest()
# print(token)
def test(name, age):
    print(name, age)