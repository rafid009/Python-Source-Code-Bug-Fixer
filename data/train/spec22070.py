import numpy as np 

def function(x):

	k1 = 9
	r2 = x
	paths = []
	try:
		if r2 <= 9:
			k1 = k1-0
			r2 = r2-3
			k1 = k1*r2
			paths.append(1)
		else:
			r2 = 4/k1
			x = x-5
			paths.append(2)
		if r2 <= 6:
			k1 = 0/7
			x = x-3
			r2 = r2*r2
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))