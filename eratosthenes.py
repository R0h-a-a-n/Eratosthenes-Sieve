import matplotlib.pyplot as plt
import numpy as np
import time

def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primes = [p for p in range(2, n + 1) if prime[p]]  
    return primes

n = int(input("Enter the rightmost limit: "))
start_time = time.time()
primes = sieve_of_eratosthenes(n)
end_time = time.time()

print(f"Prime numbers up to {n}: {primes}")
print(f"Execution time: {end_time - start_time:.5f} seconds")

x = np.arange(1, len(primes) + 1)
y = primes
colors = np.linspace(0.1, 1, len(primes))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(x, y, c=colors, cmap='viridis', s=100, edgecolor='black')
plt.title('Prime Numbers Distribution')
plt.xlabel('Index')
plt.ylabel('Prime Numbers')

plt.subplot(1, 2, 2)
plt.hist(primes, bins=20, color='skyblue', edgecolor='black')
plt.title('Prime Numbers Histogram')
plt.xlabel('Prime Number')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
