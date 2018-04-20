"""
EOS钱包生成算法
未压缩私钥与比特币一样是256位整数，生成方式一样,生成压缩私钥和公钥的方式也和比特币一样
生成地址的过程不太样，过程如下:
1. 对公钥ripemd160
2. 取后四位作为checksum
3. 将第1步和第2步的值加在一起，base58编码
4. 第3步的结果前面加上'EOS'前缀

"""
import os
import hashlib
import base58
from ecdsa import SigningKey, VerifyingKey, SECP256k1



def ripemd160(data):
    """先sha256，在ripemd160
    返回20字节的public key hash
    """
    h = hashlib.new('ripemd160')
    h.update(bytes().fromhex(data))
    return h.digest()

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


# 从公钥生成地址
def publicKey2address(public_key_string):
    """从公钥生成未压缩地址
    """
    h160 = ripemd160(public_key_string)
    checksum = h160[:4]
    address = 'EOS' + base58.b58encode(bytes().fromhex(public_key_string) + checksum)
    return address


def WIF2privateKey(wif_private_key_string):
    """压缩形式的wif私钥转成原始的私钥
    """
    payload = base58.b58decode(wif_private_key_string)[1:-4]
    return payload.hex()


def eos_privatekey2address(eos_private_key):
    raw_privatekey = WIF2privateKey(eos_private_key)
    public_key = privateKey2publicKeyCompress(raw_privatekey)
    address = publicKey2address(public_key)
    return address

def ethprivate2eosprivateandpublickey(private_key):
    raw_privatekey = private_key.strip('0x')
    eos_private_key = privateKey2WIF(raw_privatekey)
    public_key = privateKey2publicKeyCompress(raw_privatekey)
    address = publicKey2address(public_key)
    return eos_private_key, address



if __name__ == '__main__':

    # 原始私钥
    private_key = os.urandom(32).hex()

    # wif形式私钥
    wif_private_key = privateKey2WIF(private_key)

    # 公钥
    public_key = privateKey2publicKeyCompress(private_key)

    # 地址
    address = publicKey2address(public_key)
    print("原始私钥：", private_key)
    print("EOS私钥：", wif_private_key)
    print("EOS公钥：", public_key)
    print("EOS地址：", address)

    print(WIF2privateKey(wif_private_key))

