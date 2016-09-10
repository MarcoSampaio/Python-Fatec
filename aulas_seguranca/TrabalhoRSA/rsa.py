"""
Trabalho - Prof. Alexandre Garcia

Em um sistema de mensagens criptografadas usando o RSA, o n�mero N foi fatorado de alguma forma comprometendo totalmente a seguran�a do mesmo. 
Foi achado p e q (muitos d�gitos) primos de forma a fatorar N. 
Sabendo que expoente RSA e � conhecido, pois, � chave p�blica e considerando que tamb�m foi obtido a cifra c em hexa, sua tarefa � obter a mensagem m
para cada texto cifrado c.
As informa��es est�o todas em hexadecimal.

p=0x10000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000010d
q=0x100000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000139
e=0x10001
c=c501269d5a46f0c18883f030c595884254aeaf45897136aa7d1013ded7d16ac0f5c1a4f81e4af0e5fbc5455f486785ddc393daea457aa8e483c8a2d89ce1053f0ec20dab6c0e92d386b736124b51d9d65ba1f18ca9d84ed8bdb835b7141c03c5d19d05806f4d6476dc2a5f6054c22993552df11bf7f7a30e6e62086ebcfd5ab1

p=0x10000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000010d
q=0x100000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000139
e=0xb
c=65ca261bcd59aa660e42d51cd1a0042def9a006c5d56c1ba43e5f582bad29c1acf6c54f775bb731df37e296a686142c614f4133c6bb66d8c86175816810b64e617428aad974b3f3be44f6f9398e3a1e57605163276c6df768706161f29f81910cbfb9290690b83c7fbb1104afe4b93a7718927df0b9c9a9885848eca81a534a9

p=0x10000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000010d
q=0x100000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000139
e=0x10001
c=4744d4d36c9882db141c8a1e28b2ff924d285501cab5c4020d0abebdb61e7f9ac9eafd6692a4ce86877614cbc2c8c4e518c0853a0998ab597144c17048d18b419cf8912fc309a3d71b4db24f88ec638438c72a2dd67ca255afa8ccd3238f7b2c8dc07731ca011b1f09186a6902d0f3e2aa0eae50572a53ec2a59bec32b23f2c1

p=0x10000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000010d
q=0x100000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000139
e=0x29
c=3357c983b04e8c73871624a89dd2463965ce637415cee84c9b61c95ebb4960989d8cccfbe6d7207195ee0b2cef204bd58fe1b19b918459f0e6501b52d239a6279d7ae528e0300b84cc649625b4f427509e86d0f3471226308d275b8460e2355163a17c02a1e3e7741c475bbda2fa212b0eb0271681fdbbb86ab0fa0979e2e41f

p=0x10000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000010d
q=0x100000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000139
e=0x10001
c=c39fd568373351dbca90c198a56790bd007e1965ebd350252ee0521a59fe0bbc429272e86ae64b38c51de5aca051483f841e69b4d6816f8606f173428530ff4732242884b8c74eed757a07989f43a0dde2672848b018b3addd8bcf3061be89efa06dae56331f221422193635d7327a29741300315faba474e378ce251872bb1a
"""

import random
from collections import namedtuple


def get_primes(start, stop):
    """Return a list of prime numbers in ``range(start, stop)``."""
    if start >= stop:
        return []

    primes = [2]

    for n in range(3, stop + 1, 2):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)

    while primes and primes[0] < start:
        del primes[0]

    return primes


def are_relatively_prime(a, b):
    """Return ``True`` if ``a`` and ``b`` are two relatively prime numbers.

    Two numbers are relatively prime if they share no common factors,
    i.e. there is no integer (except 1) that divides both.
    """
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True


def make_key_pair(length):
    """Create a public-private key pair.

    The key pair is generated from two random prime numbers. The argument
    ``length`` specifies the bit length of the number ``n`` shared between
    the two keys: the higher, the better.
    """
    if length < 4:
        raise ValueError('cannot generate a key of length less '
                         'than 4 (got {!r})'.format(length))

    # First step: find a number ``n`` which is the product of two prime
    # numbers (``p`` and ``q``). ``n`` must have the number of bits specified
    # by ``length``, therefore it must be in ``range(n_min, n_max + 1)``.
    n_min = 1 << (length - 1)
    n_max = (1 << length) - 1

    # The key is stronger if ``p`` and ``q`` have similar bit length. We
    # choose two prime numbers in ``range(start, stop)`` so that the
    # difference of bit lengths is at most 2.
    start = 1 << (length // 2 - 1)
    stop = 1 << (length // 2 + 1)
    primes = get_primes(start, stop)

    # Now that we have a list of prime number candidates, randomly select
    # two so that their product is in ``range(n_min, n_max + 1)``.
    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_candidates = [q for q in primes
                        if n_min <= p * q <= n_max]
        if q_candidates:
            q = random.choice(q_candidates)
            break
    else:
        raise AssertionError("cannot find 'p' and 'q' for a key of "
                             "length={!r}".format(length))

    # Second step: choose a number ``e`` lower than ``(p - 1) * (q - 1)``
    # which shares no factors with ``(p - 1) * (q - 1)``.
    stop = (p - 1) * (q - 1)
    for e in range(3, stop, 2):
        if are_relatively_prime(e, stop):
            break
    else:
        raise AssertionError("cannot find 'e' with p={!r} "
                             "and q={!r}".format(p, q))

    # Third step: find ``d`` such that ``(d * e - 1)`` is divisible by
    # ``(p - 1) * (q - 1)``.
    for d in range(3, stop, 2):
        if d * e % stop == 1:
            break
    else:
        raise AssertionError("cannot find 'd' with p={!r}, q={!r} "
                             "and e={!r}".format(p, q, e))

    # That's all. We can build and return the public and private keys.
    return PublicKey(p * q, e), PrivateKey(p * q, d)


class PublicKey(namedtuple('PublicKey', 'n e')):
    """Public key which can be used to encrypt data."""

    __slots__ = ()

    def encrypt(self, x):
        """Encrypt the number ``x``.

        The result is a number which can be decrypted only using the
        private key.
        """
        return pow(x, self.e, self.n)


class PrivateKey(namedtuple('PrivateKey', 'n d')):
    """Private key which can be used both to decrypt data."""

    __slots__ = ()

    def decrypt(self, x):
        """Decrypt the number ``x``.

        The argument ``x`` must be the result of the ``encrypt`` method of
        the public key.
        """
        return pow(x, self.d, self.n)


if __name__ == '__main__':
    # Test with known results.
    public = PublicKey(n=2534665157, e=7)
    private = PrivateKey(n=2534665157, d=1810402843)

    assert public.encrypt(123) == 2463995467
    assert public.encrypt(456) == 2022084991
    assert public.encrypt(123456) == 1299565302

    assert private.decrypt(2463995467) == 123
    assert private.decrypt(2022084991) == 456
    assert private.decrypt(1299565302) == 123456

    # Test with random values.
    for length in range(4, 17):
        public, private = make_key_pair(length)

        assert public.n == private.n
        assert len(bin(public.n)) - 2 == length

        x = random.randrange(public.n - 2)
        y = public.encrypt(x)
        assert private.decrypt(y) == x

        assert public.encrypt(public.n - 1) == public.n - 1
        assert public.encrypt(public.n) == 0

        assert private.decrypt(public.n - 1) == public.n - 1
        assert private.decrypt(public.n) == 0

    import doctest
    doctest.testfile(__file__, globs=globals())