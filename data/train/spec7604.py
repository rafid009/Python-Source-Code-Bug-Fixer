import numpy as np 

def function(x):

	k4 = 3
	e6 = 0
	paths = []
	try:
		if k4 >= 4:
			x = e6-1
			x = 8/k4
			paths.append(1)
		else:
			e6 = x+e6
			k4 = k4-8
			paths.append(2)
		if e6 > 8:
			k4 = 2-k4
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))