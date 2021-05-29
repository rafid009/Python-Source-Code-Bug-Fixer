import numpy as np 

def function(x):

	k1 = x
	k6 = 6
	paths = []
	try:
		if x >= 8:
			x = 9*x
			paths.append(1)
		else:
			k1 = k1-k6
			paths.append(2)
		if x < 9:
			k6 = k1+k6
			x = x+x
			paths.append(3)
		else:
			k6 = 4+k6
			k6 = 7*3
			x = x+5
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