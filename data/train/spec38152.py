import numpy as np 

def function(x):

	k6 = x
	u0 = x
	x = x
	paths = []
	try:
		if u0 > 2:
			u0 = u0*4
			paths.append(1)
		else:
			x = k6+x
			x = 9+x
			u0 = x+4
			paths.append(2)
		if k6 >= 7:
			x = u0*6
			paths.append(3)
		else:
			u0 = 2*6
			u0 = 9*1
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))