import numpy as np 

def function(x):

	k7 = 2
	u0 = x
	paths = []
	try:
		if u0 > 0:
			k7 = 6+k7
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if u0 <= 7:
			u0 = u0+3
			k7 = 1*u0
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))