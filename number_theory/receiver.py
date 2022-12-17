import number_theory.number_theory as nt
from hashlib import sha256

class Receiver:
    def gen_encryption_keys(self):
        # Public keys (p, g, y) and private key (x)
        p_bit = 32
        p = nt.random_prime(p_bit)
        print('p: ', p)

        g = nt.primitive_root(p)
        print('g: ', g)

        x_bit = 18
        x = nt.random_prime(x_bit)
        print('x: ', x)

        y = pow(g, x, p)
        print('y: ', y)

        self.p_encryption = p
        self.g_encryption = g
        self.y_encryption = y
        self.__x_encryption = x

        return p, g, y, x

    def decrypt_msg(self):
        decrypted_msg = []

        temp = pow(self.C1, self.__x_encryption)
        mod_inverse = pow(temp, -1, self.p_encryption)
        self.C2  = [int(num) for num in self.C2.split(' ')]
        for i in range(0, len(self.C2)):
            decrypted_msg.append(chr(int((self.C2[i] * mod_inverse) % self.p_encryption)))

        return ''.join(decrypted_msg)

    def receive_msg(self, C1, C2, e, y):
        self.C1 = C1
        self.C2 = C2
        self.e_signature = e
        self.y_signature = y

    def check_signature(self, p, a, v):
        x_strich = (pow(a, self.y_signature, p) * pow(v, self.e_signature, p)) % p

        encrypted_msg = str(self.C1) + ' ' + str(self.C2)
        checked_msg = (encrypted_msg + ' ' + str(x_strich)).encode('utf-8')
        print('checked msg: ', checked_msg)

        e_strich = int(sha256(checked_msg).hexdigest(), 16)
        print('e: ', e_strich)

        if self.e_signature == e_strich:
            return True
        else:
            return False