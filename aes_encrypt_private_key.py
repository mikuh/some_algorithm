from Crypto.Cipher import AES
import hashlib




def get_md5(password):
    md5 = hashlib.md5()
    md5.update((password + "gauss").encode('utf-8'))
    return md5.digest()



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




aesed = AESED(get_md5('asd098765'))
encrypt_private_key = 'e7517a776cad274a1b681729dab65470e034bc9cae709bfb56ae61e70862954d19f371b376d19a14403466f54b5f8ef0b574ae26330ad24b24dbc9ea195eb43bcb08fd77bbeb3488815ac43ad2c4e35c'
decode_private_key = aesed.decode(encrypt_private_key).decode('utf-8')

print(encrypt_private_key)
print(decode_private_key)
