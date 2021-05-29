import numpy as np 

def function(x):

	v0 = 9
	l0 = 0
	paths = []
	try:
		if x >= 7:
			v0 = 0-v0
			l0 = 0+5
			paths.append(1)
		else:
			l0 = l0*4
			l0 = 4+v0
			paths.append(2)
		if x >= 0:
			l0 = l0/2
			x = x/v0
			paths.append(3)
		else:
			x = l0+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))