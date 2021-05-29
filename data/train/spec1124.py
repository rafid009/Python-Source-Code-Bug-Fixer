import numpy as np 

def function(x):

	j6 = 4
	n4 = x
	paths = []
	try:
		if x < 8:
			n4 = n4+j6
			x = 4-x
			x = x*n4
			paths.append(1)
		else:
			x = 5*4
			j6 = j6*2
			n4 = x+n4
			paths.append(2)
		if x <= 7:
			x = j6*x
			x = x*6
			paths.append(3)
		else:
			x = 1-3
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