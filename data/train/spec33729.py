import numpy as np 

def function(x):

	l5 = 6
	x6 = x
	x = x
	paths = []
	try:
		if x6 < 5:
			l5 = x6+l5
			x = x+3
			paths.append(1)
		else:
			x6 = x6-3
			x6 = 4*8
			paths.append(2)
		if x > 3:
			x = 7/x
			x6 = x*x6
			paths.append(3)
		else:
			l5 = 0*4
			x6 = x6/2
			l5 = 5*6
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