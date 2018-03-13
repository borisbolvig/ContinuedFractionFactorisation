#!/bin/env python
from math import sqrt
from fractions import gcd
from collections import defaultdict

class partial_quotients: #, number=10, printout=True, pell_sol=False, print_mod=False):

    def __init__(self, N, steps=0):

        # Check if N is square, don't bother.
        if sqrt(N) == int(sqrt(N)):
            self.isSquare = True
        else:
            self.isSquare = False
        self.N = N
        self.part_quotns = []
        self.rs = []
        self.ss = []
        self.P = [0, 1]
        self.Q = [1, 0]

        self.Pells = []
        self.neg_pell_sol = False
        self.continue_fraction(steps=steps)

    def continue_fraction(self, steps=100, savemode=True):

        a_0 = sqrt(self.N)
        # Check if N is square, otherwise take floor of the square root.
        if a_0==int(a_0):
            # print "N = {}^2".format(a_0)
            return None
        else:
            self.a_0 = int(a_0)
        if self.rs == []:
            # Set initial conditions x = (0 + sqrt(N)) / 1
            r = 0
            s = 1
            q_n = -self.N
        else:
            # Carry on where we left
            r = self.rs[-1]
            s = self.ss[-1]
            q_n = -self.ss[-2]  # Fails if exactly 1 iteration has been run in previous call.
            a_n = self.part_quotns[-1]

        result = set()
        Psqr = defaultdict(set)
        factors = set()
        for _ in range(steps):
            # find partial quotient from r, s
            if ((r+self.a_0)>0)==(s>0):  # integer division only works if same sign.
                a_n = (r+self.a_0) / s  # this does integer division with remainder, returns divisor.
            else:
                a_n = -(-(r + self.a_0) / s)

            # Now update r, s, q
            s_next = 2 * a_n * r - s * a_n ** 2 - q_n  # still need old s to update r and q.
            r = a_n * s - r
            q_n = -s
            s = s_next

            self.rs.append(r)
            self.ss.append(s)
            if savemode:
                # Here we save it all (can get memory heavy)
                self.part_quotns.append(a_n)
                # Update convergents
                self.P.append(a_n * self.P[-1] + self.P[-2])
                self.Q.append(a_n * self.Q[-1] + self.Q[-2])
            else:
                # Here we only save the last ones in case we need to take up the iteration again
                self.part_quotns = [a_n]
                if len(self.ss)>2:
                    self.ss.pop(0)
                    self.rs.pop(0)
                P = (a_n * self.P[-1] % self.N + self.P[-2] % self.N) % self.N
                # P = (a_n * self.P[-1] + self.P[-2])
                self.P.append(P)
                P2 = P**2 % self.N
                if P2 in Psqr and P not in Psqr[P2]:
                    print "iteration number {}".format(_)
                    for PP in Psqr[P2]:
                        f = gcd(N, P + PP)
                        if f != 1:
                            print f
                            factors.add(f)
                        if P != PP:
                            fs = gcd(N, abs(P - PP))
                            if f != 1:
                                print f
                                factors.add(f)
                Psqr[P2].add(P)
                self.P.pop(0)

        return list(factors)  # returns empty list for savemode, but that doesn't really matter.


    def compute_Pells(self):

        self.Pell_solutions = set()
        for i in range(len(self.P)):
            Pell = self.P[i]**2 - self.N * self.Q[i]**2
            self.Pells.append(Pell)
            if BigPell(-1, self.P[i], self.Q[i], self.N):
                # sanity check:
                assert Pell == -1
                self.neg_pell_sol = True
            if BigPell(1, self.P[i], self.Q[i], self.N):
                self.Pell_solutions.add((self.P[i], self.Q[i]))
        self.Pell_solutions.remove((1, 0))

    # mod_sols = set()
    # if (P[-1]**2-Q[-1]**2) % N == 0:
    #     mod_sols.add((P[-1], Q[-1]))
    #
    # if print_mod:
    #     for sol in mod_sols:
    #         print sol, sol[0]-sol[1]


    def max_rs(self):

        if self.rs == []:
            self.continue_fraction()
        return max(self.rs), max(self.ss)


    def neg_pell_soluble(self):

        if self.Pells == []:
            self.compute_Pells()
        return self.neg_pell_sol

def BigPell(val, x, y, N):
    # 1e40+2 < 6733663 * 886741 * 77849 * 6841 * 907 * 4489103 * 591161 * 51899
    Ps = [6733663, 886741, 77849, 6841, 907, 4489103, 591161, 51899]
    Pells = []
    for p in Ps:
        if val != (x % p) ** 2 - (N % p) * (y % p) ** 2:
            return False
    return True


def Q2_rs_bound(N_pqs):

    print "SQRT({1}): {}, 2*SQRT({1}): {}".format(N_pqs.N, sqrt(N_pqs.N), 2*sqrt(N_pqs.N))
    rmax, smax = N_pqs.max_rs()
    print "r_max: {}, s_max: {}".format(rmax, smax)
    print "Relatively: {}, {}".format(rmax/sqrt(N), smax/sqrt(N))


def Q2(Ns):
    # Question 2
    for Npq in Ns:
        print "Here comes the square root of %d" % N
        for i in range(len(Npq.part_quotns)):
            print "a_n: {}, r: {}, s: {}".format(Npq.part_quotns[i], Npq.rs[i], Npq.ss[i])
        print "Investigating how big r, s becomes in terms of SQRT(N):"
        rmax, smax = Npq.max_rs()
        print(sqrt(Npq.N), 2*sqrt(Npq.N))
        print((rmax, smax))
        print((rmax/sqrt(Npq.N), smax/sqrt(Npq.N)))

def Q3(Ns):
    # Question 3
    for Npq in Ns:
        if Npq.Pells == []:
            Npq.compute_Pells()
        print "Here come the Pell values of N = {}".format(Npq.N)
        for p in Npq.Pells:
            print p

    # Investigate insoluble neg_pell:
    print "\nThese are the N for which a solution to neg Pells eq. was found:"
    print "N,  (mod 3)"
    for Npq in Ns:
        if Npq.neg_pell_soluble():
            print Npq.N, Npq.N % 3

    print "\nThese are the solutions found for Pells equation:"
    for Npq in Ns:
        if not Npq.Pell_solutions == set():
            print "N = {}".format(Npq.N)
            for sol in Npq.Pell_solutions:
                print sol

def my_gcd(a, b):
    x, y = a, b
    while y:
        x, y = y, x%y
    return x

def find_factor(N, steps=100):
    Npq = partial_quotients(N, steps=0)
    factors = Npq.continue_fraction(steps=steps, savemode=False)
    while factors == []:
        print "No candidates found from continued fraction"
        factors = Npq.continue_fraction(steps=steps, savemode=False)
    return list(factors)

if __name__=="__main__":

    # Ns = []
    # for N in range(1,51):
    #     Npq = partial_quotients(N, steps=100)
    #     if not Npq.isSquare:  # this is in case N is square
    #         Ns.append(Npq)

    # Q2(Ns)
    # Q3(Ns)

    # N = 4994306101
    # N = 2181933577
    N = 3760842719
    # N = 51783
    print find_factor(N, steps=20000)

