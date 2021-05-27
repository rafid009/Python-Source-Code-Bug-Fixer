import numpy as np 

def function(x):

	l3 = x
	e5 = 5
	paths = []
	try:
		if e5 < 2:
			x = x-4
			l3 = 6+l3
			x = x+7
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if e5 < 4:
			l3 = e5-l3
			x = e5*x
			l3 = l3/x
			paths.append(3)
		else:
			l3 = l3-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))