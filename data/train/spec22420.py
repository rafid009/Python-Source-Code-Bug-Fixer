import numpy as np 

def function(x):

	k6 = 3
	i0 = 8
	paths = []
	try:
		if x > 4:
			x = i0-5
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if i0 > 0:
			i0 = i0*k6
			i0 = i0-3
			paths.append(3)
		else:
			k6 = 4/k6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))