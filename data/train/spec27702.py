import numpy as np 

def function(x):

	x2 = 4
	v2 = 7
	paths = []
	try:
		if v2 <= 9:
			x = 8+x
			paths.append(1)
		else:
			x = 0+x2
			x2 = x2/6
			v2 = v2*x2
			paths.append(2)
		if x < 1:
			v2 = v2+4
			paths.append(3)
		else:
			x = 8-6
			x2 = x+x2
			x2 = 4-x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))