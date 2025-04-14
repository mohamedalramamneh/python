import random
import math

def calculate_standard_deviation(N):
    # Generate N random numbers between 1 and 100
    numbers = [random.randint(1, 100) for _ in range(N)]
    
    # Calculate the mean of the numbers
    mean = sum(numbers) / N
    
    # Calculate the variance
    variance = sum((x - mean) ** 2 for x in numbers) / N
    
    # Calculate the standard deviation
    standard_deviation = math.sqrt(variance)
    
    # Output results in the desired format with detailed calculations
    print(f"Concept                        Value                         Symbol or formula                      Calculation")
    print("-" * 100)
    
    print(f"Standard deviation)   {standard_deviation:.3f}    σ = √σ²                             √{variance:.3f}")
    print(f"Variance               = {variance:.3f}    σ² = Σ(xᵢ - μ)² / N                    Sum of squared differences divided by N")
    
    return standard_deviation

# Example usage
if __name__ == "__main__":
    N = int(input("Enter N= "))
    std_dev = calculate_standard_deviation(N)
