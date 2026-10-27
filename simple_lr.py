import matplotlib.pyplot as plt

class simple_rl:
    def moyenne(T):
        n = len(T)
        sum = 0
        for obs in T:
            sum += obs
        return sum/n
    
    def variance(T):
        squared = [x**2 for x in T]
        var = simple_rl.moyenne(squared) - simple_rl.moyenne(T)**2
        return var

    def covariance(X, Y):
        mul = [x*y for x,y in zip(X,Y)]
        cov = simple_rl.moyenne(mul) - simple_rl.moyenne(X)*simple_rl.moyenne(Y)
        return cov

    def tracer_droite(X, Y, a, b):
        plt.scatter(X, Y, color='darkorange', label='Data')

        prediction = [a * x + b for x in X]
        plt.plot(X, prediction, color='royalblue', linewidth=2, label=f'Regression Line (y = {a:.2f}x + {b:.2f})')

        plt.title("Linear Regression Fit")
        plt.xlabel("Independent Variable (X)")
        plt.ylabel("Dependent Variable (Y)")
        plt.legend()
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.show()

    def predire(x, a ,b):
        return a*x + b