from math import sqrt
from Erastothenes import gen_primes

def factors(N):
    factors = []
    n = N
    for p in gen_primes():
        if p<=sqrt(N):
            while n%p == 0:
                factors.append(p)
                n /= p
                if n == 1:
                    break
        else:
            factors.append(n)
            break
    return factors, n, N, p

if __name__=="__main__":
    #N = 4994306101
    #N = 2181933577
    N = 3760842719
    # N = 51783
    print factors(N)