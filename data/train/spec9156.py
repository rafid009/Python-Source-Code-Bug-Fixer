import numpy as np 

def function(x):

	n2 = x
	x4 = x
	paths = []
	try:
		if x > 5:
			x = x+1
			n2 = 5/n2
			paths.append(1)
		else:
			x = x/n2
			x = n2*7
			paths.append(2)
		if x4 > 0:
			x = 6-x
			paths.append(3)
		else:
			x = x*n2
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