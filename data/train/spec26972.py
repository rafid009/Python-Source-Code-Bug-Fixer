import numpy as np 

def function(x):

	l1 = x
	k2 = x
	x = x
	paths = []
	try:
		if x < 6:
			k2 = k2/x
			x = x+7
			l1 = x*l1
			paths.append(1)
		else:
			k2 = 3-5
			paths.append(2)
		if x <= 1:
			x = 1*x
			paths.append(3)
		else:
			k2 = k2*6
			k2 = k2-l1
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