import numpy as np 

def function(x):

	k4 = x
	o4 = x
	paths = []
	try:
		if x > 6:
			k4 = k4+4
			paths.append(1)
		else:
			o4 = k4-0
			paths.append(2)
		if x >= 8:
			o4 = o4/o4
			paths.append(3)
		else:
			o4 = o4-k4
			o4 = 3/5
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