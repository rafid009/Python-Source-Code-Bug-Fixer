import numpy as np 

def function(x):

	v3 = 6
	b9 = 1
	paths = []
	try:
		if v3 >= 6:
			v3 = b9+2
			b9 = b9*4
			v3 = 0/v3
			paths.append(1)
		else:
			v3 = v3+8
			paths.append(2)
		if x >= 6:
			v3 = v3*b9
			x = 0+9
			paths.append(3)
		else:
			v3 = x-8
			x = x*1
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