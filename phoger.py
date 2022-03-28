from res.lib import enclib
from res.lib import utils
import argparse
import hashlib,json


# Parsing the arguments from command line

parser = argparse.ArgumentParser(description="Phoger Image Steganography App")
parser.add_argument('msg', metavar='msg',
                    type=str, help='Message to encrypt.')
parser.add_argument('password', metavar='password',
                    type=str, help='Password for encrypting.')
args = parser.parse_args()
password = args.password
msg = args.msg

# Function to Convert the given password to 32 byte MD5 Hash


def to_md5(password):
    pass_in_md5 = hashlib.md5(password.encode())
    pass_hash = pass_in_md5.hexdigest()
    return pass_hash


# Function to encrypt to AES 256 GCM ,a bit string will be returned

encrypted_msg = enclib.encrypt_AES_256_GCM(msg, to_md5(password))

# Pillow integration

#######################################################################
#Test and Trial Printing section below
#######################################################################

#print("Message = ", encrypted_msg, "  Password Hash=", to_md5(password))

#print("len=",enclib.decrypt_AES_256_gcm(encrypted_msg,"abc"))
#m = to_md5("manu4")
#print(enclib.decrypt_AES_256_gcm(encrypted_msg[0],m),"\n\n\n")

#print(encrypted_msg[2],encrypted_msg[1],"\n\n\n", enclib.decrypt_AES_256_gcm(encrypted_msg[0],m))
print(encrypted_msg,enclib.decrypt_AES_256_gcm(encrypted_msg,to_md5(password)))

#print(encrypted_msg[2],encrypted_msg[1],"\n\n\n", enclib.decrypt_AES_256_gcm(encrypted_msg[0],m))



#print(encrypted_msg[1],"\n\n\n", enclib.decrypt_AES_256_gcm(encrypted_msg[0],m))
