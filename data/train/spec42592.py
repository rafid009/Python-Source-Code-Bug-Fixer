import numpy as np 

def function(x):

	l3 = 1
	z6 = 7
	paths = []
	try:
		if l3 > 5:
			l3 = z6-l3
			x = 6*x
			paths.append(1)
		else:
			l3 = 2*4
			paths.append(2)
		if z6 < 3:
			l3 = l3+7
			l3 = l3-4
			x = l3-x
			paths.append(3)
		else:
			l3 = l3-4
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