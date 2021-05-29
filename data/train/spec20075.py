import numpy as np 

def function(x):

	h4 = x
	o8 = x
	paths = []
	try:
		if x < 5:
			x = x-6
			x = 7*6
			x = 7*x
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if h4 >= 9:
			x = 8+2
			paths.append(3)
		else:
			x = x+x
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))