import number_theory.number_theory as nt
from hashlib import sha256

class Sender:
    def gen_session_key(self, p):
        self.k = nt.coprime_number(p-1)
        return self.k

    def encrypt(self, msg, p, g, y):
        encrypted_msg = []

        C1 = pow(g, self.k, p)   # a = g^k mod p
        coder = pow(y, self.k, p)    # b = y^k * M mod p  =>  temp = y^k mod p

        for i in range(0, len(msg)):
            encrypted_msg.append(msg[i])

        for i in range(0, len(encrypted_msg)):
            encrypted_msg[i] = coder * ord(encrypted_msg[i])

        self.C1 = C1
        self.C2 = ' '.join(str(s) for s in encrypted_msg)
        print("C1: ", self.C1)
        print("C2: ", self.C2)
        return self.C1, self.C2

    def gen_signature_keys(self):
        def get_a():
            for a in range(p-1, 2, -1):
                if pow(a, q, p) == 1:
                    return a

        # Public keys (p, q, a, v) and private key (s)
        p_bit = 32
        p = nt.random_prime(p_bit)
        print('p: ', p)

        q = nt.prime_factors(p-1)[-1]  # last prime factor
        print('q: ', q)

        a = get_a()
        print('a: ', a)

        s_bit = 18
        s = nt.nBit_random(s_bit)
        print('s: ', s)

        v = pow(a, q-s, p)      # or you can use pow(a, -s, p)
        print('v: ', v)

        self.p = p
        self.q = q
        self.a = a
        self.v = v
        self.__s = s

        return p, q, a, v, s

    def __preprocessing(self):
        print("Sender's prerocessing stage: ")
        self.r = nt.random_max(self.q-1)
        print('r: ', self.r)
        
        self.x = pow(self.a, self.r, self.p)
        print('x: ', self.x)

    def sign_up(self):
        self.__preprocessing()
        # (e, y) - signature
        encrypted_msg = str(self.C1) + ' ' + str(self.C2)
        signed_msg = (encrypted_msg + ' ' + str(self.x)).encode('utf-8')
        print('signed msg: ', signed_msg)

        e = int(sha256(signed_msg).hexdigest(), 16)
        print('e: ', e)

        y = (self.r + self.__s * e) % self.q
        print('y: ', y)

        return self.C1, self.C2, e, y