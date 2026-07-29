import math
import matplotlib.pyplot as plt
import numpy as np



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
    for n in range(1, 1000):
        try:
            divisors = get_divisors(n)
            Div = (f"\nDivisors of {n}: {divisors}")
            AddDiv = (f"Sum:   {sum(divisors)}\n")   
            print(Div)
            print(AddDiv)
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            
def difference(n=None):
    """Calculate the difference between the sum of divisors and the number itself."""
    if n is None:
        for i in range(1, 1000):
            try:
                divisors = get_divisors(i)
                sum_divisors = sum(divisors)
                diff = sum_divisors - (2 * i)
                print(f"Difference for {i}: {diff}")
            except ValueError as e:
                print(f"Invalid input: {e}\n")
        return None

    try:
        divisors = get_divisors(n)
        sum_divisors = sum(divisors)
        return sum_divisors - (2 * n)
    except ValueError as e:
        print(f"Invalid input: {e}\n")
        return None

def plot_difference():
    """Plot the difference between the sum of divisors and the number itself."""
    x = []
    y = []
    for i in range(1, 1000):
        try:
            divisors = get_divisors(i)
            sum_divisors = sum(divisors)
            diff = abs(sum_divisors - (2 * i))
            x.append(i)
            y.append(diff)
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            
    coefficients1 = np.polyfit(x, y, 1)
    linear_function = np.poly1d(coefficients1)
    coefficients2 = np.polyfit(x, np.log(y), 1)
    a = np.exp(coefficients2[1])
    b = coefficients2[0]
    exp_function = lambda x: a * np.exp(b * np.array(x))
    
    plt.scatter(x, y, color="#7CB342", alpha=0.6, s=40)
    plt.plot(x, linear_function(x), color="#2E7D32", linestyle="-", linewidth=2, label="Trendline")
    plt.plot(x, exp_function(x), color="#1B5E20", linestyle="--", linewidth=2, label="Exponential Trendline")
    plt.xlabel("Number")
    plt.ylabel("Difference")
    plt.title("Divisor Sum vs Number")
    plt.show()
    plt.legend()


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
    x = []
    y = []
    for i in range(1, 1000):
        try:
            if is_prime(i):
                original = i
                divisors = get_divisors(i)
                sum_divisors = sum(divisors)
                diff = abs(sum_divisors - (2 * i))
                diff_comp = (diff/original)
                x.append(i)
                y.append(diff_comp)
        except ValueError as e:
            print(f"Invalid input: {e}\n")
            
    coefficients1 = np.polyfit(x, y, 1)
    linear_function = np.poly1d(coefficients1)
    coefficients2 = np.polyfit(x, np.log(y), 1)
    a = np.exp(coefficients2[1])
    b = coefficients2[0]
    exp_function = lambda x: a * np.exp(b * np.array(x))
    
    plt.scatter(x, y, color="#8E24AA", alpha=0.6, s=40)
    plt.plot(x, linear_function(x), color="#6A1B9A", linestyle="-", linewidth=2, label="Trendline")
    plt.plot(x, exp_function(x), color="#4A148C", linestyle="--", linewidth=2, label="Exponential Trendline")
    plt.xlabel("Number")
    plt.ylabel("Difference")
    plt.title("Divisor Sum vs Number for prime numbers")
    plt.show()
    plt.legend()


def plot_perfect_and_prime():
    """Plot perfect numbers and prime numbers with trendline analysis."""
    x_perfect = []
    y_perfect = []
    x_prime = []
    y_prime = []
    x_diff = []
    y_diff = []

    for i in range(2, 10000):
        divisors = get_divisors(i)
        sum_divisors = sum(divisors)
        diff_value = difference(i)
        
        if perfect_number(i):
            x_perfect.append(i)
            y_perfect.append(sum_divisors - i)
        
        if is_prime(i):
            x_prime.append(i)
            y_prime.append(sum_divisors - i)

        if diff_value is not None:
            x_diff.append(i)
            y_diff.append(diff_value)
    
    # Plot perfect numbers
    if x_perfect:
        plt.scatter(x_perfect, y_perfect, color="#333d29", alpha=0.7, s=25, label="Perfect Numbers")
        
        # Add trendline for perfect numbers, extending slightly past the last point
        coefficients = np.polyfit(x_perfect, y_perfect, 2)
        poly_function = np.poly1d(coefficients)
        x_end = max(x_perfect) + (max(x_perfect) - min(x_perfect)) * .23
        x_trend = np.linspace(min(x_perfect), x_end, 200)
        plt.plot(x_trend, poly_function(x_trend), color="#414833", linestyle="-", linewidth=2)
    
    # Plot primes
    if x_prime:
        plt.scatter(x_prime, y_prime, color="#656d4a", alpha=0.5, s=25, label="Prime Numbers")
        
        # Add trendline for primes
        coefficients = np.polyfit(x_prime, y_prime, 2)
        poly_function = np.poly1d(coefficients)
        x_trend = np.linspace(min(x_prime), max(x_prime), 100)
        plt.plot(x_trend, poly_function(x_trend), color="#a4ac86", linestyle="-", linewidth=2, label="Prime Trendline")

    # Plot differences
    if x_diff:
        plt.scatter(x_diff, y_diff, color="#a68a64", alpha=0.25, s=10, label="Differences")
        

        reference_x = np.linspace(min(x_diff), max(x_diff), 200)
        plt.plot(reference_x, -reference_x, color="#415d43", linestyle="-", linewidth=1, label="y = -x")
        plt.plot(reference_x, -reference_x / 2, color="#415d43", linestyle="-", linewidth=1, label="y = -x/2")
        plt.plot(reference_x, -(2 * reference_x) / 3, color="#415d43", linestyle="-", linewidth=1, label="y = -2x/3")
        plt.plot(reference_x, - reference_x / 4, color="#415d43", linestyle="-", linewidth=1, label="y = -x/4")
        plt.plot(reference_x, reference_x / 3, color="#415d43", linestyle="-", linewidth=1, label="y = x/3")
        #plt.plot(reference_x, -(3 * reference_x) / 4, color="#eab308", linestyle="--", linewidth=2, label="y = -3x/4")   - dosent match anything in data, not needed, but noted

    
    plt.xlabel("Number")
    plt.ylabel("Sum of Divisors - Number")
    plt.title("Perfect Numbers vs Prime Numbers with general data")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_perfect_and_prime()
    
