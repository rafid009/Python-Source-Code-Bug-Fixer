import numpy as np 

def function(x):

	k1 = 8
	k2 = 1
	x = x
	paths = []
	try:
		if x >= 1:
			x = 1+x
			k1 = 3+k1
			x = x+k1
			paths.append(1)
		else:
			k2 = 2*k2
			paths.append(2)
		if x >= 4:
			x = k1*x
			k2 = 0/3
			paths.append(3)
		else:
			k1 = 2-k1
			k1 = 6+9
			k2 = k1*k2
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