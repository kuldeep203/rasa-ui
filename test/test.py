# import ldap
# username = "CN=Tarun Gupta,OU=Delhi AISGlass,OU=AIS Users,DC=asahiindia,DC=com"
# password ="tasty@lemon09"
# address = "80.0.0.108"
# # username= 'CN=Administrator,CN=Users,DC=tcplcoe,DC=com'
# # password= "Xanadu@@12345"
# # address = "172.16.19.20"
#
# def is_user_exist(address, username, password):
#     conn = ldap.initialize('ldap://' + address)
#     conn.protocol_version = 3
#     conn.set_option(ldap.OPT_REFERRALS, 0)
#     try:
#         conn.simple_bind_s(username, password)
#     except ldap.INVALID_CREDENTIALS:
#         print("invalid credentials")
#
# print(is_user_exist(address,username,password))

username = "test2"
userfullpath = f"{username}"+"@asahiindia.com"
print(userfullpath)
