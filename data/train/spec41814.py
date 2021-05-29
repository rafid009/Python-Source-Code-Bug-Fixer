import numpy as np 

def function(x):

	k4 = x
	a9 = 5
	x = x
	paths = []
	try:
		if k4 < 2:
			a9 = a9-x
			a9 = a9+7
			k4 = k4*3
			paths.append(1)
		else:
			x = 2-6
			x = x*x
			a9 = 6*0
			paths.append(2)
		if x >= 8:
			a9 = a9-8
			paths.append(3)
		else:
			x = x*k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		a9 = k4**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))