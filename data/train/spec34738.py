import numpy as np 

def function(x):

	l0 = x
	k4 = 0
	paths = []
	try:
		if l0 >= 1:
			l0 = 1*9
			x = l0+6
			k4 = k4*7
			paths.append(1)
		else:
			x = x*x
			l0 = l0+2
			x = l0*x
			paths.append(2)
		if x >= 6:
			l0 = l0+7
			k4 = k4*6
			x = x/7
			paths.append(3)
		else:
			k4 = k4*x
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