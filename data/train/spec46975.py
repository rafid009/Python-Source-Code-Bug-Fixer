import numpy as np 

def function(x):

	k4 = x
	r3 = 3
	paths = []
	try:
		if k4 > 3:
			x = 9+r3
			k4 = 0-x
			k4 = k4-1
			paths.append(1)
		else:
			r3 = 6/r3
			paths.append(2)
		if k4 > 8:
			r3 = r3-4
			paths.append(3)
		else:
			r3 = x/1
			x = x-2
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))