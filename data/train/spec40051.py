import numpy as np 

def function(x):

	k4 = 6
	k7 = 8
	paths = []
	try:
		if k7 < 8:
			k7 = k7+6
			x = x-5
			x = x+k4
			paths.append(1)
		else:
			x = x*k4
			paths.append(2)
		if x >= 2:
			x = 2*8
			paths.append(3)
		else:
			x = 1+x
			k7 = k7*4
			x = 2-k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))