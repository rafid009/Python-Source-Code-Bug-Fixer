import numpy as np 

def function(x):

	k4 = x
	l9 = 8
	paths = []
	try:
		if k4 < 8:
			l9 = l9+0
			paths.append(1)
		else:
			x = 8/2
			x = 0*3
			l9 = l9-l9
			paths.append(2)
		if k4 <= 2:
			x = 3/5
			paths.append(3)
		else:
			x = x-1
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