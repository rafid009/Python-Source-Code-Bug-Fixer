import numpy as np 

def function(x):

	v4 = x
	b2 = 9
	paths = []
	try:
		if v4 < 0:
			b2 = b2-7
			v4 = 9-6
			v4 = 9+v4
			paths.append(1)
		else:
			x = 5/x
			b2 = 3*b2
			v4 = 1*x
			paths.append(2)
		if x >= 9:
			v4 = 4+2
			x = b2-1
			paths.append(3)
		else:
			v4 = 2*1
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))