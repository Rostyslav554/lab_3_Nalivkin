import math

def gauss_function(x, mu, sigma):
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    e = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return a * e

x = float(input("Введіть значення x: "))
mu = float(input("Введіть значення μ : "))
sigma = float(input("Введіть значення σ : "))

result = gauss_function(x, mu, sigma)
print("Значення функції Гауса для x = "+str(x)+" "+"становить"+" "+ str(result))
