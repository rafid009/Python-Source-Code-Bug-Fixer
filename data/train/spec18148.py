import numpy as np 

def function(x):

	k2 = x
	q4 = x
	paths = []
	try:
		if k2 <= 4:
			k2 = k2/x
			k2 = x-3
			paths.append(1)
		else:
			k2 = x*9
			paths.append(2)
		if q4 < 7:
			q4 = q4+2
			x = q4/x
			paths.append(3)
		else:
			q4 = 0-k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))