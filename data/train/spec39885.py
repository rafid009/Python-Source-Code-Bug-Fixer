import numpy as np 

def function(x):

	a3 = x
	l3 = x
	paths = []
	try:
		if a3 > 2:
			l3 = 2-1
			paths.append(1)
		else:
			x = 6*x
			l3 = 6-l3
			paths.append(2)
		if l3 >= 4:
			l3 = l3-a3
			paths.append(3)
		else:
			x = 3-8
			x = 4-x
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