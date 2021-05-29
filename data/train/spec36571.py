import numpy as np 

def function(x):

	k4 = x
	k1 = x
	paths = []
	try:
		if k4 <= 2:
			x = x/2
			k4 = k4/1
			k1 = k1/7
			paths.append(1)
		else:
			x = 5/7
			paths.append(2)
		if k1 >= 3:
			k1 = k1-x
			k4 = k4-5
			paths.append(3)
		else:
			x = x+6
			x = 3*x
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