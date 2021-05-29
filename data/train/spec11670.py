import numpy as np 

def function(x):

	x0 = 4
	l3 = x
	paths = []
	try:
		if x > 5:
			l3 = 9-l3
			x = 9+2
			x0 = 0-x0
			paths.append(1)
		else:
			l3 = l3-l3
			paths.append(2)
		if l3 < 2:
			l3 = l3-3
			x0 = x+7
			paths.append(3)
		else:
			l3 = 5-l3
			l3 = l3+0
			x0 = x0*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))