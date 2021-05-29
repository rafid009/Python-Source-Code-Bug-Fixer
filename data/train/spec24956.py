import numpy as np 

def function(x):

	x1 = x
	v2 = 2
	paths = []
	try:
		if x >= 4:
			x1 = 7*x1
			paths.append(1)
		else:
			v2 = x*v2
			x = x*2
			paths.append(2)
		if v2 > 0:
			x = v2/x
			v2 = 2-x1
			paths.append(3)
		else:
			v2 = v2-1
			x1 = v2+x1
			v2 = 2*v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))