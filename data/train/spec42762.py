import numpy as np 

def function(x):

	n0 = 2
	x2 = x
	paths = []
	try:
		if n0 <= 9:
			x = x-5
			x = x-n0
			paths.append(1)
		else:
			x2 = x2*n0
			x = x+x2
			x = x*0
			paths.append(2)
		if n0 <= 6:
			x2 = x2+x
			n0 = n0-x2
			paths.append(3)
		else:
			x2 = x2*n0
			x2 = x2-9
			x = n0+5
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