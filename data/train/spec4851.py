import numpy as np 

def function(x):

	e6 = x
	k3 = 3
	paths = []
	try:
		if e6 < 9:
			e6 = e6+8
			x = e6*7
			e6 = e6/1
			paths.append(1)
		else:
			k3 = 7*k3
			k3 = k3/8
			paths.append(2)
		if e6 <= 6:
			e6 = e6-1
			paths.append(3)
		else:
			x = x-0
			k3 = 2-k3
			k3 = k3/k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))