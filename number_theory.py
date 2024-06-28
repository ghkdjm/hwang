#두 수의 최대공약수
def gcd(a, b):
    while b: a, b = b, a%b
    return a

#두 수의 최소공배수
def lcm(a, b):
    return a*b//gcd(a, b)

#최대공배수
def gcds(nums):
    result = nums[0]
    for num in nums[1:]:
        result = gcd(num, result)
    return result

#최소공배수
def lcms(nums):
    result = nums[0]
    for num in nums[1:]:
        result = lcm(num, result)
    return result

#소인수
def prime_factor(n):
    result = []
    for i in range(2,int(n**0.5)+1):
        while n % i == 0:
            result.append(i)
            n //= i
    if n != 1: result.append(n)
    return result

#소인수분해
def prime_factorization(n):
    lst = []
    dict = {}
    for i in prime_factor(n):
        if i in dict: dict[i] += 1
        else: dict[i] = 1
    for i in dict:
        lst.append(f"({i}^{dict[i]})")
    result = "*".join(lst)
    return result

#오일러 피함수
def phi(m):
    result = m
    for num in set(prime_factor(m)):
        result *= (num-1)
        result //= num
    return result

#약수
def factor(n):
    result = []
    for i in range(2,n+1):
        if n % i == 0:
            result.append(i)
    return result

#위수
def order(a, m):
    if gcd(a, m) != 1: return None
    for i in factor(phi(m)):
        if pow(a, i, m) == 1:       #pow(a, i, m) : (a**i) % m
            return i

#a^b 위수
def orders(a, b, m):
    r = order(a, m)
    return r//gcd(b, r)

#기약잉여계
def reduced_residue_system(m):
    result = []
    for i in range(1,m):
        if gcd(i, m) == 1: result.append(i)
    return result

#원시근
def primitive_root(m):
    #원시근이 존재할 조건
    def check(m):
        if m in [2, 4]: return True
        elif set(prime_factor(m)) == {2}: return False
        elif len(set(prime_factor(m))) == 1: return True
        elif m % 2 == 0 and len(set(prime_factor(m//2))) == 1: return True
        else: return False
    if check(m) == False: return None
    result = []
    for i in reduced_residue_system(m):
        if order(i, m) == phi(m):
            result.append(i)
    return result

#이차잉여
def quadratic_residue(m):
    result = set()
    for i in reduced_residue_system(m):
        result.add(pow(i, 2, m))
    return result

print(quadratic_residue(11
                        ))