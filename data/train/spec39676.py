import numpy as np 

def function(x):

	a2 = 4
	k1 = 2
	paths = []
	try:
		if x >= 7:
			k1 = 9+k1
			x = x-6
			k1 = k1/7
			paths.append(1)
		else:
			a2 = a2+0
			paths.append(2)
		if x > 3:
			a2 = 0+1
			x = x-k1
			paths.append(3)
		else:
			x = k1-8
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