import numpy as np 

def function(x):

	l0 = 9
	v7 = 2
	paths = []
	try:
		if v7 > 2:
			v7 = 7/v7
			v7 = 0+x
			v7 = 9*v7
			paths.append(1)
		else:
			l0 = x-v7
			paths.append(2)
		if l0 <= 6:
			v7 = v7/l0
			x = x+5
			x = x-7
			paths.append(3)
		else:
			l0 = l0*l0
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