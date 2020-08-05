from tqdm import tqdm

class PrimeGenerator:
    """
    Generator of prime numbers.
    """
    def __init__(self):
        self.prime_nbs = []
        self.last_nb = 1
    
    def __repr__(self):
        repr = """
        Generator of prime numbers. Found prime numbers until {}.
        Below are the found prime numbers:
        """.format(self.last_nb)
        if len(self.prime_nbs) > 10:
            repr += "[" + \
                ", ".join([str(prime) for prime in self.prime_nbs[:5]]) + \
                ", ... , " + \
                ", ".join([str(prime) for prime in self.prime_nbs[-5:]]) + \
                "]"
        else:
           repr += "{}".format(self.prime_nbs)
        return repr

    def find_until(self, n, verbose=True):
        """Find prime numbers between self.last_number and n."""
        if n < self.last_nb:
            if verbose: print("All prime numbers have already been found below this value.")
        else:
            counter = 0
            for nb in tqdm(range(self.last_nb+1, n+1), disable=not(verbose)):
                prime = True
                for prime_nb in self.prime_nbs:
                    if nb % prime_nb == 0:
                        prime = False
                        break
                if prime:
                    self.prime_nbs.append(nb)
                    counter += 1
                self.last_nb += 1
            if verbose: print("Found {} new prime numbers!".format(counter))
    
    def is_prime(self, n, search=True, verbose=False):
        if n > self.last_nb:
            if search:
                self.find_until(n, verbose=verbose)
            else:
                ValueError("The generator hasn't searched for these prime numbers.")
        return n in self.prime_nbs

gen = PrimeGenerator()
assert gen.is_prime(7) == True
gen.find_until(10, verbose=False)
assert gen.prime_nbs == [2,3,5,7]
assert gen.is_prime(7) == True