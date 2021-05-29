import numpy as np 

def function(x):

	k1 = 8
	u0 = x
	paths = []
	try:
		if u0 < 2:
			x = x+u0
			x = x-k1
			x = 3*x
			paths.append(1)
		else:
			u0 = 3/x
			k1 = k1/6
			paths.append(2)
		if u0 < 4:
			x = 5*k1
			paths.append(3)
		else:
			k1 = 2+k1
			x = x/7
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))