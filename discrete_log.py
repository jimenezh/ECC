from math import floor


def brute_force(prime, generator, number):
    """
    initial problem: find x s.t. generator ** x == number (mod prime)
    brute force approach is to exponentiate the generator 
    then check if equal to number

    Solves the discrete log problem in exponential time i.e. O(2**k) where
    k is the number of bits in the number
    """

    number_mod_prime = number % prime
    x = 0
    while True:
        
        exp_gen = generator ** x # exponentiating generator
        # print(generator, 'to the', x, 'is', exp_gen % prime)
    
        if exp_gen % prime == number_mod_prime: # checking if equal
            return x # returning x if equal
        
        x += 1 # otherwise we try the next biggest value for x

def collision_alg(prime, generator, number):
    """

        Creates two lists: one of powers of generator and one of the number
        multiplied by powers of generator's inverse
        Do this n times s.t. n = 1 + floor(sqrt(N)) where N is the order of
        the generator 

        Then find the one element in both lists

        N is equal to prime (i.e. Z_7 has 7 elements {0, 1,...,6})
    """
    # find order of n
    order = prime-1
    # find n
    n = 1 + floor(  order ** 0.5 )

    # find inverse of gen
    g_inv = find_inv(generator, prime)

    # initialize dictionary
    gen_list = {}

    # initializing runner vals
    curr_gen = 1
    curr_g_inv = 1

    # exponentiations of generator 
    for i in range(n+1):
        index = (curr_gen ) % prime # index is the generator exponentiation
        gen_list[index] = i # this index is part of the answer
        curr_gen = index* generator

    for i in range(n+1):
        cand =  (number * curr_g_inv) % prime
        if cand in gen_list: # checking for collision
            return gen_list[cand]+i # answer is sum of exponents
        curr_g_inv = (curr_g_inv * g_inv) % prime

    
def find_inv(g, p):
    # print('here')
    return pow(g, p-2, p)


def main():
    prime = int(input('Pick a prime: '))
    generator = int(input('Pick a generator: '))
    num = int(input('Pick an arbitrary number: '))
    a0 = collision_alg(prime, generator, num)
    a1 = brute_force(prime, generator, num)

    print('\n\n\nSolving', generator, '^ x =', num, 'mod', prime)
    print('Answer using brute force', a1, '\nAnswer using collision', a0)

    print('Checking:', pow(generator, a0, prime) == num,pow(generator, a1, prime) == num)

main()