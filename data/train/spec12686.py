import numpy as np 

def function(x):

	e5 = 6
	k3 = x
	paths = []
	try:
		if k3 >= 3:
			x = 6+k3
			e5 = e5*4
			x = x*e5
			paths.append(1)
		else:
			e5 = 1*e5
			k3 = 2/x
			e5 = e5/x
			paths.append(2)
		if e5 < 7:
			k3 = 3/1
			paths.append(3)
		else:
			e5 = e5/k3
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