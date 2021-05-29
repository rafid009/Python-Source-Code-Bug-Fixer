import numpy as np 

def function(x):

	r2 = 3
	k5 = 5
	paths = []
	try:
		if k5 <= 4:
			k5 = k5/3
			k5 = 7-k5
			paths.append(1)
		else:
			r2 = 0+r2
			k5 = 0*k5
			r2 = r2*6
			paths.append(2)
		if x <= 8:
			k5 = 7/6
			k5 = 9*k5
			paths.append(3)
		else:
			x = x*r2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))