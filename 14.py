# 14. Hill Climbing
def hill_climbing(f, x, step=0.1, iterations=1000):
    for _ in range(iterations):
        if f(x+step)>f(x): x+=step
        elif f(x-step)>f(x): x-=step
        else: break
    return x, f(x)

f = lambda x: -(x**2) + 4*x
x, val = hill_climbing(f, 0)
print(f"Hill Climbing: x={x:.2f}, f(x)={val:.2f}")