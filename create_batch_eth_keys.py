from ecdsa import SigningKey, VerifyingKey, SECP256k1
import os
import sha3
import csv
from Crypto.Cipher import AES
import hashlib

class AESED(object):
    def __init__(self, key):
        self.BLOCK_SIZE = 16
        self.key = key
        self.iv = self.key[:16]

    def encrypt(self, data):
        """加密数据
        """
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        return aes.encrypt(self.pad(data)).hex()

    def decode(self, hex_data):
        """解密数据"""
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.unpad(aes.decrypt(bytes.fromhex(hex_data)))

    def pad(self, data):
        pad = self.BLOCK_SIZE - len(data) % self.BLOCK_SIZE
        return (data + pad * chr(pad)).encode('utf-8')

    def unpad(self, padded):
        return padded[:-padded[-1]]


def get_md5(password):
    md5 = hashlib.md5()
    md5.update((password + "gauss").encode('utf-8'))
    return md5.digest()



def privateKey2publicKey(private_key_string):
    """私钥生成未压缩公钥
    """
    sk = SigningKey.from_string(bytes().fromhex(private_key_string), curve=SECP256k1)
    vk = sk.get_verifying_key()
    return vk.to_string().hex()

def publicKey2address(public_key):
    """从公钥生成地址
    """
    sha3256 = sha3.keccak_256(bytes().fromhex(public_key)).hexdigest()
    return '0x' + sha3256[-40:]



if __name__ == '__main__':
    try:
        nums = int(input("请输入您要生成的钱包地址数量："))
        password = input("请输入密码（请一定要记住，忘记钱包就没了）：")
        flag = input("是否保存私钥(y/n)：")
    except:
        print("请输入整数")
        exit()

    aesed = AESED(get_md5(password))

    with open("eth_keys.csv", 'w', encoding='utf-8', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(['地址', '公钥', '加密私钥{}'.format(password)])
        print("正在生成钱包，请稍后...")
        for i in range(nums):
            private_key = os.urandom(32).hex()
            encrypt_private_key = aesed.encrypt(private_key)
            public_key = privateKey2publicKey(private_key)
            address = publicKey2address(public_key)
            f_csv.writerow([address, public_key, encrypt_private_key, private_key if flag == 'y' else ''])

