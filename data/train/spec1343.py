import numpy as np 

def function(x):

	e7 = 6
	k1 = 7
	paths = []
	try:
		if k1 <= 2:
			k1 = 9-k1
			k1 = 7-k1
			e7 = 7+e7
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if k1 > 6:
			k1 = x*k1
			e7 = 4/e7
			paths.append(3)
		else:
			x = 7/x
			x = 6-3
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))