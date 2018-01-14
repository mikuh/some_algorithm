import hashlib
import ecdsa
from ecdsa import VerifyingKey, SECP256k1

def hash160(data):
    sha256 = hashlib.sha256(bytes().fromhex(data)).hexdigest()
    h = hashlib.new('ripemd160')
    h.update(bytes().fromhex(sha256))
    return h.hexdigest()

def dhash256(data):
    return hashlib.sha256(hashlib.sha256(bytes().fromhex(data)).digest()).digest()

rep = "8b4830450221009908144ca6539e09512b9295c8a27050d478fbb96f8addbc3d075544dc41328702201aa528be2b907d316d2da068dd9eb1e23243d97e444d59290d2fddf25269ee0e0141042e930f39ba62c6534ee98ed20ca98959d34aa9e057cda01cfd422c6bab3667b76426529382c23f42b9b08d7832d4fee1d6b437a8526e59667ce9c4e9dcebcabb"
hash_text = dhash256("01000000018dd4f5fbd5e980fc02f35c6ce145935b11e284605bf599a13c6d415db55d07a1000000008b4830450221009908144ca6539e09512b9295c8a27050d478fbb96f8addbc3d075544dc41328702201aa528be2b907d316d2da068dd9eb1e23243d97e444d59290d2fddf25269ee0e0141042e930f39ba62c6534ee98ed20ca98959d34aa9e057cda01cfd422c6bab3667b76426529382c23f42b9b08d7832d4fee1d6b437a8526e59667ce9c4e9dcebcabbffffffff0200719a81860000001976a914df1bd49a6c9e34dfa8631f2c54cf39986027501b88ac009f0a5362000000434104cd5e9726e6afeae357b1806be25a4c3d3811775835d235417ea746b7db9eeab33cf01674b944c64561ce3388fa1abd0fa88b06c44ce81e2234aa70fe578d455dac0000000001000000".replace(rep, "1976a91446af3fb481837fadbb421727f9959c2d32a3682988ac"))
print(hash_text.hex())
# c2d48f45d7fbeff644ddb72b0f60df6c275f0943444d7df8cc851b3d55782669
def verify():
    # 先构建一个栈
    stack = []

    # 第一条是数据,直接入栈
    stack.append("30450221009908144ca6539e09512b9295c8a27050d478fbb96f8addbc3d075544dc41328702201aa528be2b907d316d2da068dd9eb1e23243d97e444d59290d2fddf25269ee0e01")

    # 第二条也是数据，直接入栈
    stack.append("042e930f39ba62c6534ee98ed20ca98959d34aa9e057cda01cfd422c6bab3667b76426529382c23f42b9b08d7832d4fee1d6b437a8526e59667ce9c4e9dcebcabb")

    # 第三条是OP_DUP操作 复制栈顶元素
    stack.append("042e930f39ba62c6534ee98ed20ca98959d34aa9e057cda01cfd422c6bab3667b76426529382c23f42b9b08d7832d4fee1d6b437a8526e59667ce9c4e9dcebcabb")

    # 第四条是OP_HASH160操作， 对栈顶元素进行HASH160,就是先sha256再rmd160
    print(hash160(stack[-1]))
    stack[-1] = hash160(stack[-1])

    # 第五条是数据 直接入栈
    stack.append("46af3fb481837fadbb421727f9959c2d32a36829")

    # 接下来执行 OP_EQUALVERIFY 发现栈顶的元素相等 于是继续执行
    if stack[-1] == stack[-2]:
        stack = stack[:-2]
    else:
        return
    # 然后执行 OP_CHECKSIG 栈顶的两个元素 第一个被看做公钥 第二个被看做签名 如果验证成功存入1 否则存入0
    print('公钥', stack[-1])  # 公钥
    print('签名', stack[-2])  # 签名
    pub_key = VerifyingKey.from_string(bytes.fromhex("2e930f39ba62c6534ee98ed20ca98959d34aa9e057cda01cfd422c6bab3667b76426529382c23f42b9b08d7832d4fee1d6b437a8526e59667ce9c4e9dcebcabb"), curve=SECP256k1)
    try:
        pub_key.verify_digest(bytes.fromhex("30450221009908144ca6539e09512b9295c8a27050d478fbb96f8addbc3d075544dc41328702201aa528be2b907d316d2da068dd9eb1e23243d97e444d59290d2fddf25269ee0e"), hash_text,  sigdecode=ecdsa.util.sigdecode_der)
        print("验证通过")
    except Exception:
        print("验证不通过")

if __name__ == '__main__':
    verify()


