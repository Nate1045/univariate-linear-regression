from simple_lr import simple_rl
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [40, 60, 70, 80, 100]
    y = [5.1, 6.7, 8.4, 8.7, 11.1]
    a = simple_rl.covariance(x, y) / simple_rl.variance(x)
    b = simple_rl.moyenne(y) - a * simple_rl.moyenne(x)
    print(f'The predicted price for an apartement of size 75 m² is {simple_rl.predire(75, a, b)}')
    print(f'The predicted price for an apartement of size 120 m² is {simple_rl.predire(120, a, b)}')
    simple_rl.tracer_droite(x, y, a, b)
