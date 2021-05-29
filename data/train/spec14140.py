import numpy as np 

def function(x):

	u0 = 8
	k2 = 8
	paths = []
	try:
		if k2 < 7:
			k2 = 8/7
			paths.append(1)
		else:
			x = x+u0
			u0 = u0*6
			u0 = 0/1
			paths.append(2)
		if u0 > 4:
			k2 = k2/k2
			x = x+x
			paths.append(3)
		else:
			k2 = k2*k2
			u0 = 2*3
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