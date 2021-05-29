import numpy as np 

def function(x):

	x6 = 9
	h3 = 3
	paths = []
	try:
		if x6 > 8:
			x6 = x*x6
			paths.append(1)
		else:
			h3 = 3-x6
			h3 = 5/h3
			paths.append(2)
		if x < 0:
			x = 7-7
			x = 8-0
			paths.append(3)
		else:
			x6 = x6-1
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))