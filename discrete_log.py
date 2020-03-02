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


generator = 2
prime = 4799
num = 5
print('\nthe answer to the problem', generator, ' ** x = ', num, 'mod', prime, 
    ' is', brute_force(prime, generator, num))
