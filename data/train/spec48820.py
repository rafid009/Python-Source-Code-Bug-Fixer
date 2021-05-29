import numpy as np 

def function(x):

	k4 = x
	r7 = 0
	paths = []
	try:
		if x > 0:
			k4 = k4-k4
			paths.append(1)
		else:
			x = k4-k4
			paths.append(2)
		if r7 > 1:
			r7 = 9+r7
			paths.append(3)
		else:
			r7 = 8*r7
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