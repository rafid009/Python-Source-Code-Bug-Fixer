import numpy as np 

def function(x):

	e8 = 2
	k3 = x
	paths = []
	try:
		if k3 <= 0:
			e8 = k3-3
			paths.append(1)
		else:
			e8 = k3+x
			e8 = 6+e8
			x = x*9
			paths.append(2)
		if k3 <= 6:
			x = x+0
			paths.append(3)
		else:
			e8 = e8+7
			k3 = 9-k3
			k3 = 5/k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))