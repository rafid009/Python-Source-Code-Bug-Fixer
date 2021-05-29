import numpy as np 

def function(x):

	l3 = 0
	z6 = x
	paths = []
	try:
		if z6 <= 9:
			l3 = 5+l3
			paths.append(1)
		else:
			l3 = 3-5
			paths.append(2)
		if z6 <= 6:
			x = x+x
			x = x*l3
			paths.append(3)
		else:
			x = 4-8
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