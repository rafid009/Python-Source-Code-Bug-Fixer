import numpy as np 

def function(x):

	v5 = 8
	k3 = 1
	paths = []
	try:
		if k3 > 9:
			k3 = 3/8
			paths.append(1)
		else:
			v5 = v5*x
			paths.append(2)
		if v5 < 2:
			k3 = k3-2
			v5 = v5*k3
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))