import matplotlib.pyplot as plt

def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = [p for p in range(2, n + 1) if prime[p]]  
    return primes

n = int(input("Enter the rightmost limit: "))

primes = sieve_of_eratosthenes(n)
print(f"Prime numbers up to {n}: {primes}")

plt.scatter(range(1, len(primes) + 1), primes, color='blue', s=100, marker='o')
plt.title('Prime Numbers')
plt.xlabel('Index')
plt.ylabel('Prime Numbers')

plt.show()
