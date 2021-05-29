import numpy as np 

def function(x):

	l2 = 2
	v2 = 2
	x = x
	paths = []
	try:
		if v2 < 5:
			x = l2+x
			l2 = l2/3
			x = x-3
			paths.append(1)
		else:
			l2 = l2-1
			paths.append(2)
		if v2 > 6:
			v2 = l2*v2
			paths.append(3)
		else:
			x = 6+x
			x = 9*x
			x = 7*x
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