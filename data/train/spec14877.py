import numpy as np 

def function(x):

	k6 = x
	x7 = 8
	x = 3
	paths = []
	try:
		if x7 > 0:
			k6 = x7/k6
			x7 = k6*7
			paths.append(1)
		else:
			x7 = 2/k6
			x7 = 2*x7
			x7 = k6-k6
			paths.append(2)
		if x < 6:
			k6 = 3-9
			k6 = k6*7
			paths.append(3)
		else:
			x = x7+x
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))