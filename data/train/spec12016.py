import numpy as np 

def function(x):

	k5 = x
	h3 = x
	paths = []
	try:
		if h3 <= 2:
			x = x+3
			k5 = 8+h3
			paths.append(1)
		else:
			k5 = x-8
			paths.append(2)
		if x < 9:
			k5 = 2+h3
			x = x/3
			x = x/6
			paths.append(3)
		else:
			k5 = k5/h3
			x = 9+k5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))