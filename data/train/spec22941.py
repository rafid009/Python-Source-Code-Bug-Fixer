import numpy as np 

def function(x):

	k2 = x
	v1 = 0
	paths = []
	try:
		if v1 < 6:
			k2 = k2+v1
			v1 = 8*v1
			k2 = k2+x
			paths.append(1)
		else:
			k2 = k2-x
			paths.append(2)
		if x <= 0:
			k2 = x*7
			x = k2/x
			x = k2-3
			paths.append(3)
		else:
			k2 = 2/k2
			k2 = k2-k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))