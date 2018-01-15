"""
比特币密钥和地址生成算法
示例：
私钥是（未压缩）：3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa6
私钥（WIF）：5JG9hT3beGTJuUAmCQEmNaxAuMacCTfXuw1R3FCXig23RQHMr4K
私钥（压缩）：3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa601
私钥(压缩 WIF)：KyBsPXxTuVD82av65KZkrGrWi5qLMah5SdNq6uftawDbgKa2wv6S
公钥是(未压缩)： 045c0de3b9c8ab18dd04e3511243ec2952002dbfadc864b9628910169d9b9b00ec243bcefdd4347074d44bd7356d6a53c495737dd96295e2a9374bf5f02ebfc176
公钥（压缩）：025c0de3b9c8ab18dd04e3511243ec2952002dbfadc864b9628910169d9b9b00ec
地址是(未压缩)： 1thMirt546nngXqyPEz532S8fLwbozud8
地址(压缩)： 14cxpo3MBCYYWCgF74SWTdcmxipnGUsPw3
"""
import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import base58
import os


def hash160(data):
    """先sha256，在ripemd160
    返回20字节的public key hash
    """
    sha256 = hashlib.sha256(bytes().fromhex(data)).digest()
    h = hashlib.new('ripemd160')
    h.update(sha256)
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

# 生成一个私钥
private_key = os.urandom(32).hex()
# private_key = '3aba4162c7251c891207b747840551a71939b0de081f85c4e44cf7c13e41daa6'



# 从私钥生成公钥
def privateKey2publicKey(private_key_string):
    """私钥生成未压缩公钥
    公钥类型1个字节、32字节x 32字节y 一共65字节
    """
    sk = SigningKey.from_string(bytes.fromhex(private_key_string), curve=SECP256k1)
    vk = sk.get_verifying_key()
    # 前面加上04代表未压缩
    return (b'\x04' + vk.to_string()).hex()

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
    h160 = hash160(public_key_string)
    address = base58CheckEncode(b'\00', h160)
    return address


# WIF格式的私钥
def privateKey2WIF(private_key_string):
    version = b'\x80'
    payload = bytes().fromhex(private_key_string)
    return base58CheckEncode(version, payload)


public_key = privateKey2publicKey(private_key)
address = publicKey2address(public_key)
private_key_wif = privateKey2WIF(private_key)
public_key_compress = privateKey2publicKeyCompress(private_key)
address_compress = publicKey2address(public_key_compress)

print("私钥是（未压缩）：{}".format(private_key))
print("私钥（WIF）：{}".format(private_key_wif))
print("私钥（压缩）：{}".format(private_key+'01'))
print("私钥(压缩 WIF)：{}".format(privateKey2WIF(private_key+'01')))
print("公钥是(未压缩)：", public_key)
print("公钥（压缩）：{}".format(public_key_compress))
print("地址是(未压缩)：", address)
print("地址(压缩)：", address_compress)


