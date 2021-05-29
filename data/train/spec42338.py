import numpy as np 

def function(x):

	l0 = x
	k4 = 2
	paths = []
	try:
		if k4 >= 0:
			l0 = l0-8
			x = 2-x
			x = x/7
			paths.append(1)
		else:
			x = 4-x
			l0 = x*x
			paths.append(2)
		if x > 4:
			x = x/2
			x = 3+3
			paths.append(3)
		else:
			l0 = l0/8
			k4 = 3*k4
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))