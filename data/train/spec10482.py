import numpy as np 

def function(x):

	x7 = x
	l0 = 1
	paths = []
	try:
		if l0 < 9:
			l0 = l0+0
			paths.append(1)
		else:
			x = 5*3
			paths.append(2)
		if x7 <= 0:
			x = x/7
			x = 0*6
			x = 4-x
			paths.append(3)
		else:
			x7 = 0+x7
			x = 3-x
			l0 = l0*x7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))