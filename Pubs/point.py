class Point:
    """A class of points in F_q x F_q.
    
    Takes as input 
    - components x and y
    - parameters q and d
    
    Specifies defaults for the paramters that apply
    in the case of Ed25519; and defaults for the components 
    that yield the generator for Ed25519. 

    Defines an attribute .doubles_seq that
    is not calculated when an instance is created.

    It is calculated only when the repeated addtion 
    method is first used. It is then saved so  doesn't 
    need to be calculated again. 

    The timing is important because the .doubles() method
    that calculates the list .doubles_seq has to create 255 
    additional curve points and it is important to avoid a
    situation where each time you create one curve point, 
    you create 255 additional curve points.

    Uncomment the print statement in self.doubles() to see a 
    notification each time .doubles.seq is calculated.

    The upper bound for the integers used to specify repeated 
    addition of a point is 2 raised to the power 512.
    In the application to Ed25519, this should be large enough 
    to handle calculation involving repeated addition.

    """
    def __init__(self, x, y, q, d): 
        self.x = x 
        self.y = y 
        self.q = q
        self.a = q-1
        self.d = d
        self.doubles_seq = []


    def __repr__(self):
        nl = "\n" + " " * 4
        if self.q > 2**254:
            return f"{self.__class__.__name__}({nl}{self.x}{nl}{self.y}\n)"
        else:
            s = f"{self.__class__.__name__}"
            s += f"(x={self.x}, y={self.y}, q={self.q}, d={self.d})"
            return s


    def __eq__(self, Other):
        if all(
            [
                isinstance(Other, type(self)),
                self.x == Other.x,
                self.y == Other.y,
                self.q == Other.q,
                self.d == Other.d,
            ]
        ):
            return True
        else:
            return False


    def __add__(self, Other):
        if all([ 
                isinstance(Other, type(self)),
                self.q == Other.q,
                self.d == Other.d,
            ]):
            N = self
            M = Other
            Dx = pow((1 + self.d * M.x * N.x * M.y * N.y), self.q - 2, self.q)
            x = (M.x * N.y + M.y * N.x) * Dx % self.q
            Dy = pow((1 - self.d * M.x * N.x * M.y * N.y), self.q - 2, self.q)
            y = (M.y * N.y + M.x * N.x) * Dy % self.q
            return Point(x=x, y=y, q=self.q, d=self.d)


    def __rmatmul__(self, m):
        br = self.br_from_int(m)
        if len(self.doubles_seq) == 0:
            self.doubles_seq = self.doubles()
        cp = Point(x=0, y=1, q=self.q, d=self.d)
        for b, p in zip(br, self.doubles_seq):
            if b:
                cp += p
        return cp

    
    @classmethod
    def valid_params(cls, q, a, d):
        """
        Confirm whether the parameters q, a and d yield
        an elliptic curve that is complete and not signular.
        """
        # Test whether q is prime only if q < 2**10.
        if q < 2**10:
            if not cls.is_prime(q):
                return False
        # For co-factor to be 8
        if q % 8 != 5:
            return False
        # To avoid singularity, need a != d, both != 0
        if a % q == 0 or d % q == 0 or a % q == d % q:
            return False
        # For completeness, d must be non-square in F_q
        if pow(d % q, (q - 1) // 2, q) != q - 1:
            return False
        # For completeness, a must be square in F_q
        if pow(a % q, (q - 1) // 2, q) == q - 1:
            return False
        return True


    @classmethod
    def is_prime(cls, n: int) -> bool:
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


    @classmethod 
    def Ed(cls, M):
        """The equation that defines the twisted Edwards elliptic curve for the 
        parameters M.q and M.d. The parameter that is often denoted as a is set 
        to -1.
        """
        return (-1 * M.x**2 + M.y**2 - 1 - M.d * M.x**2 * M.y**2) % M.q
            
    
    @classmethod
    def curve_points(cls, q, d):
        """For paramters q and d, returns the set of all curve points. Because 
        it could take impossibly long and could exhaust the available RAM, it 
        would be a mistake to run this method for large values of q.
        """
        points = []
        for x in range(q):
            for y in range(q):
                M = Point(x, y, q, d)
                if cls.Ed(M) == 0:
                    points.append(M)
        return points

    
    @staticmethod
    def br_from_int(m: int) -> list:
        """Used to calculate m repeated sums of a point with itself. 
        If m is too large, it will throw an error.
        """
        if m >= 2**512:
            raise TypeError("The integer supplied is too large.") 
        return [int(b) for b in list(bin(m)[2:])[::-1]]


    def doubles(self):
        """Another function that is used to calculate the repeated 
        sum of a point with itself.
        
        It uses repeated doubling to calculate a sequence 
        of terms of the form 2**2**r @ self. 

        You can uncomment the first line to see on the command 
        line when this function runs. It should run only once and
        only the first time that an expression of the form 
        m @ self is calculated.  
        """
        # print("Calculating the sequence of doubled points.")
        ls = []
        ls.append(self)
        for j in range(1, 512):
            ls.append(ls[-1] + ls[-1])
        self.doubles = ls
        return ls

    
    @classmethod
    def find_params(cls):
        """A function that searches for parameters q and d that are 
        valid and with the property that the large subgroup of curve points 
        has a cofator equal to 8.
        """
        
        for q in range(100, 200):
            for nd in range(2, 10):
                d = -nd % q
                a = -1 % q
                if not cls.valid_params(q, a, d):
                    continue
                n = len(cls.curve_points(q, d))
                if n % 8 == 0 and cls.is_prime(n // 8):
                    print(f"q={q}, d={q - nd}, #E={n}, cofactor=8, r={n // 8}")
                    break
