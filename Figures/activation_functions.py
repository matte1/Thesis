from matplotlib import pyplot as plt
import numpy as np
import math

def relu(x):
    return max(0, x)

def tanh(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

def sigmoid(x):
    return 1./(1. + math.exp(-x))

x = np.linspace(-10,10,1e3, dtype=float)

plt.plot(x, np.array(list(map(relu, x))), label='ReLu')
plt.legend()
plt.grid()
plt.savefig('Relu')
plt.clf()

plt.plot(x, np.array(list(map(tanh, x))), label='Tanh')
plt.legend()
plt.grid()
plt.savefig('Tanh')
plt.clf()

plt.plot(x, np.array(list(map(sigmoid, x))), label='Sigmoid')
plt.legend()
plt.grid()
plt.savefig('Sigmoid')
plt.clf()

print((np.random.randn(6,6)+1)*5)
