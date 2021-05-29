import numpy as np 

def function(x):

	v0 = 4
	l9 = x
	paths = []
	try:
		if x >= 0:
			v0 = x*5
			v0 = v0/4
			v0 = 2+v0
			paths.append(1)
		else:
			v0 = v0+8
			v0 = v0*3
			x = x-4
			paths.append(2)
		if l9 < 9:
			l9 = l9*l9
			paths.append(3)
		else:
			l9 = 6*l9
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