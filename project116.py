import pandas as pad


def model(x):
    return 1 / (1 + np.exp(-x))

X_test = np.linspace(0,100,200)
chances = model(X_test * lr.coef + lr.intercept.ravel())
plt.plot(X_test_chances,color,linewidth = 3)
plt.axhline(y=0,color = k,linestyle ='-')
plt.axhline(y=0,color = k,linestyle ='-')
plt.axhline(y=0,color = k,linestyle ='-')

plt.xlabel('X')
plt.ylabel('Y')
plt.show()




