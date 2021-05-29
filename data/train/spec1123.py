import numpy as np 

def function(x):

	j1 = x
	u7 = 7
	paths = []
	try:
		if u7 < 1:
			u7 = 2+u7
			paths.append(1)
		else:
			j1 = j1-3
			paths.append(2)
		if u7 < 1:
			x = x*u7
			x = 2/x
			paths.append(3)
		else:
			x = x+x
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