#2
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return x**2
def f2(x):
    return np.sqrt(x)
def f3(x):
    return -x**2
x_values = np.linspace(0.01, 10, 400)
x_values_neg = np.linspace(-10, -0.01, 400)
plt.figure(figsize=(10, 6))
plt.plot(x_values, f1(x_values), label='f(x) = f1(x)', color='blue')
plt.plot(x_values[:50], f1(x_values[:50]), linestyle='dashed', color='blue', label='Small x')
plt.plot(x_values[-50:], f1(x_values[-50:]), linestyle='dashed', color='blue', label='Large x')
plt.axhline(y=0, color='black', linestyle='--', label='f(x) = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График для x > 0')
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(x_values_neg, f3(x_values_neg), label='f(x) = f3(x)', color='red')
plt.plot(x_values_neg, f3(x_values_neg), linestyle='dashed', color='red', label='x -> -∞')
plt.axhline(y=0, color='black', linestyle='--', label='f(x) = 0')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График для x < 0')
plt.legend()
plt.grid(True)
plt.show()


#4
import numpy as np
import matplotlib.pyplot as plt
def plot_graph(alpha, beta, color, label):
    x = np.linspace(-5, 5, 100)
    y = alpha * x + beta
    plt.plot(x, y, color, label=label)
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plot_graph(1, 0, 'b--', label='α=1, β=0')
plot_graph(1, -1, 'r--', label='α=1, β=-1')
plot_graph(1, 0.5, 'g-', label='α=1, β=0.5')
plot_graph(1, 0.8, 'y-', label='α=1, β=0.8')
plt.title('График 1')
plt.legend()
plt.subplot(1, 3, 2)
plot_graph(1, 0, 'b--', label='α=1, β=0')
plot_graph(1, -1, 'r--', label='α=1, β=-1')
plot_graph(1, -0.5, 'g-', label='α=1, β=-0.5')
plot_graph(1, -0.8, 'y-', label='α=1, β=-0.8')
plt.title('График 2')
plt.legend()
plt.subplot(1, 3, 3)
plot_graph(1, 0, 'b--', label='α=1, β=0')
plot_graph(1, -1, 'r--', label='α=1, β=-1')
plot_graph(1, -1.5, 'g-', label='α=1, β=-1.5')
plot_graph(1, -2.5, 'y-', label='α=1, β=-2.5')
plt.title('График 3')
plt.legend()
plt.tight_layout()
plt.show()