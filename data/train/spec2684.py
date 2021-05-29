import numpy as np 

def function(x):

	j1 = 0
	g3 = 3
	paths = []
	try:
		if j1 >= 2:
			g3 = g3/g3
			j1 = j1+7
			paths.append(1)
		else:
			x = 3/x
			paths.append(2)
		if g3 <= 4:
			j1 = j1*x
			paths.append(3)
		else:
			g3 = 5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))