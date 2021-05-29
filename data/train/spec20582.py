import numpy as np 

def function(x):

	a4 = 6
	x6 = 7
	paths = []
	try:
		if x6 <= 7:
			a4 = 3*a4
			a4 = a4+a4
			paths.append(1)
		else:
			a4 = 3-0
			a4 = a4*a4
			x = 9-5
			paths.append(2)
		if x < 7:
			x = x-x6
			paths.append(3)
		else:
			x6 = x6-6
			x6 = x6-4
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))