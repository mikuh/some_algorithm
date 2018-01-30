"""
生成以太坊钱包私钥公钥和地址
实例：（使用myetherwallet验证过）
私钥是： 69c74e3c0125acb86676e681d8df52072dc1d85aa90c6685a8050d0e6e0858f5
公钥是： 8a8a28106be2823c3e695e182730e65343a91df109262a3292cc6294fce558d8ab3d01981412f096db440c4434be8d5288cdc514688e0d3810aec48637754357
地址是： 0xeceeb1e065cb4ccffb0c8c04c4b5fea29bc95b9e

"""
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import os
import sha3

print("您的以太坊钱包：")

private_key = os.urandom(32).hex()
# private_key = '69c74e3c0125acb86676e681d8df52072dc1d85aa90c6685a8050d0e6e0858f5'
print('私钥是：', private_key)


# 从私钥生成公钥
def privateKey2publicKey(private_key_string):
    """私钥生成未压缩公钥
    """
    sk = SigningKey.from_string(bytes.fromhex(private_key_string), curve=SECP256k1)
    vk = sk.get_verifying_key()
    return vk.to_string().hex()

public_key = privateKey2publicKey(private_key)
print('公钥是：', public_key)

def publicKey2address(public_key):
    """从公钥生成地址
    """
    sha3256 = sha3.keccak_256(bytes().fromhex(public_key)).hexdigest()
    return '0x' + sha3256[-40:]

address = publicKey2address(public_key)
print('地址是：', address)