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
    print('\n\n\nSolving', generator, '^ x =', number, 'mod', prime)
    # print('order is', order, 'so', generator,'^', order, 'is', generator ** order % prime)
    # print('n is', n, 'as floor', order**0.5)
    # find inverse of gen
    g_inv = find_inv(generator, prime)
    # print('\ninverse', g_inv, 'so', generator, '*', g_inv, 'is', generator*g_inv % prime)

    # initialize two lists
    gen_list = {}
    num_list = []
    
    # print('\ntaking gen', generator, 'and gen_inv', g_inv,'\n')

    curr_gen = 1
    curr_g_inv = 1
    l = []
    # exponentiations of generator 
    for i in range(n+1):
        index = (curr_gen ) % prime # index is the generator exponentiation
        gen_list[index] = i # this index is part of the answer
        curr_gen = index* generator
        l.append(index)
    print('exponentiations', gen_list, l)
    # num times exponentiations of gen_inv

    for i in range(n+1):
        cand =  (number * curr_g_inv) % prime
        print(number, '*', curr_g_inv % prime, pow(g_inv, i, prime),'=', cand)
        # print('possible collision is with', cand)
        num_list.append(cand)
        if cand in gen_list: # checking for collision
            print(cand, 'in dict at index', i, 'with', gen_list[cand], 'is', gen_list[cand]+i)
            # we know gen_list[cand] holds part of the answer
            print('generator', generator, '^', gen_list[cand]+i, 'is',
                generator **(gen_list[cand]+i) % prime, '=?', number)
            return gen_list[cand]+i
        curr_g_inv = (curr_g_inv * g_inv) % prime

    print('lists are:', l, num_list)

    

def find_order(n, p):
    i = 1
    while True:
        # print(n, i, (n ** i) % p)
        if (n ** i) % p == 1:
            return i
        i += 1
def find_inv(g, p):
    # print('here')
    return pow(g, p-2, p)

# print(find_order(2, 11))
# print(find_inv(3, 7))

generator = 3
prime = 11
num =4
# print('\nthe answer to the problem', generator, ' ** x = ', num, 'mod', prime, 
#     ' is', brute_force(prime, generator, num))
collision_alg(prime, generator, num)
