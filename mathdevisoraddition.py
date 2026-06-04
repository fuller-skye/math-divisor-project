import math
import matplotlib.pyplot as plt



def get_divisors(n):
    """Return a sorted list and sum of all divisors of n."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    
    return sorted(divisors)

def perfect_number(n):
    """Check if n is a perfect number."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    divisors = get_divisors(n)
    sum_of_divisors = sum(divisors) - n  # Exclude n itself
    return sum_of_divisors == n


def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    """Find the divisors and their sum for future testing."""
    for n in range(1, 100):
        try:
            divisors = get_divisors(n)
            Div = (f"\nDivisors of {n}: {divisors}")
            AddDiv = (f"Sum:   {sum(divisors)}\n")   
            print(Div)
            print(AddDiv)
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            
def difference():
    """Calculate the difference between the sum of divisors and the number itself."""
    for i in range(1, 100):
        try:
            divisors = get_divisors(i)
            sum_divisors = sum(divisors)
            diff = sum_divisors - (2 * i)
            num = (f"Difference for {i}: {diff}")
            print(num)
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            
def plot_difference():
    """Plot the difference between the sum of divisors and the number itself."""
    x = []
    y = []
    for i in range(1, 100):
        try:
            divisors = get_divisors(i)
            sum_divisors = sum(divisors)
            diff = (sum_divisors - (2 * i))
            x.append(i)
            y.append(diff)
        except ValueError as e:
            print(f"Invalid input: {e}\n")


def diff_comp():
    """the difference in comparison to how large the original number is"""
    for i in range(1,100):
        try:
            original = i
            divisors = get_divisors(i)
            sum_divisors = sum(divisors)
            diff = abs(sum_divisors - (2 * i))
            diff_comp = (diff/original)
            print(diff_comp)
        except ValueError as e:
            print(f"Invalid input: {e}\n")

def plot_diffcomp():
    """plot the comparitive difference against the original intiger"""
    u = []
    v = []
    for i in range(1, 100):
        try:
            original = i
            divisors = get_divisors(i)
            sum_divisors = sum(divisors)
            diff = abs(sum_divisors - (2 * i))
            diff_comp = (diff/original)
            u.append(i)
            v.append(diff_comp)
        except ValueError as e:
            print(f"Invalid input: {e}\n")
    
    plt.scatter(u, v)
    plt.xlabel("Number")
    plt.ylabel("Comparitive Difference")
    plt.title("Comparitive Divisor Sum vs Number")
    plt.show()


if __name__ == "__main__":
    plot_difference()
