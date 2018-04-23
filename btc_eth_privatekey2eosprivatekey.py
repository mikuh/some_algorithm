# coding:utf-8
import hashlib
import base58
from ecdsa import SigningKey, SECP256k1



def ripemd160(data):
    """先sha256，在ripemd160
    返回20字节的public key hash
    """
    h = hashlib.new('ripemd160')
    h.update(bytes().fromhex(data))
    return h.digest()


# 从私钥生成压缩公钥
def privateKey2publicKeyCompress(private_key_string):
    """私钥生成压缩公钥"""
    sk = SigningKey.from_string(bytes.fromhex(private_key_string), curve=SECP256k1)
    vk = sk.get_verifying_key()
    x = vk.to_string()[:32]
    y = vk.to_string()[32:]
    if y[-1] % 2 == 0:
        prefix = b'\x02'
    else:
        prefix = b'\x03'
    return (prefix + x).hex()

def base58CheckEncode(version, payload):
    """对数据进行base58check编码
    1.添加版本字节前缀 前缀用来识别编码的数据的类型
    比特币地址的前缀是0（十六进制是0x00），而对私钥编码时前缀是128（十六进制是0x80）
    2.计算“双哈希”校验和，对第1步的结果执行两次SHA256，再取前4个字节，添加到第1步结果末尾
    3.对第2步结果base58编码
    """
    s = version + payload
    checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
    result = base58.b58encode(s + checksum)
    return result

# WIF格式的私钥
def privateKey2WIF(private_key_string):
    version = b'\x80'
    payload = bytes().fromhex(private_key_string)
    return base58CheckEncode(version, payload)


# 从公钥生成地址
def publicKey2address(public_key_string):
    """从公钥生成未压缩地址
    """
    h160 = ripemd160(public_key_string)
    checksum = h160[:4]
    address = 'EOS' + base58.b58encode(bytes().fromhex(public_key_string) + checksum)
    return address


def ethprivate2eosprivateandpublickey(private_key):
    raw_privatekey = private_key.strip('0x')
    eos_private_key = privateKey2WIF(raw_privatekey)
    public_key = privateKey2publicKeyCompress(raw_privatekey)
    address = publicKey2address(public_key)
    return eos_private_key, address


if __name__ == '__main__':
    print("声明：本程序可以通过您的eth私钥生成对应的EOS私钥和地址，但未经全面测试，不承担任何后果，为确保安全可以将此处私钥对应的地址与EOS官网生成的对比一下。")
    private_key = input("请输入您的eth私钥：")
    eos_private_key, address = ethprivate2eosprivateandpublickey(private_key)
    print("您的EOS私钥：", eos_private_key)
    print("您的EOS地址：", address)
    print()
    input("按任意键，结束程序...")
